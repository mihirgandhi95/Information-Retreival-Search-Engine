import pickle
import collections
import os
import math

doc_score_folder = './Task1_JMSmoothedQL/'
if not os.path.exists(doc_score_folder):
    os.makedirs(doc_score_folder)

with open("./Task1_Data/encoded_inverted_index.txt", 'rb') as f:
    inverted_index = pickle.loads(f.read())

with open("./Task1_Data/encoded_inverted_index_docs.txt", 'rb') as f:
    docs_ID_len = pickle.loads(f.read())


with open("./Task1_Data/encoded_clean_queries.txt", 'rb') as f:
    query_dict = pickle.loads(f.read())

query_list = list(query_dict.values())  # Contains all the queries required

# This represents a dictionary containing the document IDs with their corresponding JM Smoothed QL scores
final_score = {}

# value for |C|
modC = sum(docs_ID_len.values())


# This function calculating the JM smoothed document score for each document
def JMSmoothing(tf, modD, lambda_value, modC, qf):
    term1 = (1 - lambda_value) * (tf / modD)
    term2 = lambda_value * (qf / modC)
    value = term1 + term2

    return math.log(value)


# This function calculates the document score for each document
def doc_score(q):
    lambda_value = 0.35
    final_score = {}
    terms = q.split()
    for term in terms:
        if term in inverted_index:
            qf=0
            for doc in inverted_index[term]:
                qf = qf + doc[1]
            for doc in inverted_index[term]:
                if doc[0] not in final_score.keys():
                    final_score[doc[0]] = JMSmoothing(doc[1], docs_ID_len[doc[0]], lambda_value, modC, qf)
                else:
                    final_score[doc[0]] += JMSmoothing(doc[1], docs_ID_len[doc[0]], lambda_value, modC, qf)

    return final_score


def task1_JMSmoothing():
    count = 1
    f = open('./Task1_JMSmoothedQL/JMSmoothing_top100_docs.txt', 'w')

    f.write('Top 100:' + "\n")
    f.write('Format: query_id Q0 doc_id rank JMSmoothedQL-score system_name' + "\n\n")

    for query in query_list:
        # Rank of the document
        rank = 1
        print("JM Smoothing score for query: " + query)
        ql_score = doc_score(query)
        score = collections.OrderedDict(sorted(ql_score.items(), key=lambda s: s[1], reverse=True))
        f.write('\nQuery : %s\n' % query)
        for query_id in score:
            if rank <= 100:
                f.write('%d Q0 %s %d %s JMSmoothed_Query_Likelihood\n' % (count, query_id, rank, score[query_id]))
            rank += 1
        newpath = r'./Task1_JMSmoothedQL/encoded_JMSmoothing_top100_docs_perQuery/'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        output = open(
            newpath + 'Encoded_Top100Docs-QLM' + '_%d' % count + '.txt', 'wb')
        pickle.dump(score, output)
        output.close()
        count = count + 1
    f.close()

    print("\nScored documents using JM Smoothing Query Likelihood Model")


def main():
    task1_JMSmoothing()

if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
