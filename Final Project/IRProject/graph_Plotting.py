import os
import matplotlib.pyplot as plt

def read_directories_create_list(location1, location2, location3,location4,location5,location6,location7,location8):


    path = location1

    location1_list = []

    for file in os.listdir(path):
        print(file)
        location1_list.append(file)

    print(location1_list)

        # text = reader1.read()
        # text_terms = text.split("=")
        # print("+++++++++++++++++++++++++++++")
        # print(text_terms)

    Precision_final_list_BM25_1 = []
    Recall_final_list_BM25_1 = []

    for document in location1_list:
        reader1 = open('Precision Recall Tables/BM25 Evaluation Results (No relevance)/' + document, 'r')
        text = reader1.read()
        text_terms = text.split("\n")

        # print(text_terms[-3])

        precision_value = text_terms[-3]

        precision_value_terms = precision_value.split("=")
        # print(precision_value_terms[1])

        Precision_final_list_BM25_1.append(float(precision_value_terms[1].strip()))

        # print(text_terms[-1])

        recall_value = text_terms[-1]

        recall_value_terms = recall_value.split("=")
        # print(recall_value_terms[1])

        Recall_final_list_BM25_1.append(float(recall_value_terms[1].strip()))

    print(Precision_final_list_BM25_1)
    print(Recall_final_list_BM25_1)
    print(len(Precision_final_list_BM25_1))
    print(len(Recall_final_list_BM25_1))


    Y = Precision_final_list_BM25_1
    X = Recall_final_list_BM25_1




    #################################################################
    path = location2

    location2_list = []

    for file in os.listdir(path):
        print(file)
        location2_list.append(file)

    print(location2_list)

    # text = reader1.read()
    # text_terms = text.split("=")
    # print("+++++++++++++++++++++++++++++")
    # print(text_terms)

    Precision_final_list_BM25_2 = []
    Recall_final_list_BM25_2 = []

    for document in location2_list:
        reader1 = open('Precision Recall Tables/BM25 PRF Evaluation Results/' + document, 'r')
        text = reader1.read()
        text_terms = text.split("\n")

        # print(text_terms[-3])

        precision_value = text_terms[-3]

        precision_value_terms = precision_value.split("=")
        # print(precision_value_terms[1])

        Precision_final_list_BM25_2.append(float(precision_value_terms[1].strip()))

        # print(text_terms[-1])

        recall_value = text_terms[-1]

        recall_value_terms = recall_value.split("=")
        # print(recall_value_terms[1])

        Recall_final_list_BM25_2.append(float(recall_value_terms[1].strip()))

    print(Precision_final_list_BM25_2)
    print(Recall_final_list_BM25_2)
    print(len(Precision_final_list_BM25_2))
    print(len(Recall_final_list_BM25_2))

    Y2 = Precision_final_list_BM25_2
    X2 = Recall_final_list_BM25_2




    #################################################################
    path = location3

    location3_list = []

    for file in os.listdir(path):
        print(file)
        location3_list.append(file)

    print(location3_list)

    # text = reader1.read()
    # text_terms = text.split("=")
    # print("+++++++++++++++++++++++++++++")
    # print(text_terms)

    Precision_final_list_BM25_3 = []
    Recall_final_list_BM25_3 = []

    for document in location3_list:
        reader1 = open('Precision Recall Tables/BM25 Stopped Evaluation Results/' + document, 'r')
        text = reader1.read()
        text_terms = text.split("\n")

        # print(text_terms[-3])

        precision_value = text_terms[-3]

        precision_value_terms = precision_value.split("=")
        # print(precision_value_terms[1])

        Precision_final_list_BM25_3.append(float(precision_value_terms[1].strip()))

        # print(text_terms[-1])

        recall_value = text_terms[-1]

        recall_value_terms = recall_value.split("=")
        # print(recall_value_terms[1])

        Recall_final_list_BM25_3.append(float(recall_value_terms[1].strip()))

    print(Precision_final_list_BM25_3)
    print(Recall_final_list_BM25_3)
    print(len(Precision_final_list_BM25_3))
    print(len(Recall_final_list_BM25_3))

    Y3 = Precision_final_list_BM25_3
    X3 = Recall_final_list_BM25_3


    #################################################################
    path = location4

    location4_list = []

    for file in os.listdir(path):
        print(file)
        location4_list.append(file)

    print(location4_list)

    # text = reader1.read()
    # text_terms = text.split("=")
    # print("+++++++++++++++++++++++++++++")
    # print(text_terms)

    Precision_final_list_BM25_4 = []
    Recall_final_list_BM25_4 = []

    for document in location4_list:
        reader1 = open('Precision Recall Tables/JMSmoothing QL Evaluation Results/' + document, 'r')
        text = reader1.read()
        text_terms = text.split("\n")

        # print(text_terms[-3])

        precision_value = text_terms[-3]

        precision_value_terms = precision_value.split("=")
        # print(precision_value_terms[1])

        Precision_final_list_BM25_4.append(float(precision_value_terms[1].strip()))

        # print(text_terms[-1])

        recall_value = text_terms[-1]

        recall_value_terms = recall_value.split("=")
        # print(recall_value_terms[1])

        Recall_final_list_BM25_4.append(float(recall_value_terms[1].strip()))

    print(Precision_final_list_BM25_4)
    print(Recall_final_list_BM25_4)
    print(len(Precision_final_list_BM25_4))
    print(len(Recall_final_list_BM25_4))

    Y4 = Precision_final_list_BM25_4
    X4 = Recall_final_list_BM25_4

    #################################################################
    path = location5

    location5_list = []

    for file in os.listdir(path):
        print(file)
        location5_list.append(file)

    print(location5_list)

    # text = reader1.read()
    # text_terms = text.split("=")
    # print("+++++++++++++++++++++++++++++")
    # print(text_terms)

    Precision_final_list_BM25_5 = []
    Recall_final_list_BM25_5 = []

    for document in location4_list:
        reader1 = open('Precision Recall Tables/JMSmoothing QL Stopped Evaluation Results/' + document, 'r')
        text = reader1.read()
        text_terms = text.split("\n")

        # print(text_terms[-3])

        precision_value = text_terms[-3]

        precision_value_terms = precision_value.split("=")
        # print(precision_value_terms[1])

        Precision_final_list_BM25_5.append(float(precision_value_terms[1].strip()))

        # print(text_terms[-1])

        recall_value = text_terms[-1]

        recall_value_terms = recall_value.split("=")
        # print(recall_value_terms[1])

        Recall_final_list_BM25_5.append(float(recall_value_terms[1].strip()))

    print(Precision_final_list_BM25_5)
    print(Recall_final_list_BM25_5)
    print(len(Precision_final_list_BM25_5))
    print(len(Recall_final_list_BM25_5))

    Y5 = Precision_final_list_BM25_5
    X5 = Recall_final_list_BM25_5

    #################################################################
    path = location6

    location6_list = []

    for file in os.listdir(path):
        print(file)
        location6_list.append(file)

    print(location6_list)

    # text = reader1.read()
    # text_terms = text.split("=")
    # print("+++++++++++++++++++++++++++++")
    # print(text_terms)

    Precision_final_list_BM25_6 = []
    Recall_final_list_BM25_6 = []

    for document in location4_list:
        reader1 = open('Precision Recall Tables/Lucene Evaluation Results/' + document, 'r')
        text = reader1.read()
        text_terms = text.split("\n")

        # print(text_terms[-3])

        precision_value = text_terms[-3]

        precision_value_terms = precision_value.split("=")
        # print(precision_value_terms[1])

        Precision_final_list_BM25_6.append(float(precision_value_terms[1].strip()))

        # print(text_terms[-1])

        recall_value = text_terms[-1]

        recall_value_terms = recall_value.split("=")
        # print(recall_value_terms[1])

        Recall_final_list_BM25_6.append(float(recall_value_terms[1].strip()))

    print(Precision_final_list_BM25_6)
    print(Recall_final_list_BM25_6)
    print(len(Precision_final_list_BM25_6))
    print(len(Recall_final_list_BM25_6))

    Y6 = Precision_final_list_BM25_6
    X6 = Recall_final_list_BM25_6

    #################################################################
    path = location7

    location7_list = []

    for file in os.listdir(path):
        print(file)
        location7_list.append(file)

    print(location7_list)

    # text = reader1.read()
    # text_terms = text.split("=")
    # print("+++++++++++++++++++++++++++++")
    # print(text_terms)

    Precision_final_list_BM25_7 = []
    Recall_final_list_BM25_7 = []

    for document in location4_list:
        reader1 = open('Precision Recall Tables/Lucene Evaluation Results/' + document, 'r')
        text = reader1.read()
        text_terms = text.split("\n")

        # print(text_terms[-3])

        precision_value = text_terms[-3]

        precision_value_terms = precision_value.split("=")
        # print(precision_value_terms[1])

        Precision_final_list_BM25_7.append(float(precision_value_terms[1].strip()))

        # print(text_terms[-1])

        recall_value = text_terms[-1]

        recall_value_terms = recall_value.split("=")
        # print(recall_value_terms[1])

        Recall_final_list_BM25_7.append(float(recall_value_terms[1].strip()))

    print(Precision_final_list_BM25_7)
    print(Recall_final_list_BM25_7)
    print(len(Precision_final_list_BM25_7))
    print(len(Recall_final_list_BM25_7))

    Y7 = Precision_final_list_BM25_7
    X7 = Recall_final_list_BM25_7

    #################################################################
    path = location8

    location8_list = []

    for file in os.listdir(path):
        print(file)
        location8_list.append(file)

    print(location8_list)

    # text = reader1.read()
    # text_terms = text.split("=")
    # print("+++++++++++++++++++++++++++++")
    # print(text_terms)

    Precision_final_list_BM25_8 = []
    Recall_final_list_BM25_8 = []

    for document in location4_list:
        reader1 = open('Precision Recall Tables/Lucene Evaluation Results/' + document, 'r')
        text = reader1.read()
        text_terms = text.split("\n")

        # print(text_terms[-3])

        precision_value = text_terms[-3]

        precision_value_terms = precision_value.split("=")
        # print(precision_value_terms[1])

        Precision_final_list_BM25_8.append(float(precision_value_terms[1].strip()))

        # print(text_terms[-1])

        recall_value = text_terms[-1]

        recall_value_terms = recall_value.split("=")
        # print(recall_value_terms[1])

        Recall_final_list_BM25_8.append(float(recall_value_terms[1].strip()))

    print(Precision_final_list_BM25_8)
    print(Recall_final_list_BM25_8)
    print(len(Precision_final_list_BM25_8))
    print(len(Recall_final_list_BM25_8))

    Y8 = Precision_final_list_BM25_8
    X8 = Recall_final_list_BM25_8

    # plt.plot(X, Y, color='red', linestyle='dashed', marker='o')
    # # plt.scatter(X,Y)
    #
    # plt.plot(X2, Y2, color='blue', linestyle='dashed', marker='o')
    #
    #
    # plt.plot(X3, Y3, color='green', linestyle='dashed', marker='o')
    #
    # plt.plot(X4, Y4, color='purple', linestyle='dashed', marker='o')


    plt.plot(X,  Y, marker='o', label = "BM25 Evaluation Results (No relevance)")
    plt.plot(X2, Y2, marker='o', label = "BM25 PRF Evaluation Results")
    plt.plot(X3, Y3, marker='o', label = "BM25 Stopped Evaluation Results")
    plt.plot(X4, Y4, marker='o', label = "JMSmoothing QL Evaluation Results")
    plt.plot(X5, Y5, marker='o', label = "JMSmoothing QL Stopped Evaluation Results")
    plt.plot(X6, Y6, marker='o', label = "Lucene Evaluation Results")
    plt.plot(X7, Y7, marker='o', label = "TF IDF Evaluation Results")
    plt.plot(X8, Y8, marker='o', label= "TF IDF Stopped Evaluation Results")

    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision Recall Curve')
    # plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([0, 1, 0, 1])
    # plt.grid(True)
    # plt.show()
    plt.legend()
    plt.show()

    #
    #     if term in text_terms:
    #         r += 1
    # return r

# Declaring the main function in Python
def main():


    # hello = "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase3/Task_Data/Precision Recall Tables"
    location1 = "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase3/Task_Data/Precision Recall Tables/BM25 Evaluation Results (No relevance)/"
    location2 = "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase3/Task_Data/Precision Recall Tables/BM25 PRF Evaluation Results"
    location3 = "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase3/Task_Data/Precision Recall Tables/BM25 Stopped Evaluation Results"
    location4 = "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase3/Task_Data/Precision Recall Tables/JMSmoothing QL Evaluation Results"
    location5 = "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase3/Task_Data/Precision Recall Tables/JMSmoothing QL Stopped Evaluation Results"
    location6 = "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase3/Task_Data/Precision Recall Tables/Lucene Evaluation Results"
    location7 = "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase3/Task_Data/Precision Recall Tables/TF IDF Evaluation Results"
    location8 = "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase3/Task_Data/Precision Recall Tables/TF IDF Stopped Evaluation Results"
    read_directories_create_list(location1, location2, location3, location4, location5, location6, location7, location8)


# Checking if the program is being run by itself or imported from another module
if __name__ == '__main__':
    # print ('This program is being run by itself');
    main()
else:
    print('the program is imported from another module')