from bs4 import BeautifulSoup
import os
import re

common_words_dict = []
corpus = "/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/cacm/"
output = './Task3_PartA_Stopping_tokens_output/'


def init():
    with open('/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/Phase1/common_words', 'r') as file:
        line = file.readlines()
    line = [x.strip() for x in line]
    common_words_dict.extend(line)

    if not os.path.exists(output):
        os.makedirs(output)


def task3_tokenizer_stopping():
    for file in os.listdir(corpus):
        current_file = os.path.join(corpus, file)
        page_content = open(current_file, 'r').read()
        soup = BeautifulSoup(page_content, "html.parser")
        for content in soup.find_all("html"):
            content_text = content.text
            content_text = re.sub(r"[^0-9A-Za-z,-\.:\\$]", " ", content_text)
            result_text = re.sub(r"(?!\d)[$,%,:.,-](?!\d)", " ", content_text, 0)
            result_text = result_text.split()
            for text in result_text:
                if text.startswith('-'):
                    text.replace(text, text.split('-')[1])
                if text.endswith('-'):
                    text.replace(text, text.split('-')[0])
                else:
                    continue

            result_text = [x for x in result_text if x not in common_words_dict]
            result_text = ' '.join(result_text)
            result_text = result_text.lower()
            AM_index = result_text.rfind("am")
            PM_index = result_text.rfind("pm")
            if AM_index > PM_index:
                greater_index = AM_index
            else:
                greater_index = PM_index
            result_text = result_text[:(greater_index + 2)]

            writer = open(output + file[:-5] + '.txt', 'w', encoding='utf-8')
            writer.write(result_text.strip())
            writer.close()


def main():
    init()
    task3_tokenizer_stopping()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
