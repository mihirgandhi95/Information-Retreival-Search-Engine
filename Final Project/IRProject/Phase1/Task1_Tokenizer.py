import re
import os
from bs4 import BeautifulSoup

# create folder for Task1 Output Tokens to be stored
outputFolder = './Task1_Output_Tokens/'
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

inputFolder = os.path.dirname("/Users/mihirg/Desktop/InformationRetrievalSpring2018/Final/IRProject/cacm/")


def select_specific_content(output_text):
    remove_AM = output_text.rfind("am")
    remove_PM = output_text.rfind("pm")

    if remove_AM > remove_PM:
        keep_content_till_index = remove_AM
    else:
        keep_content_till_index = remove_PM

    output_text = output_text[:(keep_content_till_index + 2)]
    return output_text


def write_to_file(output_text, file):
    writer = open(outputFolder + file[: -5] + '.txt', 'w', encoding='utf-8')
    output_text = output_text.lower()
    writer.write(output_text.strip())
    writer.close()


def task1():
    for file in os.listdir(inputFolder):
        current_file = os.path.join(inputFolder, file)
        page_content = open(current_file, 'r').read()
        soup = BeautifulSoup(page_content, "html.parser")
        for content in soup.find_all("html"):
            required_text = content.text
            required_text = re.sub(r"[^0-9A-Za-z,-\.:\\$]", " ", required_text)
            output_text = re.sub(r"(?!\d)[$,%,:.,-](?!\d)", " ", required_text, 0)
            output_text = output_text.split()
            for data in output_text:
                if data.startswith('-'):
                    data.replace(data, data.split('-')[1])
                if data.endswith('-'):
                    data.replace(data, data.split('-')[0])
                else:
                    continue
            output_text = ' '.join(output_text)
            output_text = output_text.lower()
            output_text = select_specific_content(output_text)

            write_to_file(output_text, file)


def main():
    task1()


if __name__ == '__main__':
    main()
else:
    print('the program is imported from another module')
