import pickle


def write_to_file(relevance_dictionary):
    writer = open('Task1_Data/Encoded_Query_ID_BM25_relevance.txt', 'wb')
    pickle.dump(relevance_dictionary, writer)
    writer.close()


def create_relevance_dictionary(text):
    relevance_dictionary = {}
    for line in text:
        elements_in_line = line.split(" ")
        splitter = elements_in_line[2].split("-")
        if int(splitter[1]) < 1000:
            splitter[1] = '{0}'.format(splitter[1].zfill(4))

        temp = splitter[0] + '-' + splitter[1]
        query_id = elements_in_line[0]

        if query_id in relevance_dictionary:
            relevance_dictionary[query_id].append(temp)
        else:
            relevance_dictionary[query_id] = []
            relevance_dictionary[query_id].append(temp)

    print(relevance_dictionary)

    write_to_file(relevance_dictionary)


def create_dictionary():
    relevance_judgements = r'cacm.rel.txt'
    text = open(relevance_judgements, 'r').read()
    text = text.split("\n")
    text = [x for x in text if x != ""]
    create_relevance_dictionary(text)


def main():
    create_dictionary()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
