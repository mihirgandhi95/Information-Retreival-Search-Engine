import collections
import os
import pickle

# This stores the terms and their frequency
dictionary = {}

# dictionary with key as docID and value as corresponding document length
documents_ID_length = {}

# This directory contains encoded data which will be used later
datafolder = './Task1_Data/'
if not os.path.exists(datafolder):
    os.makedirs(datafolder)

input_tokens = r'./Task1_Output_Tokens/'

# This contains the inverted index built upon the CACM corpus
output_inverted_index = open('inverted_list_to_use.txt', 'w+', encoding='utf-8')
# This contains the inverted list of docs
output_inverted_index_docs = open("document_id_document_length.txt", 'w', encoding='utf-8')

# Dumping the files using pickle to be used later
output_encoded_inverted_index = open(datafolder + 'encoded_inverted_index.txt', 'wb')
output_encoded_inverted_index_docs = open(datafolder + 'encoded_inverted_index_docs.txt', 'wb')


def inverted_index(filename):
    inv_index_unigram = {}
    current_file = os.path.join(input_tokens, filename)
    terms = open(current_file, 'r').read()
    term_list = terms.split()
    documents_ID_length[filename[:-4]] = len(term_list)
    for term in term_list:
        if terms.count(term) == 0:
            continue
        else:
            dictionary[term] = terms.count(term)
        tup = filename[:-4], dictionary[term]
        inv_index_unigram[term] = tup
    return inv_index_unigram


def task1_indexer():
    inverted_list = {}
    for file in os.listdir(input_tokens):
        print("Inverted index list for: " + str(file))
        inverted_list_posting = inverted_index(file)
        for term in inverted_list_posting:
            if term in inverted_list:
                # append the (docID,tf) for the term if the same term appears in another document
                inverted_list[term].append(inverted_list_posting[term])
            else:
                inverted_list[term] = [inverted_list_posting[term]]

    # Sorting the inverted list
    inv_list_unigram = collections.OrderedDict(sorted(inverted_list.items()))
    write_to_file(inv_list_unigram)


def write_to_file(inv_list_unigram):
    for term in inv_list_unigram:
        output_inverted_index.write("%s -> %s\n" % (term, inv_list_unigram[term]))
    output_inverted_index.close()

    output_inverted_index_docs.write(str(documents_ID_length))
    output_inverted_index_docs.close()

    pickle.dump(inv_list_unigram, output_encoded_inverted_index)
    output_encoded_inverted_index.close()

    pickle.dump(documents_ID_length, output_encoded_inverted_index_docs)
    output_encoded_inverted_index_docs.close()

    print("\n Generated Inverted Index!")


def main():
    task1_indexer()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
