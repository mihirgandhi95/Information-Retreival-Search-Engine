import re
import os

current_file = r'/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/cacm_stem.txt'
content = open(current_file, 'r').read()

output_path = r'./Task3_PartB_Stemmed_Corpus/'


def stemm_extraction():
    docs = re.split("# [\d]+", content)
    docs = [w for w in docs if w != ""]
    for i, doc in enumerate(docs, 1):
        print("Creating Stemmed Corpus file for CACM-" + str(i))
        f = open(output_path + 'CACM-' + str(i) + '.txt', 'w', encoding='utf-8')
        f.write(doc.strip())
        f.close()


def init():
    if not os.path.exists(output_path):
        os.makedirs(output_path)


def main():
    init()
    stemm_extraction()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
