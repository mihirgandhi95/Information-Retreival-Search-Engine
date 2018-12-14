import os
import nltk
from collections import OrderedDict
from more_itertools import locate
import json



# GLOBAL VARIABLES
# dictionary declared for inverted index
inverted_index = {}

# dictionary for storing
inverted_index_with_term_positions = {}

# dictionary for term frequency sorted index
sorted_index_with_term_frequency  = {}

# dictionary for document frequency sorted index
sorted_index_with_document_frequency = {}

# array to store the terms in the document
terms_per_document = []


def read_folder(location):
    files_to_navigate = []
    for directory in os.walk(location):
        for files in directory:
            files_to_navigate = files

    return files_to_navigate




# method to create inverted index
def Create_Index(location, n_gram, dgaps):

    files_to_navigate = read_folder(location)

    for filtered_file in files_to_navigate:

        # open the file in the directory
        with(open(location + '/' + filtered_file, 'r+')) as f:

            # removing .txt from file name
            filtered_file = filtered_file[:-4]

            # testing comment
            print('--------------------------')
            print(filtered_file)
            print('--------------------------')
            # time.sleep(2)


            # creating terms depending on the value of n_gram
            if n_gram == '1':
                filtered_file_terms = f.read().split()
            elif n_gram == '2':
                filtered_file_terms = f.read().split()
                filtered_file_terms = list(nltk.bigrams(filtered_file_terms))
            elif n_gram == '3':
                filtered_file_terms = f.read().split()
                filtered_file_terms = list(nltk.trigrams(filtered_file_terms))
            else:
                filtered_file_terms = []
                break

            calculate_inverted_index(n_gram,dgaps,filtered_file_terms,filtered_file)

            for term in filtered_file_terms:

                # testing comment
                # print (":::::::::::::::>> ",term)
                # time.sleep(2)

                length = 0
                if term not in inverted_index:
                    inverted_index[term] = [[filtered_file, 1]]
                else:

                    # testing comment
                    # print ("hey the "+term+" is in index!")
                    for i in range(len(inverted_index[term])):
                        if inverted_index[term][i][0] == filtered_file:
                            inverted_index[term][i][1] += 1

                        else:
                            length = length + 1
                    if length == len(inverted_index[term]):
                        inverted_index[term].append([filtered_file, 1])

        terms_per_document.append([filtered_file, len(set(filtered_file_terms))])

        # testing the value of invereted index by writing to a file
        with open('test' + str(n_gram) + 'inverted_index.txt', 'w') as f:
            f.write(str(inverted_index))

        fj = open(str(n_gram) + 'invertedindexJSON.json', 'w')
        docfreqnewjson = json.dumps(inverted_index)
        fj.write(docfreqnewjson)

        # testing comment
        # print(inverted_index)

    sort_inverted_index(inverted_index_with_term_positions, terms_per_document, sorted_index_with_document_frequency,
                        sorted_index_with_term_frequency, inverted_index, n_gram)

def calculate_inverted_index(n_gram,dgaps,filtered_file_terms,filtered_file):
    # check the value of n_gram and if the value is 1, then check if dgaps is enabled
    # dgap calculation is only to be performed for n_gram value = 1
    if n_gram == '1':
        for term in filtered_file_terms:
            count = 0
            # check for dgaps enabled or not
            if dgaps:
                term_positions = dgaps_encode(term, list(locate(filtered_file_terms, lambda x: x == term)))
            else:
                term_positions = list(locate(filtered_file_terms, lambda x: x == term))

            if term not in inverted_index_with_term_positions:
                inverted_index_with_term_positions[term] = [[filtered_file, len(list(locate(filtered_file_terms, lambda x:
                                                             x == term))),
                                                             list(locate(filtered_file_terms, lambda x:
                                                             x == term))]]
            else:
                for i in range(len(inverted_index_with_term_positions[term])):
                    if inverted_index_with_term_positions[term][i][0] == filtered_file:
                        break
                    else:
                        count = count + 1
                if count == len(inverted_index_with_term_positions[term]):
                    inverted_index_with_term_positions[term].append([filtered_file, len(term_positions), term_positions])





def sort_inverted_index(inverted_index_with_term_positions, terms_per_document, sorted_index_with_document_frequency,
                        sorted_index_with_term_frequency, inverted_index, n_gram):
    for key in inverted_index:
        term_frequency = 0
        for i in range(len(inverted_index[key])):
            term_frequency = term_frequency + inverted_index[key][i][1]
        sorted_index_with_term_frequency[key] = term_frequency

    sorted_index_with_term_frequency = OrderedDict(sorted(sorted_index_with_term_frequency.items(),
                                                      key=lambda key_value: key_value[1], reverse=True))
    # print(sorted_index_with_term_frequency)

    for key in sorted(inverted_index):
        document_list = []
        document_count = 0

        for i in range(len(inverted_index[key])):
            document_list.append(inverted_index[key][i][0])
            document_count = document_count + 1
            sorted_index_with_document_frequency[key] = [document_list, document_count]

    # testing comment
    # print('Document Frequency Sorted Index')
    # print(sorted_index_with_document_frequency)

    write_tf_table(inverted_index_with_term_positions,terms_per_document,sorted_index_with_document_frequency,
                      sorted_index_with_term_frequency, inverted_index,n_gram)
    write_df_table(inverted_index_with_term_positions, terms_per_document, sorted_index_with_document_frequency,
                   sorted_index_with_term_frequency, inverted_index, n_gram)
    write_df_table_json(inverted_index_with_term_positions, terms_per_document, sorted_index_with_document_frequency,
                   sorted_index_with_term_frequency, inverted_index, n_gram)

    write_term_count(inverted_index_with_term_positions,terms_per_document, sorted_index_with_document_frequency,
                         sorted_index_with_term_frequency, inverted_index,n_gram)

    write_position_inverted_index(inverted_index_with_term_positions, terms_per_document, sorted_index_with_document_frequency,
                     sorted_index_with_term_frequency, inverted_index, n_gram)


def write_tf_table(inverted_index_with_term_positions, terms_per_document,
                      sorted_index_with_document_frequency,sorted_index_with_term_frequency,
                           inverted_index, n_gram):
    # testing comment
    # print('hello')

    for key in sorted_index_with_term_frequency:
        with open(str(n_gram) + '_tf_table.txt', 'a+') as f:
            f.write(str(key) + "@@~" + str(sorted_index_with_term_frequency[key]) + "\n")

def write_df_table(inverted_index_with_term_positions, terms_per_document,
                   sorted_index_with_document_frequency, sorted_index_with_term_frequency,
                   inverted_index, n_gram):
    with open(str(n_gram) + '_df_table.txt', 'w') as f:
        f.write("The format of the file is:  TERM :  DOCUMENTS  DOCUMENT_FREQUENCY \n")
        for key in sorted_index_with_document_frequency:
            f.write(str(key) + " : " + str(sorted_index_with_document_frequency[key][0]) + " @@~ " +
                    str(sorted_index_with_document_frequency[key][1]) + "\n")



def write_df_table_json(inverted_index_with_term_positions, terms_per_document,
                    sorted_index_with_document_frequency, sorted_index_with_term_frequency,
                    inverted_index, n_gram):
    # JSON file to dump data
    fj = open(str(n_gram) + '_df_tableJSON.json', 'w')

    for key in sorted_index_with_document_frequency.keys():
        if type(key) is not str:
            try:
                sorted_index_with_document_frequency[str(key)] = sorted_index_with_document_frequency[key]
            except:
                try:
                    sorted_index_with_document_frequency[repr(key)] = sorted_index_with_document_frequency[key]
                except:
                    pass
            del sorted_index_with_document_frequency[key]

    docfreqjson = json.dumps(sorted_index_with_document_frequency)
    fj.write(docfreqjson)




def write_term_count(inverted_index_with_term_positions, terms_per_document,
                         sorted_index_with_document_frequency, sorted_index_with_term_frequency, inverted_index, n_gram):

    with open(str(n_gram) + '_term_count.txt', 'w') as f:
        for term in terms_per_document:
            f.write(str(term) + '\n')

def write_position_inverted_index(inverted_index_with_term_positions, terms_per_document,
                     sorted_index_with_document_frequency, sorted_index_with_term_frequency, inverted_index,
                     n_gram):
    if n_gram == '1':
        with open(str(n_gram) + '_position_inverted_index.txt', 'w') as f:
            for key in inverted_index_with_term_positions:
                f.write(str(key) + " : " +
                        str(inverted_index_with_term_positions[key]) + "\n")
    else:
        print('cannot write because n_gram is not 1')


# Method to encode dgaps
def dgaps_encode(term, list):

    # testing comment
    # print('compare with')
    # print(list)

    newlist = []
    initial_value = 0


    for x in list:
        new_value = abs(x - initial_value)
        newlist.append(new_value)
        initial_value = x

        # testing comment
        # print(new_value)

    # testing comment
    # print(newlist)
    # print('++++++++++++++=')
    return newlist


# Declaring the main function in Python
def main():
    location = '/Users/mihirg/PycharmProjects/extracreditnew/Task1_Output_Tokens'

    n_gram = input("Enter the term you want:" +
                   "\n" + "enter 1 for unigram terms" +
                   "\n" + "enter 2 for bigram terms" +
                   "\n" + "enter 3 for trigram terms" + '\n')

    d_gaps = input("Enter 1 for using dgaps and 2 for not using dgaps"+"\n")

    # provide input value for n_gram value and d_gaps value to be used or not
    Create_Index(location, n_gram, d_gaps)


# Checking if the program is being run by itself or imported from another module
if __name__ == '__main__':
    # print ('This program is being run by itself');
    main()
else:
    print('the program is imported from another module')


