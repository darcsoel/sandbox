import nltk

from machine_learning.nlp.chat_bot.retrieve_datasets import DialogsRetriever

nltk.download('punkt')
nltk.download('wordnet')


if __name__ == '__main__':
    train_dialogs = DialogsRetriever().data

    for dialog in train_dialogs:
        d = 1

    exit()
