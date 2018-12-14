import pickle
import math
import collections
import os




with open("Task1_Data/encoded_inverted_index.txt", 'rb') as reader1:
    inverted_index = pickle.loads(reader1.read())
with open("Task1_Data/encoded_inverted_index_docs.txt", 'rb') as reader2:
    inverted_index_docID_doclength = pickle.loads(reader2.read())
with open("Data_Encoded(Pseudo_Relevance)/encoded_expanded_queries.txt", 'rb') as reader3:
    query_term_dictionary = pickle.loads(reader3.read())
with open("Task1_Data/Encoded_Query_ID_BM25_relevance.txt", 'rb') as reader4:
    query_ID_relevance_documents = pickle.loads(reader4.read())


final_dictionary = {}
query_ID_number_of_relevant_documents = {}
for string in query_ID_relevance_documents:
    query_ID_number_of_relevant_documents[string] = len(query_ID_relevance_documents[string])

query_list = list(query_term_dictionary.values())



def calculate_r_score(term, counter2):
    r = 0
    relevant_document_list = query_ID_relevance_documents[str(counter2)]

    for document in relevant_document_list:
        reader1 = open('Task1_Output_Tokens/' + document + '.txt', 'r')
        text = reader1.read()
        text_terms = text.split()

        if term in text_terms:
            r += 1
    return r


def bestmatch25(f, n, L, R, r, q):
    k1 = 1.2
    k2 = 100
    b = 0.75
    N = len(inverted_index_docID_doclength.keys())
    K = k1 * ((b * L) + (1 - b))
    term1 = (k2 + 1) * q / (k2 + q)
    term2 = (k1 + 1) * f / (K + f)
    term3 = (r + 0.5) * (N - n - R + r + 0.5)
    term4 = (n - r + 0.5) * (R - r + 0.5)

    bm_score = term1 * term2 * math.log(term3 / term4)

    return bm_score






def Calculate_Score_for_BM25(q, R, id):
    average_document_length = sum(inverted_index_docID_doclength.values()) / len(inverted_index_docID_doclength.keys())
    final_dictionary = {}
    terms = q.split()
    if str(id) in query_ID_relevance_documents.keys():
        for term in terms:
            if term in inverted_index:
                r = calculate_r_score(term, id)
                qf = terms.count(term)
                for doc in inverted_index[term]:
                    if doc[0] not in final_dictionary.keys():
                        final_dictionary[doc[0]] = bestmatch25(doc[1], len(inverted_index[term]),
                                                   (inverted_index_docID_doclength[doc[0]] / average_document_length), R, r, qf)
                    else:
                        final_dictionary[doc[0]] += bestmatch25(doc[1], len(inverted_index[term]),
                                                    (inverted_index_docID_doclength[doc[0]] / average_document_length), R, r, qf)

    return final_dictionary


def BM25_relevance_with_PRF():
    writer = open('BM25_relevance_PRF_Top100_pages.txt', 'w')

    writer.write('ranking for expanded queries')

    writer.write('query_id Q0 document_id rank BM25_Score system_title' + "\n\n")

    for x in query_term_dictionary:
        rank = 1
        R = query_ID_number_of_relevant_documents[x]
        bm25_score = Calculate_Score_for_BM25(query_term_dictionary[x], R, x)
        final_dictionary1 = collections.OrderedDict(sorted(bm25_score.items(), key=lambda y: y[1], reverse=True))
        writer.write('\nFor query : %s\n\n' % query_term_dictionary[x])
        for id in final_dictionary1:
            if rank < 100:
                rank += 1
                writer.write('%d Q0 %s %d %s BM25_model\n' % (int(x), id, rank, final_dictionary1[id]))

        location = r'/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Data_Encoded(Pseudo_Relevance)/Encoded-BM25-Relevance-PRF-Top100Docs-perQuery/'
        if not os.path.exists(location):
            os.makedirs(location)

        writer2 = open(location + 'Top_100_PRF_Relevant_Documents' + '_%d' % int(x) + '.txt', 'wb')
        pickle.dump(final_dictionary1, writer2)
        writer2.close()

    writer.close()


def bestmatch25():
    BM25_relevance_with_PRF()


def main():
    bestmatch25()

if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
