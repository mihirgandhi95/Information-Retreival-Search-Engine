import os
import pickle

query_top100 = {}
input_path = r'/Users/nehagundecha/PycharmProjects/IRProject/Phase1/Task1_TF_IDF/Encoded-TF-IDF-Normalized-Top100Docs-perQuery'
output_path = r'./Task_Data/'


def init():
    if not os.path.exists(output_path):
        os.makedirs(output_path)


def encoder_documents():
    for file in os.listdir(input_path):
        f = os.path.join(input_path, file)
        query_number = f.split("Encoded-Top100Docs-TF-IDF-Normalized_")
        split = query_number[1].split(".")
        key = split[0]
        with open(f, 'rb') as f:
            score = pickle.loads(f.read())
        documents = list(score.keys())
        documents_top100 = documents[:100]
        query_top100[key] = documents_top100


def write_to_file():
    output = open(output_path + 'Encoded-QueryID_Top100Docs_tf-idf_normalized.txt', 'wb')
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
