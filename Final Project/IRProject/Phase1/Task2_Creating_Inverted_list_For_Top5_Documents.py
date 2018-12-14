import pickle
import collections

with open("Task1_Data/encoded_clean_queries.txt", 'rb') as f:
    query_ID = pickle.loads(f.read())

document_name = []

dictionary1 = {}

document_ID = 0

dictionary_with_document_id_document_length = {}

common_words_list = []

document_list = []




with open('common_words', 'r') as reader1:
    lines = reader1.readlines()
lines = [item.strip() for item in lines]
common_words_list.extend(lines)





with open('/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Data_Encoded(Pseudo_Relevance)/query_id_with_relevance_top_5_docs.txt', 'rb') as reader2:
    query_ID_with_top5_documents = pickle.loads(reader2.read())

for document_array in query_ID_with_top5_documents.values():
    document_list += document_array


def inverted_list():
    global document_list
    global common_words_list
    complete_top_5_word_list = []
    for document in document_list:
        top_5_word_list = []
        file_name_list = 'Task1_Output_Tokens/' + document + '.txt'

        reader = open(file_name_list, 'r').read()

        file_text = reader.split(" ")

        term_with_term_frequency_dictionary = {}

        for x in file_text:
            if x not in common_words_list:
                if x in term_with_term_frequency_dictionary:
                    term_with_term_frequency_dictionary[x] += 1
                else:
                    term_with_term_frequency_dictionary[x] = 1

        term_with_term_frequency_dictionary = collections.OrderedDict(sorted(term_with_term_frequency_dictionary.items(), key=lambda z : z[1], reverse = True))

        rank = 0
        for a in term_with_term_frequency_dictionary:
            if rank<5:
                top_5_word_list.append(a)
            rank += 1
        complete_top_5_word_list.append(top_5_word_list)
    write_to_file(complete_top_5_word_list)

def write_to_file(word_list):
    top5_words_array = []

    i = 1

    while i <= len(word_list):
        new_array = word_list[i-1] + word_list[i] + word_list[i+1] + word_list[i+2] + word_list[i+3]
        top5_words_array.append(new_array)
        i += 5

    query_term_title = list(query_ID.values())


    query_expanded = dict(zip(query_term_title,top5_words_array))

    path_to_read = open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Data_Encoded(Pseudo_Relevance)/expanded_encoded_queries.txt", 'wb')
    pickle.dump(query_expanded, path_to_read)

    path_to_read.close()


def main():
    # common_words()
    # document_list_creator()
    inverted_list()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')