import re
import json
stop_word_list_text = []
inverted_index = {}

def loading_inverted_index_from_content(location):
    global inverted_index
    with open(location, 'r') as pos_inverted:
        for line in pos_inverted:
            item = line.split(":")
            # item[1] = item[1].strip()
            # item[0] = item[0].strip()

            inverted_index[item[0].strip()] = eval(item[1])

            # print(item)

            # if item[1] == 09:
            # # item[0] = str(item[0])
            # # if item[0] == "09":
            # regex = re.compile('[0]*')
            # if regex.match(item[1]):
            #     continue
            # else:
            # if "09" not in item[0] and "09" not in item[1]:
            # if (("09" not in item[1]) and ("01" not in item[1]) and
            #     ("02" not in item[1]) and ("04" not in item[1]) and
            #     ("03" not in item[1]) and ("05" not in item[1]) and
            #     ("06" not in item[1]) and ("09" not in item[1]) and
            #     ("07" not in item[1]) and ("08" not in item[1])):
            #     item[0] = item[0].lstrip("0").strip()
            #     inverted_index[item[0].strip()] = eval(item[1])

    with open("abcd.txt", 'w') as f:
        docfreqjson = json.dumps(inverted_index)
        f.write(docfreqjson)
        # f.write(inverted_index)
    print(inverted_index)





def stop_word_list():
    with open('common_words') as f:
        for line in f:
            stop_word_list_text.append(line.strip())
            print(stop_word_list_text)
            # print(line)

def enter_query():
    user_input = input("Do you want to enter the query term? yes/no \n")
    if user_input.lower() == "yes":
        query_content = input("enter your query\n")
    elif user_input.lower() == "no":
        return
    else:
        enter_query()
    return query_content



def remove_stop_words_from_query(query):

    choose_to_remove_stopwords = input("Do you want to remove the stop words from query? y/n \n ")

    if choose_to_remove_stopwords.lower() == 'y':
        global stop_word_list_text
        print('inside removing stopwords')

        print('query is:')
        print(query)

        newQuery = ""
        query_list = query.split(" ")

        print('query list is:')
        print(query_list)

        for item in query_list:
            print('item in query list')
            print(item)
            if item not in stop_word_list_text:
                print('item not in stop word list')
                print(item)
                newQuery = newQuery + item + " "
        print('newQuery is: ')
        print(newQuery.strip())
        return newQuery.strip()
    elif choose_to_remove_stopwords.lower() == 'n':
        return query.strip()
    else:
        remove_stop_words_from_query(query)



def remove_punctuations(query_text):
    punctuations_text = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '|', '\'',
                         '<', '"', ',', '.', '[', ']', ';', ',', '/', '.', ' (', ')', '`', '~', ' .', '&#8221',
                         '&#8220', '&#8222', '&#8482', '&#8364']


    for x in punctuations_text:
        if x in query_text:
            query_text = query_text.replace(x, " ")

    query_text = query_text.lower()
    query_text = query_text.lower().replace("\n", " ")
    query_text = re.sub(' +', ' ', query_text).strip()

    # punctuations for handling text with special ascii characters for double quotes not specific to the mac system


    query_text = re.sub(r"[^0-9A-Za-z,-\.:\\$]", " ", query_text)
    query_text = re.sub(r"(?!\d)[$,%,:.,-](?!\d)", " ", query_text, 0)

    query_text = query_text.split()
    return query_text


def find_documents_with_terms_matching(query_term):

    if query_term not in inverted_index.keys():
        return []

    list_of_documents_with_term = inverted_index[query_term]

    list_of_documents = []

    for element in list_of_documents_with_term:
        list_of_documents.append(element[0])
        # print(list_of_documents, element)
    return list_of_documents

def exact_match(query_content):
    # print(query_content)
    # print('inside exact match')
    track_list = []

    for x in query_content[:1]:
        # print('x first is:')
        # print(x)
        result = find_documents_with_terms_matching(x)
        # print('result is:')
        # print(result)
        track_list = result
        print('track list is:')
        print(track_list)

    for x in query_content[1:]:
        # print('x second is:')
        # print(x)
        result = find_documents_with_terms_matching(x)
        track_list = list(set(track_list).intersection(result))
        # for y in track_list:
        #     if y in track_list:
        #         track_list = track_list

    print(track_list)

    for i in range(len(query_content)):
        list1 = []
        list2 = []
        key = inverted_index[query_content[i]]
        for k in key:
            if k[0] == track_list[0]:
                list1 = k[2]
        if i == len(query_content) - 1:
            break
        key = inverted_index[query_content[i+1]]
        for k in key:
            if k[0] == track_list[0]:
                list2 = k[2]
        for li in list1:
            for li2 in list2:
                k = li - li2
                if k == -1:
                    print("match")
                    print(key)
                    for x in key:
                        print(x[0])



def best_match(query_term):
    print('query_term is : ')
    print(query_term)
    new_final_list = []
    final_list = []
    for x in query_term:
        postings_list = inverted_index[x]
        final_list.append(postings_list)

    print(final_list)

    for x in final_list:
        # print(x)
        for y in x:
            print(y[0])
            if (y[0]) not in new_final_list:
                new_final_list.append(y[0])
            # print('\n')


    print('new_final_list is:')
    print(new_final_list)



def prox_match(query, n):
    n = int(n)
    print(type(n))

    print('Query terms are:')
    print(query)


    new_dict = {}

    for query_word in query:
        print('Postings list for term in query:', query_word)
        print(inverted_index[query_word])
        print('\n')
        new_dict[query_word] = inverted_index[query_word]


    print('New dictionary is:')
    print(new_dict)
    print('\n')


    print('List to store the positions for a terms is called list567')
    list567 = []
    print('\n')

    print('inverted list to store the document name as key and the [[query term1, positions][query term2, position]]')

    inverted_dict = {}

    print('\n')


    for query_word in new_dict.keys():
        # inverted_dict[]


        for val in new_dict[query_word]:

            temp = []
            if(val[0] in inverted_dict.keys()):
                if(query_word in inverted_dict[val[0]].keys()):
                    temp = inverted_dict[val[0]].get(query_word)

            for z in (val[2]):

                temp.append(z)


            if(val[0] not in inverted_dict.keys()):
                inverted_dict[val[0]] = {query_word: temp}
            else:
                inverted_dict[val[0]].update({query_word: temp})
        print(inverted_dict)
        print('\n')
        print('\n')


        for x in inverted_dict:
            print(x)
            print('\n')





# Declaring the main function in Python
def main():
    loading_inverted_index_from_content('/Users/mihirg/PycharmProjects/extracreditnew/1_position_inverted_index.txt')
    query_content = enter_query()
    # query_content = query_content.split(" ")
    print(query_content)
    stop_word_list()
    query_content = remove_stop_words_from_query(query_content)
    query_content = remove_punctuations(query_content)
    print(query_content)
    exact_match(query_content)
    # best_match(query_content)
    n = input("Enter the value for proximity n" + "\n")
    print(n)
    prox_match(query_content, n)

# Checking if the program is being run by itself or imported from another module
if __name__ == '__main__':
    # print ('This program is being run by itself');
    main()
else:
    print('the program is imported from another module')
