import pickle
import collections
import os



# Global Variables

dictionary_for_final_score = {}


with open("./Task3_Data_Stopped/Encoded-Stopped_Inverted_List.txt", 'rb') as reader1:
    inverted_index = pickle.loads(reader1.read())

with open("./Task3_Data_Stopped/Encoded-Stopped_DocumentID_DocLen.txt", 'rb') as reader2:
    document_ID_document_length = pickle.loads(reader2.read())

length_of_corpus = sum(document_ID_document_length.values())

with open("./Task3_Data_Stopped/Encoded-Cleaned_Queries_Stopped.txt", 'rb') as reader3:
    query_term_dictionary = pickle.loads(reader3.read())


list_of_query_terms = list(query_term_dictionary.values())


def ql_score_calculator(term_frequency, document_length, r, corpus_length):
    a = (1 - r) * (term_frequency / document_length)
    b = r * (term_frequency / corpus_length)
    cal_score = a + b

    return cal_score


def calc_score(q):
    dictionary_for_final_score = {}
    terms = q.split()
    for term in terms:
        if term in inverted_index:
            for doc in inverted_index[term]:
                if doc[0] not in dictionary_for_final_score.keys():
                    dictionary_for_final_score[doc[0]] = ql_score_calculator(doc[1], document_ID_document_length[doc[0]], 0.35, length_of_corpus)
                else:
                    dictionary_for_final_score[doc[0]] += ql_score_calculator(doc[1], document_ID_document_length[doc[0]], 0.35, length_of_corpus)

    return dictionary_for_final_score


def JMSmoothingQL_stopwords():
    i = 1
    writer3 = open('Stopped_QLM_Top100_Pages.txt', 'w')
    for query in list_of_query_terms:
        rank = 1

        ql_score = calc_score(query)
        final_score1 = collections.OrderedDict(sorted(ql_score.items(), key=lambda s: s[1], reverse=True))
        writer3.write('\nFor query   : %s\n\n' % query)
        for quid in final_score1:
            if rank <= 100:
                writer3.write('%d Q0 %s %d %s Query_Likelihood_Model_StopNoStem\n' % (
                    i, quid, rank, final_score1[quid]))

            rank += 1
        file_write_path = r'./Task3_Data_Stopped/Encoded-Stopped_QLM-Top100Docs-perQuery/'
        if not os.path.exists(file_write_path):
            os.makedirs(file_write_path)
        writer2 = open(
            file_write_path + 'Encoded-Top100Docs-Stopped_QLM' + '_%d' % i + '.txt', 'wb')
        pickle.dump(final_score1, writer2)
        writer2.close()
        i += 1
    writer3.close()


def main():
    JMSmoothingQL_stopwords()

if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
