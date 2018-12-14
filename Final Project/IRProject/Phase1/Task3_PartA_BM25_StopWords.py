import pickle
import math
import collections
import os


# Global variables
final_dictionary = {}
documents_top_5 = {}





with open("./Task3_Data_Stopped/Encoded-Stopped_Inverted_List.txt", 'rb') as f:
    dictionary = pickle.loads(f.read())


with open("./Task3_Data_Stopped/Encoded-Stopped_DocumentID_DocLen.txt", 'rb') as f:
    docID_documentLen = pickle.loads(f.read())



with open("./Task3_Data_Stopped/Encoded-Cleaned_Queries_Stopped.txt", 'rb') as f:
    query_term_dictionary = pickle.loads(f.read())

query_list = list(query_term_dictionary.values())


average_document_length = sum(docID_documentLen.values()) / len(
    docID_documentLen.keys())


def best_match_25(f, n, L, R, r, q):
    k1 = 1.2
    k2 = 100
    b = 0.75
    N = len(docID_documentLen.keys())
    K = k1 * ((b * L) + (1 - b))
    term1 = (k2 + 1) * q / (k2 + q)
    term2 = (k1 + 1) * f / (K + f)
    term3 = (r + 0.5) * (N - n - R + r + 0.5)
    term4 = (n - r + 0.5) * (R - r + 0.5)
    score = term1 * term2 * math.log(term3 / term4)

    return score


def calculate_score_for_best_match(q):
    final_dictionary = {}
    terms = q.split()
    for term in terms:
        if term in dictionary:
            qf = terms.count(term)
            for doc in dictionary[term]:
                if doc[0] not in final_dictionary.keys():
                    final_dictionary[doc[0]] = best_match_25(doc[1], len(dictionary[term]),
                                               (docID_documentLen[doc[0]] / average_document_length), 0, 0, qf)
                else:
                    final_dictionary[doc[0]] += best_match_25(doc[1], len(dictionary[term]),
                                                (docID_documentLen[doc[0]] / average_document_length), 0, 0, qf)

    return final_dictionary


def BM25_stop_words():
    i = 1
    writer2 = open('Stopped_BM25_NoRelevance_Top100_Pages.txt', 'w')
    for query in query_term_dictionary.values():
        rank = 1



        bm25_score = calculate_score_for_best_match(query)
        ordered_dict_new = collections.OrderedDict(sorted(bm25_score.items(), key=lambda s: s[1], reverse=True))




        writer2.write('\nFor query : %s\n\n' % query)
        for quid in ordered_dict_new:
            if rank < 100:
                writer2.write('%d Q0 %s %d %s BM25_model_StopNoStem\n' % (i, quid, rank, ordered_dict_new[quid]))
            if rank <= 5:
                if query not in documents_top_5.keys():
                    documents_top_5[query] = [quid]
                else:
                    documents_top_5[query].append(quid)
            rank += 1
        newpath = r'./Task3_Data_Stopped/Encoded-Stopped_BM25-NoRelevance-Top100Docs-perQuery/'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        writer = open(
            newpath + 'Encoded-Top100Docs-Stopped_BM25-NoRelevance' + '_%d' % i + '.txt', 'wb')
        pickle.dump(ordered_dict_new, writer)
        writer.close()
        i += 1
        write_to_file()
    writer2.close()


def write_to_file():
    top_5_docs = list(documents_top_5.values())
    list_output = open('Stopped_BM25_NoRelevance_Top5_Docs.txt', 'w')
    for doc in top_5_docs:
        for i in doc:
            list_output.write(i + "\n")
    list_output.close()



    writer4 = open('Stopped_BM25_NoRelevance_Top5_Query_Pages.txt', 'w')

    writer4.write(str(documents_top_5))
    writer4.close()


    encoded_output = open('./Task3_Data_Stopped/Encoded-Stopped_BM25_NoRelevance_Top5_Query_Pages.txt', 'wb')
    pickle.dump(documents_top_5, encoded_output)



    encoded_output.close()


def main():
    BM25_stop_words()

if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
