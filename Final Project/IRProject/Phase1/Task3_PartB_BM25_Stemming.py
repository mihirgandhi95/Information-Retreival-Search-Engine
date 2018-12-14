import pickle
import math
import collections

final_score = {}
stemmed_queries = []

with open("./Task3_Data_Stemmed/Encoded-Stemmed_Inverted_List.txt", 'rb') as f:
    inverted_index = pickle.loads(f.read())

with open("./Task3_Data_Stemmed/Encoded-Stemmed_DocumentID_DocLen.txt", 'rb') as f:
    docID_documentLen = pickle.loads(f.read())

with open('/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/cacm_stem.query.txt', 'r') as f:
    l = f.readlines()
l = [x.strip() for x in l]
stemmed_queries.extend(l)

avg_doc_len = sum(docID_documentLen.values()) / len(docID_documentLen.keys())


def get_score(q):
    score = {}
    terms = q.split()
    for term in terms:
        if term in inverted_index:
            for doc in inverted_index[term]:
                if doc[0] not in score.keys():
                    score[doc[0]] = bm25(doc[1], len(inverted_index[term]),
                                         (docID_documentLen[doc[0]] / avg_doc_len), 0, 0)
                else:
                    score[doc[0]] += bm25(doc[1], len(inverted_index[term]),
                                          (docID_documentLen[doc[0]] / avg_doc_len), 0, 0)

    return score


def stemmed_BM25():
    i = 1
    f = open('Stemmed_BM25_NoRelevance_Top100_Pages.txt', 'w')
    for query in stemmed_queries:
        rank = 1
        score = get_score(query)
        scoring = collections.OrderedDict(sorted(score.items(), key=lambda s: s[1], reverse=True))
        f.write('\nFor query : %s\n\n' % query)
        for id in scoring:
            if not rank >= 100:
                f.write('%d Q0 %s %d %s BM25ModelStemNoStop\n' % (i, id, rank, scoring[id]))
                rank += 1
        i += 1
    f.close()


def bm25(f, n, L, R, r):
    k1 = 1.2
    k2 = 100
    b = 0.75
    N = len(docID_documentLen.keys())  # 3204
    q = 1
    K = k1 * ((b * L) + (1 - b))
    term1 = (k2 + 1) * q / (k2 + q)
    term2 = (k1 + 1) * f / (K + f)
    term3 = (r + 0.5) * (N - n - R + r + 0.5)
    term4 = (n - r + 0.5) * (R - r + 0.5)
    score = term1 * term2 * math.log(term3 / term4)

    return score


def main():
    stemmed_BM25()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
