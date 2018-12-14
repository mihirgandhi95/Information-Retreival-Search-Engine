import pickle
import math
import collections
import os



dictionary_for_final_score = {}

with open("./Task3_Data_Stopped/Encoded-Stopped_Inverted_List.txt", 'rb') as reader1:
    inverted_index = pickle.loads(reader1.read())

with open("./Task3_Data_Stopped/Encoded-Stopped_DocumentID_DocLen.txt", 'rb') as reader2:
    document_ID_document_length = pickle.loads(reader2.read())

length_of_corpus = sum(document_ID_document_length.values())

with open("./Task3_Data_Stopped/Encoded-Cleaned_Queries_Stopped.txt", 'rb') as reader3:
    query_term_dictionary = pickle.loads(reader3.read())

query_list = list(query_term_dictionary.values())



def calc_score(q):
    dictionary_for_final_score = {}
    terms = q.split()
    for term in terms:
        if term in inverted_index:
            for doc in inverted_index[term]:
                if doc[0] not in dictionary_for_final_score.keys():
                    dictionary_for_final_score[doc[0]] = tf_idf_score_calculator(doc[1], len(inverted_index[term]), document_ID_document_length[doc[0]])
                else:
                    dictionary_for_final_score[doc[0]] += tf_idf_score_calculator(doc[1], len(inverted_index[term]), document_ID_document_length[doc[0]])

    return dictionary_for_final_score


def tf_idf_score_calculator(term_frequency, document_frequency, D):


    N = len(document_ID_document_length.keys())
    print("N is ")
    print(N)

    inverse_document_frequency = math.log(N / document_frequency + 1) + 1
    normalized_term_frequency = term_frequency / D

    print(normalized_term_frequency)
    score = normalized_term_frequency * inverse_document_frequency
    return score


def TF_IDF_stopwords():
    i = 1
    writer3 = open('Stopped_TF_IDF_Normalized_Top100_Pages.txt', 'w')
    for query in query_list:
        rank = 1
        tf_idf_score = calc_score(query)
        final_score1 = collections.OrderedDict(sorted(tf_idf_score.items(), key=lambda s: s[1], reverse=True))
        writer3.write('\nFor query : %s\n\n' % query)
        for quid in final_score1:
            if rank < 100:
                writer3.write('%d Q0 %s %d %s tf_idf_model_StopNoStem\n' % (i, quid, rank, final_score1[quid]))

                rank += 1
        file_to_write = r'./Task3_Data_Stopped/Encoded-Stopped_TF-IDF-Normalized-Top100Docs-perQuery/'
        if not os.path.exists(file_to_write):
            os.makedirs(file_to_write)
        output = open(
            file_to_write + 'Encoded-Top100Docs-Stopped_TF-IDF-Normalized' + '_%d' % i + '.txt', 'wb')
        pickle.dump(final_score1, output)
        output.close()
        i += 1
    writer3.close()



def main():
    TF_IDF_stopwords()

if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
