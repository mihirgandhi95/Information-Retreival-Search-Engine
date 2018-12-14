import pickle
import math
import collections

stemmed_queries = []
scores = {}
with open("./Task3_Data_Stemmed/Encoded-Stemmed_Inverted_List.txt", 'rb') as f:
    inverted_index = pickle.loads(f.read())

with open("./Task3_Data_Stemmed/Encoded-Stemmed_DocumentID_DocLen.txt", 'rb') as f:
    docID_documentLen = pickle.loads(f.read())
with open('/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/cacm_stem.query.txt', 'r') as f:
    l = f.readlines()
l = [x.strip() for x in l]
stemmed_queries.extend(l)


def TF_IDF(tf, df, D):
    N = len(docID_documentLen.keys())
    idf = math.log(N / df + 1) + 1
    normalized_tf = tf / D
    score = normalized_tf * idf
    return score


def score(q):
    final_score = {}
    terms = q.split()
    for term in terms:
        if term in inverted_index:
            for doc in inverted_index[term]:
                if doc[0] in final_score.keys():
                    final_score[doc[0]] += TF_IDF(doc[1], len(inverted_index[term]), docID_documentLen[doc[0]])
                else:
                    final_score[doc[0]] = TF_IDF(doc[1], len(inverted_index[term]), docID_documentLen[doc[0]])

    return final_score


def TF_IDF_stemming():
    i = 1
    f = open('Stemmed_TF_IDF_Normalized_Top100_Pages.txt', 'w')
    for query in stemmed_queries:
        rank = 1
        tf_idf_score = score(query)
        s = collections.OrderedDict(sorted(tf_idf_score.items(), key=lambda s: s[1], reverse=True))
        f.write('\nFor query : %s\n\n' % query)
        for key in s:
            if not rank >= 100:
                f.write('%d Q0 %s %d %s tfidf_StemNoStop\n' % (
                    i, key, rank, s[key]))
                rank += 1
        i += 1
    f.close()


def main():
    TF_IDF_stemming()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
