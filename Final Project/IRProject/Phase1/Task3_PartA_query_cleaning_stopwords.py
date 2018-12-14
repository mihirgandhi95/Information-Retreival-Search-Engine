import re
import pickle
from xml.etree import cElementTree as ElementTree
import os



#global variable
word_list = []




current_file = r'/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/cacm.query.txt'
data = open(current_file, 'r').read()
data = "<ROOT>\n" + data + "\n</ROOT>"
data = data.replace("</DOCNO>", "</DOCNO>\n<QUERY>")
xml_string_content = data.replace("</DOC>", "</QUERY>\n</DOC>")
query_dict = {}
root = ElementTree.fromstring(xml_string_content)
encoded_dir = r'./Task3_Data_Stopped/'
if not os.path.exists(encoded_dir):
    os.makedirs(encoded_dir)




def query_cleaning_stopwords():
    global word_list
    for query in root:
        q_id = query.find('DOCNO').text.strip()
        query_term = query.find('QUERY').text
        query_term = query_term.lower().replace("\n", " ")
        query_term = re.sub(' +', ' ', query_term).strip()
        query_term = re.sub(r"[^0-9A-Za-z,-\.:\\$]", " ", query_term)  # retain alpha-numeric text along with ',',':' and '.'
        query_term = re.sub(r"(?!\d)[$,%,:.,-](?!\d)", " ", query_term, 0)  # retain '.', '-' or ',' between digits
        query_term = query_term.split()
        for rt in query_term:
            if rt.startswith('-'):
                rt.replace(rt, rt.split('-')[1])
            if rt.endswith('-'):
                rt.replace(rt, rt.split('-')[0])
            else:
                continue
        query_term = [x for x in query_term if x not in word_list]  # remove stop words from the list
        query_term = ' '.join(query_term)
        query_dict[q_id] = query_term



def create_word_list():
    global word_list
    with open('/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/common_words', 'r') as f:
        lines = f.readlines()
    lines = [x.strip() for x in lines]
    word_list.extend(lines)


def write_to_file():
    f = open("Cleaned_Queries_Stopped.txt", 'w', encoding='utf-8')
    for id in query_dict:
        f.write(id + "\t" + query_dict[id] + "\n")
    f.close()

    output = open(encoded_dir + 'Encoded-Cleaned_Queries_Stopped.txt', 'wb')
    pickle.dump(query_dict, output)
    output.close()


def main():
    create_word_list()
    query_cleaning_stopwords()
    write_to_file()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
