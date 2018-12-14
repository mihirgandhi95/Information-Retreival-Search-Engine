import collections
import os
import pickle

document1 = {}
document_ID_document_length = {}


encoded_dir = r'./Task3_Data_Stopped/'
if not os.path.exists(encoded_dir):
    os.makedirs(encoded_dir)

def Stop_Indexer():
    print("")

def inverted_index(filename):
    unigram_inverted_index = {}
    current_file = os.path.join(path, filename)
    terms = open(current_file, 'r').read()
    term_list = terms.split()
    document_ID_document_length[file[:-4]] = len(term_list)
    for term in term_list:
        if terms.count(term) == 0:
            continue
        else:
            document1[term] = terms.count(term)
        tup = file[:-4], document1[term]
        unigram_inverted_index[term] = tup
    unigram_inverted_index




inverted_list_ancestor = {}
path = r'./Task3_PartA_Stopping_tokens_output/'
for file in os.listdir(path):
    child_inverted_list = inverted_index(file)
    for term in child_inverted_list:

        if term in inverted_list_ancestor:

            inverted_list_ancestor[term].append(child_inverted_list[term])

        else:

            inverted_list_ancestor[term] = [child_inverted_list[term]]

unigram_inverted_list = collections.OrderedDict(sorted(inverted_list_ancestor.items()))







writer1 = open('Stopped_Inverted_List.txt', 'w+', encoding='utf-8')
for term in unigram_inverted_list:
    writer1.write("%s -> %s\n" % (term, unigram_inverted_list[term]))
writer1.close()

f = open("Stopped_DocumentID_DocLen.txt", 'w', encoding='utf-8')
f.write(str(document_ID_document_length))
f.close()


writer2 = open(encoded_dir + 'Encoded-Stopped_Inverted_List.txt', 'wb')
pickle.dump(unigram_inverted_list, writer2)
writer2.close()

writer3 = open(encoded_dir + 'Encoded-Stopped_DocumentID_DocLen.txt', 'wb')
pickle.dump(document_ID_document_length, writer3)
writer3.close()


def main():
    Stop_Indexer()
    # write_to_file()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
