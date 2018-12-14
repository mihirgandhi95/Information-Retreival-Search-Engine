from bs4 import BeautifulSoup
import re
import os
import pickle

# Initialises all the file paths
output_html = "./Snippets_HTML/"
output_text = "./Snippets_Text/"
clean_queries_path = "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/encoded_clean_queries.txt"
corpus_path = "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/cacm/"
inverted_list_path = "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task3_Data_Stopped/Encoded-Stopped_Inverted_List.txt"

files = []
output_snippets_text = []
output_snippets_html = []
common_words = []
docId_sentence_dict = {}
sentences_all = []

dict = {}
master_dict = {}
inverted_list_stopped = {}
list_words = []

with open(inverted_list_path, 'rb') as file:
    inverted_list_stopped = pickle.loads(file.read())

with open(clean_queries_path, 'rb') as file:
    query_dict = pickle.loads(file.read())


def init():
    if not os.path.exists(output_html):
        os.makedirs(output_html)
    if not os.path.exists(output_text):
        os.makedirs(output_text)
    files.append(
        "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Stopped_BM25_NoRelevance_Top5_Docs.txt")
    output_snippets_text.append(output_text + 'Snippets_Stopped_BM25_NoRelevance.txt')
    output_snippets_html.append(output_html + 'Snippets_Stopped_BM25_NoRelevance.html')

    # Generating the common words dictionary from common_words.txt
    with open('/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/common_words', 'r') as f:
        l = f.readlines()
    l = [x.strip() for x in l]
    common_words.extend(l)


# This function calls the snippet generation algorithm for all the systems
def phase2():
    for i in range(0, len(files)):
        print("\nDONE\n\n")
        generate_snippet(files[i], output_snippets_text[i], output_snippets_html[i])


# This functions is the driver function for generating snippets for all the systems
def generate_snippet(files, output_text, output_html):
    for file in os.listdir(corpus_path):
        print("Generating Snippets for File: " + file)
        current_file = os.path.join(corpus_path, file)

        # Tokenizing
        page_content = open(current_file, 'r').read()
        soup = BeautifulSoup(page_content, "html.parser")
        for content in soup.find_all("html"):
            content_text = content.text
            text = content_text.split('\n')
            for element in text:
                if element is "":
                    text.remove(element)

            result_text = '\n'.join(text)
            index_of_am = result_text.rfind("AM")  # contains the last index of the term "AM"
            index_of_pm = result_text.rfind("PM")  # contains the last index of the term "PM"

            # retain the text content uptil AM or PM in the corpus documents

            if index_of_am > index_of_pm:
                greater_index = index_of_am
            else:
                greater_index = index_of_pm
            result_text = result_text[:(greater_index + 2)]
            # Handling alpha numeric data
            result_text = re.sub(r"[^0-9A-Za-z,-\.:\\$]", " ", result_text)
            # Handling data between digits e.g. retaining dates of the format 2017-11-22 etc
            result_text = re.sub(r"(?!\d)[$,%,:.,-](?!\d)", " ", result_text, 0)
            # Handling spaces
            result_text = re.sub(r' +', ' ', result_text).strip()

            list_of_words = result_text.split()
            i = 0
            j = 0
            each = []
            for element in list_of_words:
                if i == 0:
                    each.append([])
                    each[j].append(element)
                    i += 1
                elif i < 10:
                    each[j].append(element)
                    i += 1
                else:
                    j += 1
                    each.append([])
                    each[j].append(element)
                    i = 1

            sentences = []
            for e in each:
                s = ""
                for element in e:
                    s += " " + str(element)
                sentences.append(s.strip())
            docId_sentence_dict[file[:-5]] = sentences

    with open(files, 'r') as file:
        ret = file.read().split()

    for k, v in docId_sentence_dict.items():
        for sentence in v:
            sentences_all.append(sentence)

    j = 0
    for i in range(0, int(len(ret) / 5)):
        list_doc = [ret[j], ret[j + 1], ret[j + 2], ret[j + 3], ret[j + 4]]
        dict[i + 1] = list_doc
        j += 5

    write_output_html(output_text, output_html)


def get_top_3(sentence_list, score_list):
    highThree = sorted(zip(score_list, sentence_list), reverse=True)[:3]
    return highThree


# This function is used for writing the snippet in html and text format
def write_output_html(output_text, output_html):
    file_output_text = open(output_text, 'w')
    file_output_html = open(output_html, 'w')
    file_output_html.write("<html>\n<body>\n\n")
    for query_id, docs in dict.items():
        master_dict[query_id] = []
        for doc in docs:
            master_dict[query_id].append((doc, docId_sentence_dict[doc]))

    for query_id, doclist in master_dict.items():
        file_output_text.write("\n=======================================================================\n")
        file_output_text.write("Query " + str(query_id) + ": " + query_dict[str(query_id)])
        file_output_text.write("\n=======================================================================\n")
        file_output_text.write("\n\nSnippets for top 5 documents:\n\n")
        i = 0
        for doc in doclist:
            i += 1
            s_list = []
            for sentence in doc[1]:
                words = sentence.split(" ")
                s = get_significant_words(words, doc[0], len(doc[1]))
                s_list.append(s)

            file_output_text.write(str(i) + ". " + doc[0] + "\n\n")
            file_output_html.write(str(i) + ". " + doc[0] + "<br>")
            top_3 = get_top_3(doc[1], s_list)
            ss = []
            sentences = []
            for s in top_3:
                ss.append(s[0])
                sentences.append(s[1])
            highlighted_sentences = []
            query_terms = query_dict[str(query_id)].split(" ")

            for sentence in sentences:
                highlighted_sentence_terms = []
                for term in sentence.split(" "):
                    # Query term highlighting
                    if term.lower() in query_terms and term.lower() not in common_words:
                        highlighted_sentence_terms.append("<b>" + term + "</b>")
                    else:
                        highlighted_sentence_terms.append(term)
                highlighted_sentences.append(" ".join(highlighted_sentence_terms).replace("</b> <b>", " "))

            final_snippet = " ... ".join(highlighted_sentences)

            file_output_text.write("Snippet: ")
            file_output_text.write(final_snippet)
            file_output_text.write("\n\n")

            file_output_html.write("<p>" + final_snippet + "</p>")

    file_output_html.write("\n\n</body>\n</html>")


# Significance factor of a sentence
def get_significant_words(words, doc, num_of_sentences):
    if num_of_sentences < 25:
        threshold = 4 - 0.1 * (25 - num_of_sentences)
    elif num_of_sentences <= 40:
        threshold = 4
    else:
        threshold = 4 + 0.1 * (num_of_sentences - 40)
    list_words = []
    significant_words = []
    for word in words:
        if word.lower() not in common_words:
            val = inverted_list_stopped[word.lower()]
            for x in val:
                if doc == x[0]:
                    if x[1] >= threshold:
                        list_words.append(1)
                        if word not in significant_words:
                            significant_words.append(word)
                    else:
                        list_words.append(0)
        else:
            list_words.append(0)
    if 1 in list_words:
        start = list_words.index(1)
        end = len(list_words) - list_words[::-1].index(1) - 1
        numberof1 = list_words.count(1)
        total_bracketed = end - start + 1
        significance_factor = (numberof1 ** 2) / total_bracketed
        return significance_factor
    else:
        return 0


def main():
    init()
    phase2()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
