import pickle
import collections
import os

d1 = {}
doc_name = []
docID_doclen = {}
docID_docName = {}

encoded_dir = r'./Task3_Data_Stemmed/'
if not os.path.exists(encoded_dir):
    os.makedirs(encoded_dir)


def generate_ngrams(words_list, n):
    ngrams_list = []

    for num in range(0, len(words_list)):
        ngram = ' '.join(words_list[num:num + n])
        ngrams_list.append(ngram)

    return ngrams_list


def inverted_index(file):
    inv_index_unigram = {}
    current_file = os.path.join(path, file)
    terms = open(current_file, 'r').read()
    term_list = terms.split()
    docID_doclen[file[:-4]] = len(term_list)
    for term in term_list:
        if terms.count(term) == 0:
            continue
        else:
            d1[term] = terms.count(term)
        tuple = file[:-4], d1[term]
        inv_index_unigram[term] = tuple
    return inv_index_unigram


parent_inverted_list = {}
path = r'./Task3_PartB_Stemmed_Corpus'
for file in os.listdir(path):
    child_inverted_list = inverted_index(file)
    for term in child_inverted_list:

        if term in parent_inverted_list:
            parent_inverted_list[term].append(child_inverted_list[term])

        else:

            parent_inverted_list[term] = [child_inverted_list[term]]

inv_list_unigram = collections.OrderedDict(sorted(parent_inverted_list.items()))

output = open('Stemmed_Inverted_List.txt', 'w+', encoding='utf-8')
for term in inv_list_unigram:
    output.write("%s -> %s\n" % (term, inv_list_unigram[term]))
output.close()

output = open(encoded_dir + 'Encoded-Stemmed_Inverted_List.txt', 'wb')
pickle.dump(inv_list_unigram, output)
output.close()

f = open("Stemmed_DocumentID_DocLen.txt", 'w', encoding='utf-8')
f.write(str(docID_doclen))
f.close()

output = open(encoded_dir + 'Encoded-Stemmed_DocumentID_DocLen.txt', 'wb')
pickle.dump(docID_doclen, output)
output.close()
