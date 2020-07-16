import requests
import json
from sys import exit
import re


def download():
    urls = ['http://convai.io/data/data_tolokers.json', 'http://convai.io/data/data_intermediate.json',
            'http://convai.io/data/data_volunteers.json', 'http://convai.io/data/summer_wild_evaluation_dialogs.json',
            'http://convai.io/2017/data/train_full.json']

    for url in urls:
        slash = url.rindex('/')
        file_name = url[slash + 1:]
        json_text = requests.get(url)

        if not re.search(r'^data_(?s:/*)'):
            file_name = 'data_' + file_name

        with open(file_name, 'wb') as file:
            file.write(json_text.content)


if __name__ == '__main__':
    download()
    exit()
