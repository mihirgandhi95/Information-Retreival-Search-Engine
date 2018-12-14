import pickle



with open("Data_Encoded(Pseudo_Relevance)/expanded_encoded_queries.txt", 'rb') as reader1:
    expansion_terms_query = pickle.loads(reader1.read())

with open("Task1_Data/Encoded_Query_ID_BM25_relevance.txt",
          'rb') as reader2:
    query_id_relevant_documents_dict = pickle.loads(reader2.read())




query_keys = list(expansion_terms_query.keys())

query_list = []

for x in query_keys:
    query_list.append(x.split())

expanded_list = list(expansion_terms_query.values())

list_queries_expanded = []


final_query_term_dictionary = {}
keys = list(query_id_relevant_documents_dict.keys())

def get_expanded_query():
    counter = 0
    while counter < len(query_list):
        checker_list_queries_expanded = (query_list[counter]+ expanded_list[counter])
        final_list = []


        for x in checker_list_queries_expanded:
            if x not in final_list:
                final_list.append(x)
        list_queries_expanded.append(final_list)
        counter += 1



def write_to_file():
    counter2 = 0
    for xtree in list_queries_expanded:
        expanded_query_b = ' '.join(xtree)
        final_query_term_dictionary[keys[counter2]] = expanded_query_b
        counter2 += 1

    path_to_write = open(
        'Data_Encoded(Pseudo_Relevance)/encoded_expanded_queries.txt', 'wb')
    pickle.dump(final_query_term_dictionary, path_to_write)

    path_to_write.close()

def BM25():
    get_expanded_query()
    write_to_file()


def main():
    BM25()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')