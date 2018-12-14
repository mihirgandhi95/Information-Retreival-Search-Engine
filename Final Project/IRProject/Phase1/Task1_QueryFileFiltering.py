import re
import os
import pickle
from xml.etree import cElementTree as ElementTree


def open_query_file_extract_content():
    file = r'/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/cacm.query.txt'
    text = open(file, 'r').read()
    return text


def create_XML_document(text):
    text = "<ROOT>\n" + text + "\n</ROOT>"
    text = text.replace("</DOCNO>", "</DOCNO>\n<QUERY>")
    xml_Content = text.replace("</DOC>", "</QUERY>\n</DOC>")
    xml_Root = ElementTree.fromstring(xml_Content)

    return xml_Root


def filter_query(xml_Root):
    query_term_dictionary = {}
    for query in xml_Root:
        query_id = query.find('DOCNO').text.strip()
        query_text = query.find('QUERY').text
        query_text = query_text.lower().replace("\n", " ")
        query_text = re.sub(' +', ' ', query_text).strip()
        query_text = re.sub(r"[^0-9A-Za-z,-\.:\\$]", " ", query_text)
        query_text = re.sub(r"(?!\d)[$,%,:.,-](?!\d)", " ", query_text, 0)
        query_text = query_text.split()
        for data in query_text:
            if data.startswith('-'):
                data.replace(data, data.split('-')[1])
            if data.endswith('-'):
                data.replace(data, data.split('-')[0])
            else:
                continue
        query_text = ' '.join(query_text)
        query_term_dictionary[query_id] = query_text
    return query_term_dictionary


def write_to_files(query_term_dictionary):
    datafolder = './Task1_Data/'
    if not os.path.exists(datafolder):
        os.makedirs(datafolder)
    writer = open("clean_queries" + '.txt', 'w', encoding='utf-8')
    for query_id in query_term_dictionary:
        writer.write(query_id + "\t" + query_term_dictionary[query_id] + "\n")
    writer.close()
    writer2 = open(datafolder + 'encoded_clean_queries.txt', 'wb')
    pickle.dump(query_term_dictionary, writer2)
    writer2.close()


def query_filtering():
    text = open_query_file_extract_content()
    xml_Root = create_XML_document(text)
    query_term_dictionary = filter_query(xml_Root)
    write_to_files(query_term_dictionary)


def main():
    query_filtering()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
