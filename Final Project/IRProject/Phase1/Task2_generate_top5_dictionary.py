import os
import pickle
from collections import OrderedDict


path = r'Task1_BM25/Encoded_BM25_Relevance_Top5_perQuery/'


def get_dict():
    query_with_id_top5_documents = {}
    for file in os.listdir(path):
        existing_file = os.path.join(path, file)
        term_list = existing_file.split("Encoded_Top5_BM25_Relevance_query")
        id_new = term_list[1].split('.')[0]
        with open(existing_file, 'rb') as w:
            document_BM25_with_relevance = pickle.loads(w.read())
            document_list = list(document_BM25_with_relevance.keys())
            Top_5_Documents = document_list[:5]
            query_with_id_top5_documents[id_new] = Top_5_Documents

    query_with_id_top5_documents = OrderedDict(sorted(query_with_id_top5_documents.items(), key=lambda y: y, reverse=False))
    print(query_with_id_top5_documents)
    write_to_file(query_with_id_top5_documents)


#
def write_to_file(query_with_id_top5_documents):
    # global path_to_write
    writer = open(path_to_write + 'query_id_with_relevance_top_5_docs.txt', 'wb')
    pickle.dump(query_with_id_top5_documents, writer)
    writer.close()



def create_path():
    global path_to_write

    path_to_write = r'Data_Encoded(Pseudo_Relevance)/'
    if not os.path.exists(path_to_write):
        os.makedirs(path_to_write)

    path_2 = r'Task2_BM25/Encoded_BM25_Relevance_Top5_perQuery/'
    if not os.path.exists(path_2):
        os.makedirs(path_2)

def main():

    create_path()
    get_dict()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')