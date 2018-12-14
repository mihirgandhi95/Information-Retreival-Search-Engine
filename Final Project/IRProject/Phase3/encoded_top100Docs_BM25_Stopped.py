import pickle
import os

query_top100 = {}
output_path = r'./Task_Data/'
input_path = r'/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task3_Data_Stopped/Encoded-Stopped_BM25-NoRelevance-Top100Docs-perQuery'


def init():
    if not os.path.exists(output_path):
        os.makedirs(output_path)


def encoder_documents():
    for file in os.listdir(input_path):
        f = os.path.join(input_path, file)
        query_number = f.split("Encoded-Top100Docs-Stopped_BM25-NoRelevance_")
        split = query_number[1].split(".")
        key = split[0]
        with open(f, 'rb') as f:
            score = pickle.loads(f.read())
        documents = list(score.keys())
        documents_top100 = documents[:100]
        query_top100[key] = documents_top100


def write_to_file():
    output = open(output_path + 'Encoded-QueryID_Top100Docs_Stopped_BM25_NoRelevance.txt', 'wb')
    pickle.dump(query_top100, output)
    output.close()


def main():
    init()
    encoder_documents()
    write_to_file()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
