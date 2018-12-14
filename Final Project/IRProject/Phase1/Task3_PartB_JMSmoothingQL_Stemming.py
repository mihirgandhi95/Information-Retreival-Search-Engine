import pickle
import collections

query_dict = {}
stemmed_queries = []
scores = {}
with open("./Task3_Data_Stemmed/Encoded-Stemmed_Inverted_List.txt", 'rb') as f:
    inverted_index = pickle.loads(f.read())

with open("./Task3_Data_Stemmed/Encoded-Stemmed_DocumentID_DocLen.txt", 'rb') as f:
    docID_documentLen = pickle.loads(f.read())

with open('/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/cacm.query.txt', 'r') as f:
    l = f.readlines()
l = [x.strip() for x in l]
stemmed_queries.extend(l)

corpus_len = sum(docID_documentLen.values())


def get_score(q):
    final_score = {}
    terms = q.split()
    for term in terms:
        if term in inverted_index:
            for doc in inverted_index[term]:
                if doc[0] not in final_score.keys():
                    final_score[doc[0]] = scoring(doc[1], docID_documentLen[doc[0]], 0.35, corpus_len)
                else:
                    final_score[doc[0]] += scoring(doc[1], docID_documentLen[doc[0]], 0.35, corpus_len)

    return final_score


def scoring(tf, D, lamb, C):
    term1 = (1 - lamb) * (tf / D)
    term2 = lamb * (tf / C)
    return term1 + term2


def JMSmoothing_Stemming():
    i = 1
    f1 = open('Stemmed_QLM_Top100_Pages.txt', 'w')
    for query in stemmed_queries:
        rank = 1
        ql_score = get_score(query)
        final_score1 = collections.OrderedDict(sorted(ql_score.items(), key=lambda s: s[1], reverse=True))
        f1.write('\nFor query : %s\n\n' % query)
        for id in final_score1:
            if rank <= 100:
                f1.write('%d Q0 %s %d %s QueryLikelihoodModelStemNoStop\n' % (
                    i, id, rank, final_score1[id]))
            rank += 1
        i += 1
    f.close()


def main():
    JMSmoothing_Stemming()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
