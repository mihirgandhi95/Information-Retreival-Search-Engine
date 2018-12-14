import pickle
import os

# This file contains evaluation for all 8 the Retrieval models. The inputs and outputs for each is different (and
# is commented stating for each of the systems). The evaluation metrics and code remains the same for all the retrieval
#  models.
# To run for each of the retrieval models, just uncomment the model you want to evaluate

query_rel_docs = {}
query_avg_precision = {}
reciprocal_rank = {}
precision_at_5 = {}
precision_at_20 = {}

# ------------------ For BM25 Evaluation Results -----------------------
#
output_path = r'./Precision Recall Tables/BM25 Evaluation Results (No relevance)/'
with open(
        "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase3/Task_Data/Encoded-QueryID_Top100Docs_BM25_NoRelevance.txt",
        'rb') as f:
    top100docs = pickle.loads(f.read())
    with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/encoded_clean_queries.txt", 'rb') as f:
        queries = pickle.loads(f.read())
with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/Encoded_Query_ID_BM25_relevance.txt",
          'rb') as f:
    rel_docs = pickle.loads(f.read())


# ------------------ For BM25 PRF Evaluation Results -----------------------

# output_path = r'./Precision Recall Tables/BM25 PRF Evaluation Results/'
# with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/Encoded_Query_ID_BM25_relevance.txt",
#           'rb') as f:
#     rel_docs = pickle.loads(f.read())
# with open("/Users/nehagundecha/PycharmProjects/IRProject/Phase3/Task_Data/Encoded-QueryID_Top100Docs_BM25_Relevance_PRF.txt",
#         'rb') as f:
#     queryID_top100Docs = pickle.loads(f.read())
# with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/encoded_clean_queries.txt", 'rb') as f:
#     queryID_query = pickle.loads(f.read())


# ------------------ For BM25 with stopping Evaluation Results -----------------------

# output_path = r'./Precision Recall Tables/BM25 Stopped Evaluation Results/'
# with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/Encoded_Query_ID_BM25_relevance.txt",
#           'rb') as f:
#     queryID_relevantDocs = pickle.loads(f.read())
# with open("/Users/nehagundecha/PycharmProjects/IRProject/Phase3/Task_Data/Encoded-QueryID_Top100Docs_Stopped_BM25_NoRelevance.txt",
#         'rb') as f:
#     queryID_top100Docs = pickle.loads(f.read())
# with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/encoded_clean_queries.txt", 'rb') as f:
#     queryID_query = pickle.loads(f.read())


# ------------------ For JMSmoothing QL Evaluation Results -----------------------

# output_path = r'./Precision Recall Tables/JMSmoothing QL Evaluation Results/'
# with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/Encoded_Query_ID_BM25_relevance.txt",
#           'rb') as f:
#     queryID_relevantDocs = pickle.loads(f.read())
# with open("/Users/nehagundecha/PycharmProjects/IRProject/Phase3/Task_Data/Encoded-QueryID_Top100Docs_QLM.txt",
#           'rb') as f:
#     queryID_top100Docs = pickle.loads(f.read())
# with open("/Users/nehagundecha/PycharmProjects/IRProject/Phase1/Task1_Data/encoded_clean_queries.txt", 'rb') as f:
#     queryID_query = pickle.loads(f.read())


# ------------------ For JMSmoothing QL with stopping Evaluation Results ----------------

# output_path = r'./Precision Recall Tables/JMSmoothing QL Stopped Evaluation Results/'
# with open("/Users/nehagundecha/PycharmProjects/IRProject/Phase1/Task1_Data/Encoded_Query_ID_BM25_relevance.txt",
#           'rb') as f:
#     queryID_relevantDocs = pickle.loads(f.read())
# with open("/Users/nehagundecha/PycharmProjects/IRProject/Phase3/Task_Data/Encoded-QueryID_Top100Docs_QLM_Stopped.txt",
#           'rb') as f:
#     queryID_top100Docs = pickle.loads(f.read())
# with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/encoded_clean_queries.txt", 'rb') as f:
#     queryID_query = pickle.loads(f.read())


# ------------------ For Lucene Evaluation Results -----------------------

# with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/Encoded_Query_ID_BM25_relevance.txt",
#           'rb') as f:
#     queryID_relevantDocs = pickle.loads(f.read())
# with open("/Users/nehagundecha/PycharmProjects/IRProject/Phase3/Task_Data/Encoded-QueryID_Top100Docs_Lucene.txt",
#           'rb') as f:
#     queryID_top100Docs = pickle.loads(f.read())
# with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/encoded_clean_queries.txt", 'rb') as f:
#     queryID_query = pickle.loads(f.read())
# output_path = r'./Precision Recall Tables/Lucene Evaluation Results/'


# ------------------ For TF-IDF Evaluation Results -----------------------

# output_path = r'./Precision Recall Tables/TF IDF Evaluation Results/'
# with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/Encoded_Query_ID_BM25_relevance.txt",
#           'rb') as f:
#     queryID_relevantDocs = pickle.loads(f.read())
# with open("/Users/nehagundecha/PycharmProjects/IRProject/Phase3/Task_Data/Encoded-QueryID_Top100Docs_tf-idf_normalized.txt",
#         'rb') as f:
#     queryID_top100Docs = pickle.loads(f.read())
# with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/encoded_clean_queries.txt", 'rb') as f:
#     queryID_query = pickle.loads(f.read())


# ------------------ For TF-IDF With stopping Evaluation Results -----------------------

# output_path = r'./Precision Recall Tables/TF IDF Stopped Evaluation Results/'
# with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/Encoded_Query_ID_BM25_relevance.txt",
#           'rb') as f:
#     queryID_relevantDocs = pickle.loads(f.read())
# with open("/Users/nehagundecha/PycharmProjects/IRProject/Phase3/Task_Data/Encoded-QueryID_Top100Docs_Stopped_tf-idf_normalized.txt",
#         'rb') as f:
#     queryID_top100Docs = pickle.loads(f.read())
# with open("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Data/encoded_clean_queries.txt", 'rb') as f:
#     queryID_query = pickle.loads(f.read())

def init():
    for key in rel_docs:
        query_rel_docs[key] = len(rel_docs[key])
    if not os.path.exists(output_path):
        os.makedirs(output_path)


def get_count_relevant(var):
    count = 0
    docs = rel_docs[str(var)]
    top_100_docs = top100docs[str(var)]
    for doc in docs:
        if doc in top_100_docs:
            count += 1

    return count


def get_docs(query):
    dict = {}
    if query in rel_docs:
        relevant_docs = rel_docs[query]
        top_100_docs = top100docs[query]
        for doc in top_100_docs:
            if not doc in relevant_docs:
                dict[doc] = "N"
            else:
                dict[doc] = "R"
    return dict


def cal_reciprocal_rank(var):
    docs = get_docs(str(var))
    list1 = list(docs.values())
    try:
        rank = list1.index("R") + 1
    except ValueError:
        rank = 0
    if not rank == 0:
        RR = 1 / rank
    else:
        RR = 0

    return RR


def evaluate_on_metrics():
    for query_id in rel_docs:
        f = open(output_path + "Precision_Recall_Table_for_" + query_id + '.txt', 'w')
        precision_values = []
        recall_values = []
        rank = 1
        precisions_list = []
        count_relevant_docs = query_rel_docs[str(rank)]
        docs = get_docs(query_id)
        if docs == {}:
            continue
        RR_val = cal_reciprocal_rank(query_id)
        f.write("Query: %s\n" % queries[query_id])
        f.write("RANK \t R/N \tPrecision \t  Recall\n\n")
        recall_precision(docs, 0, rank, precision_values, precisions_list, query_id, count_relevant_docs,
                         recall_values, f)

        avg_precision = sum(precision_values) / len(precision_values)
        avg_recall = sum(recall_values) / len(recall_values)

        f.write("\n\nAverage precision = " + str(avg_precision))
        f.write("\n\nAverage recall = " + str(avg_recall))

        reciprocal_rank[query_id] = RR_val
        f.close()

    write_to_file()


def recall_precision(docs, rel_count, rank, precision_values, precision_lists, query_id, count_relevant_docs,
                     recall_values, f):
    for rel in docs:
        if docs[rel] == "R":
            rel_count += 1
        precision = rel_count / rank
        precision_values.append(precision)
        if docs[rel] == "R":
            precision_lists.append(precision)
        if rank == 20:
            precision_at_20[int(query_id)] = precision
        if rank == 5:
            precision_at_5[int(query_id)] = precision

        recall = rel_count / count_relevant_docs
        recall_values.append(recall)

        if not rank < 10:
            rank_str = str(rank)
        else:
            rank_str = "0" + str(rank)

        write_each_value(rank_str, docs[rel], precision, recall, f)
        rank += 1

        calculate_avg_precision(precision_lists, query_id)


def calculate_avg_precision(relevant_lists, query_id):
    if not len(relevant_lists) == 0:
        sum1 = sum(relevant_lists)
        length = len(relevant_lists)
        query_avg_precision[query_id] = sum1 / length
    else:
        query_avg_precision[query_id] = 0


def write_each_value(rank, name, precision, recall, f):
    f.write(rank + "  \t  " + name + "  \t  %.3f" % precision + "  \t  %.3f" % recall + "\n")


def write_to_file():
    f1 = open(output_path + "Final Evaluation.txt", 'w')
    MAP = sum(query_avg_precision.values()) / len(query_avg_precision.keys())
    f1.write("Mean Average Precision (MAP) = %f\n" % MAP)

    MRR = sum(reciprocal_rank.values()) / len(reciprocal_rank.keys())
    f1.write("Mean Reciprocal Rank (MRR) = %f\n" % MRR)
    f1.close()

    f2 = open(output_path + "P@KValuesForAllQueries.txt", 'w')
    for query_id in rel_docs:
        if int(query_id) in precision_at_5.keys():
            f2.write("For query: %s\n\n" % queries[query_id])
            f2.write("Precision@5: %f\n" % precision_at_5[int(query_id)])
            f2.write("Precision@20: %f\n\n" % precision_at_20[int(query_id)])
    f2.close()


def main():
    init()
    evaluate_on_metrics()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
