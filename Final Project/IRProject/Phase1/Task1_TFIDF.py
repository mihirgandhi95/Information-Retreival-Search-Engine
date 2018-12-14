import pickle
import math
import collections
import os


# inverted_index = {}
# docs_ID_len = {}
# query_dict = {}

with open("./Task1_Data/encoded_inverted_index.txt", 'rb') as f:
    inverted_index = pickle.loads(f.read())

with open("./Task1_Data/encoded_inverted_index_docs.txt", 'rb') as f:
    docs_ID_len = pickle.loads(f.read())

with open("./Task1_Data/encoded_clean_queries.txt", 'rb') as f:
    query_dict = pickle.loads(f.read())

# Program to calculate tf-idf score for document

query_list = list(query_dict.values())  # Contains all the queries required

# This represents a dictionary containing the document IDs with their corresponding TF-IDF scores
final_score = {}


# This function calculates the tf-idf score for a document
# term_freq = term frequency
# document_freq = document frequency
# modD = Document size
# inverse_document_frequency = Inverse document frequency
def tf_idf_score(term_freq, document_freq, modD):
     N = len(docs_ID_len.keys())
     inverse_document_frequency = math.log(N / document_freq + 1) + 1
     normalized_tf = term_freq / modD
     score = normalized_tf * inverse_document_frequency

     return score


# This functions calculates the final score for a document using TF-IDF model
def doc_score(query_term):
    Final_Score_Dictionary = {}
    term_list = query_term.split()
    for x in term_list:
        if x in inverted_index:
            for y in inverted_index[x]:
                if y[0] not in Final_Score_Dictionary.keys():
                    Final_Score_Dictionary[y[0]] = tf_idf_score(y[1], len(inverted_index[x]), docs_ID_len[y[0]])
                else:
                    Final_Score_Dictionary[y[0]] += tf_idf_score(y[1], len(inverted_index[x]), docs_ID_len[y[0]])
    return Final_Score_Dictionary


def write_to_folder(count, score):
    path_to_write_files = r'./Task1_TF_IDF/TF_IDF_Top100_Docs_Encoded/'
    if not os.path.exists(path_to_write_files):
        os.makedirs(path_to_write_files)
    output = open(
        path_to_write_files + 'TF_IDF_Top100_Docs_Encoded' + '_%d' % count + '.txt', 'wb')
    pickle.dump(score, output)
    output.close()


def task1_TF_IDF():
    count = 1
    f = open('./Task1_TF_IDF/TF_IDF_top100_Pages.txt', 'w')

    f.write('Top 100:' + "\n")
    f.write('Format: query_id Q0 doc_id rank TF-IDF-score system_name' + "\n\n")

    for query_term in query_list:
        rank = 1
        print("Calculating TF-IDF score for queries" + query_term)
        TFIDF_score = doc_score(query_term)


        score = collections.OrderedDict(sorted(TFIDF_score.items(), key=lambda x: x[1], reverse=True))

        f.write(' \n \n Every query : %s \n\n' % query_term)


        for query_id in score:
            if rank < 100:
                f.write('%d Q0 %s %d %s TF_IDF_Model\n' % (count, query_id, rank, score[query_id]))

            rank += 1

        write_to_folder(count, score)
        count += 1
    f.close()

    print("\nScored documents using TF IDF Model")

def create_folder():
    doc_score_folder = './Task1_TF_IDF/'
    if not os.path.exists(doc_score_folder):
        os.makedirs(doc_score_folder)

    doc_score_folder = './Task1_TF_IDF/TF_IDF_Top100_Docs_Encoded/'
    if not os.path.exists(doc_score_folder):
        os.makedirs(doc_score_folder)


def main():

    # open_files_and_assign_values()
    create_folder()

    task1_TF_IDF()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
