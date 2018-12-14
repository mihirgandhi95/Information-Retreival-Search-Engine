import os
import pickle

query_top100 = {}
output_path = r'./Task_Data/'
documents_top100 = []


def init():
    if not os.path.exists(output_path):
        os.makedirs(output_path)


def set_top100_docs():
    with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Lucene_Top100_Docs.txt", 'r', encoding='utf-8') as f:
        line = f.readlines()
    line = [x.strip() for x in line]
    documents_top100.extend(line)


def encoder_documents():
    count = 0
    index = 1
    for d in documents_top100:
        if count < 100:
            if index not in query_top100:
                query_top100[index] = []
            query_top100[index].append(d)
            count += 1
            continue
        index += 1
        count = 1
        query_top100[index] = []
        if len(query_top100) == 0:
            query_top100[index].append(d)


def write_to_file():
    output = open(output_path + 'Encoded-QueryID_Top100Docs_Lucene.txt', 'wb')
    pickle.dump(query_top100, output)
    output.close()


def main():
    init()
    set_top100_docs()
    encoder_documents()
    write_to_file()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
