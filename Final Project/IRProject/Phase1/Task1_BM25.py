import os
import pickle
import math
import collections


def access_Task1_Data():
    with open("./Task1_Data/encoded_inverted_index.txt", 'rb') as reader1:
        inverted_index = pickle.loads(reader1.read())
    with open("./Task1_Data/encoded_inverted_index_docs.txt", 'rb') as reader2:
        inverted_index_docID_doclength = pickle.loads(reader2.read())
    with open("./Task1_Data/encoded_clean_queries.txt", 'rb') as reader3:
        query_term_dictionary = pickle.loads(reader3.read())

    query_term_list = list(query_term_dictionary.values())

    write_BM25_score_to_file(inverted_index, inverted_index_docID_doclength,
                             query_term_dictionary, query_term_list)


def BM25_calc(f, n, L, R, r, q, m):
    k1 = 1.2
    k2 = 100
    b = 0.75
    N = len(m.keys())
    K = k1 * ((b * L) + (1 - b))
    term1 = (k2 + 1) * q / (k2 + q)
    term2 = (k1 + 1) * f / (K + f)
    term3 = (r + 0.5) * (N - n - R + r + 0.5)
    term4 = (n - r + 0.5) * (R - r + 0.5)

    bm_score = term1 * term2 * math.log(term3 / term4)

    return bm_score


def score_calculation(inverted_index, inverted_index_docID_doclength, query_term_dictionary, query_term_list, query_term):
    bm25_score_final = {}

    average_document_length = sum(inverted_index_docID_doclength.values()) / len(inverted_index_docID_doclength.keys())

    terms_in_query = query_term.split()
    for term in terms_in_query:
        if term in inverted_index:
            query_frequency = terms_in_query.count(term)
            for document in inverted_index[term]:
                if document[0] not in bm25_score_final.keys():
                    bm25_score_final[document[0]] = BM25_calc(document[1], len(inverted_index[term]),(inverted_index_docID_doclength[document[0]] /average_document_length), 0, 0, query_frequency,inverted_index_docID_doclength)
                else:
                    bm25_score_final[document[0]] += BM25_calc(document[1], len(inverted_index[term]),(inverted_index_docID_doclength[document[0]] /average_document_length), 0, 0, query_frequency,inverted_index_docID_doclength)

    return bm25_score_final


def write_to_files(top_5_documents, top_5_dictionary_for_pseudo_relevance):
    top_5_document_list = open('./Task1_BM25/BM25_Top5_Documents.txt', 'w')
    for document in top_5_documents:
        for item in document:
            top_5_document_list.write(item + "\n")
    top_5_document_list.close()

    writer1 = open('./Task1_BM25/BM25_Top5_Query_Pages.txt', 'w')
    writer1.write(str(top_5_dictionary_for_pseudo_relevance))
    writer1.close()

    writer2 = open('./Task1_BM25/Encoded_BM25_Top5_Query_Pages.txt', 'wb')
    pickle.dump(top_5_dictionary_for_pseudo_relevance, writer2)
    writer2.close()


def PseudoRelevance(top_5_dictionary_for_pseudo_relevance):
    top_5_documents = list(top_5_dictionary_for_pseudo_relevance.values())
    write_to_files(top_5_documents, top_5_dictionary_for_pseudo_relevance)


def write_BM25_score_to_file(inverted_index, inverted_index_docID_doclength,
                             query_term_dictionary, query_term_list):
    BM25Folder = './Task1_BM25/'
    if not os.path.exists(BM25Folder):
        os.makedirs(BM25Folder)

    top_5_dictionary_for_pseudo_relevance = {}

    writer = open('./Task1_BM25/BM25_Top_100_No_Relevance.txt', 'w')

    writer.write('Cleaned Queries Ranked (Top 100)' + '\n')
    writer.write('query_id Q0 document_id rank BM25_Score system_title' + "\n\n")
    counter = 1
    for query_term in query_term_dictionary.values():
        rank = 1
        BM25_score = score_calculation(inverted_index, inverted_index_docID_doclength,
                                       query_term_dictionary, query_term_list, query_term)
        bm25_score_final = collections.OrderedDict(sorted(BM25_score.items(), key=lambda x: x[1], reverse=True))
        writer.write('\n For Query: %s \n\n' % query_term)
        for query_id in bm25_score_final:
            if rank <= 100:
                writer.write(
                    '%d Q0 %s %d %s BM25_Model\n' % (counter, query_id, rank, bm25_score_final[query_id]))

            if rank <= 5:
                if query_term not in top_5_dictionary_for_pseudo_relevance.keys():
                    top_5_dictionary_for_pseudo_relevance[query_term] = [query_id]
                else:
                    top_5_dictionary_for_pseudo_relevance[query_term].append(query_id)
            rank += 1
        BM25SubFolder = r'./Task1_BM25/Encoded_BM25_Top100_perQuery/'
        if not os.path.exists(BM25SubFolder):
            os.makedirs(BM25SubFolder)

        writer2 = open(BM25SubFolder + 'Encoded_Top100_BM25_query' + '%d' % counter + '.txt', 'wb')
        pickle.dump(bm25_score_final, writer2)
        writer2.close()
        counter += 1
    writer.close()

    PseudoRelevance(top_5_dictionary_for_pseudo_relevance)


def BM25():
    access_Task1_Data()


def main():
    BM25()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
