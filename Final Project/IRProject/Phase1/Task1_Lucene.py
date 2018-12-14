import re

file = r'/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Task1_Lucene.txt'
text = open(file, 'r').readlines()

relevance_dictionary = {}
regex = re.compile('CACM-\d+')

list = []
for line in text:
    list.append(regex.findall(line))

final_list = []
for x in list:
    if len(x) != 0:
        final_list.append(x)

print(final_list)
print("=====================")
print("length = ", len(final_list))

output_file = open('/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/Lucene_Top100_Docs.txt', 'w')
for x in final_list:
    for eachlist in x:
        output_file.write(str(eachlist) + '\n')
