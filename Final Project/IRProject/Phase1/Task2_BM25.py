import os
import pickle
import math
import collections


def access_Task1_Data():
    with open("Task1_Data/encoded_inverted_index.txt", 'rb') as reader1:
        inverted_index = pickle.loads(reader1.read())
    with open("Task1_Data/encoded_inverted_index_docs.txt", 'rb') as reader2:
        inverted_index_docID_doclength = pickle.loads(reader2.read())
    with open("Task1_Data/encoded_clean_queries.txt", 'rb') as reader3:
        query_term_dictionary = pickle.loads(reader3.read())
    with open("Task1_Data/Encoded_Query_ID_BM25_relevance.txt", 'rb') as reader4:
        query_ID_relevance_documents = pickle.loads(reader4.read())

    query_ID_number_of_relevant_documents = {}

    for id_new in query_ID_relevance_documents:
        query_ID_number_of_relevant_documents[id_new] = len(query_ID_relevance_documents[id_new])

    query_term_list = list(query_term_dictionary.values())

    write_BM25_score_to_file(inverted_index, inverted_index_docID_doclength,
                             query_term_dictionary, query_term_list, query_ID_relevance_documents,
                             query_ID_number_of_relevant_documents)


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


def compute_new_score_r(term, counter2, query_ID_relevance_documents):
    r = 0
    relevant_document_list = query_ID_relevance_documents[str(counter2)]

    for document in relevant_document_list:
        reader1 = open('Task1_Output_Tokens/' + document + '.txt', 'r')
        text = reader1.read()
        text_terms = text.split()

        if term in text_terms:
            r += 1
    return r


def score_calculation(inverted_index, inverted_index_docID_doclength,
                      query_term_dictionary, query_term_list,
                      query_ID_relevance_documents, query_ID_number_of_relevant_documents,
                      query_term, Checker_Score, counter2):
    bm25_score_final = {}

    average_document_length = sum(inverted_index_docID_doclength.values()) / len(inverted_index_docID_doclength.keys())

    terms_in_query = query_term.split()

    if str(counter2) in query_ID_relevance_documents.keys():
        for term in terms_in_query:
            if term in inverted_index:
                r = compute_new_score_r(term, counter2, query_ID_relevance_documents)
                query_frequency = terms_in_query.count(term)
                for document in inverted_index[term]:
                    if document[0] not in bm25_score_final.keys():
                        bm25_score_final[document[0]] = BM25_calc(document[1], len(inverted_index[term]),
                                                                  (inverted_index_docID_doclength[document[0]] /
                                                                   average_document_length), Checker_Score, r,
                                                                  query_frequency,
                                                                  inverted_index_docID_doclength)
                    else:
                        bm25_score_final[document[0]] += BM25_calc(document[1], len(inverted_index[term]),
                                                                   (inverted_index_docID_doclength[document[0]] /
                                                                    average_document_length), Checker_Score, r,
                                                                   query_frequency,
                                                                   inverted_index_docID_doclength)

    return bm25_score_final


def write_to_files(top_5_documents, top_5_dictionary_for_pseudo_relevance):
    top_5_document_list = open('Task1_BM25/BM25_Top5_Relevant_Documents.txt', 'w')
    for document in top_5_documents:
        for item in document:
            top_5_document_list.write(item + "\n")
    top_5_document_list.close()

    writer1 = open('Task1_BM25/BM25_Top5_Relevant_Query_Pages.txt', 'w')
    writer1.write(str(top_5_dictionary_for_pseudo_relevance))
    writer1.close()

    writer2 = open('Task1_BM25/Encoded_BM25_Top5_Relevant_Query_Pages.txt', 'wb')
    pickle.dump(top_5_dictionary_for_pseudo_relevance, writer2)
    writer2.close()


def PseudoRelevance(top_5_dictionary_for_pseudo_relevance):
    top_5_documents = list(top_5_dictionary_for_pseudo_relevance.values())
    write_to_files(top_5_documents, top_5_dictionary_for_pseudo_relevance)


def write_BM25_score_to_file(inverted_index, inverted_index_docID_doclength,
                             query_term_dictionary, query_term_list,
                             query_ID_relevance_documents, query_ID_number_of_relevant_documents):
    BM25Folder = 'Task2_BM25/'
    if not os.path.exists(BM25Folder):
        os.makedirs(BM25Folder)

    top_5_dictionary_for_pseudo_relevance = {}

    writer = open('Task2_BM25/BM25_Top_100_Relevance.txt', 'w')

    writer.write('Cleaned Queries Ranked (Top 100)' + '\n')
    writer.write('query_id Q0 document_id rank BM25_Score system_title' + "\n\n")

    counter2 = 1
    for query_term in query_term_dictionary.values():
        counter = 1
        rank = 1
        bm25_final_score_dictionary_check2 = {}
        if str(counter2) in query_ID_relevance_documents.keys():
            try:
                Checker_Score = query_ID_number_of_relevant_documents[str(counter2)]
            except ValueError:
                Checker_Score = 0
        BM25_score = score_calculation(inverted_index, inverted_index_docID_doclength,
                                       query_term_dictionary, query_term_list,
                                       query_ID_relevance_documents, query_ID_number_of_relevant_documents,
                                       query_term, Checker_Score, counter2)

        bm25_final_score_dictionary_check1 = collections.OrderedDict(
            sorted(BM25_score.items(), key=lambda x: x[1], reverse=True))

        writer.write('\n For Query: %s \n\n' % query_term)
        for query_id in bm25_final_score_dictionary_check1:
            if rank <= 100:
                writer.write(
                    '%d Q0 %s %d %s BestMatch25_Model\n' % (counter2, query_id, rank,
                                                            bm25_final_score_dictionary_check1[query_id]))

            if rank <= 5:
                if query_term not in top_5_dictionary_for_pseudo_relevance.keys():
                    top_5_dictionary_for_pseudo_relevance[query_term] = [query_id]
                else:
                    top_5_dictionary_for_pseudo_relevance[query_term].append(query_id)
            rank += 1

        BM25SubFolder = r'Task1_BM25/Encoded_BM25_Relevance_Top100_perQuery/'
        if not os.path.exists(BM25SubFolder):
            os.makedirs(BM25SubFolder)

        writer2 = open(BM25SubFolder + 'Encoded_Top100_BM25_query' + '%d' % counter2 + '.txt', 'wb')
        pickle.dump(bm25_final_score_dictionary_check1, writer2)
        writer2.close()

        BM25NewSubFolder = r'Task1_BM25/Encoded_BM25_Relevance_Top5_perQuery/'
        if not os.path.exists(BM25NewSubFolder):
            os.makedirs(BM25NewSubFolder)

        writer3 = open(BM25NewSubFolder + 'Encoded_Top5_BM25_Relevance_query' + '%d' % counter2 + '.txt', 'wb')
        for query_id in bm25_final_score_dictionary_check1:
            if counter <= 5:
                bm25_final_score_dictionary_check2[query_id] = bm25_final_score_dictionary_check1[query_id]
            counter += 1
        pickle.dump(bm25_final_score_dictionary_check2, writer3)
        writer3.close()

        counter2 += 1
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
