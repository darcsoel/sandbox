from sys import exit

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

sns.set()

model = make_pipeline(TfidfVectorizer(), MultinomialNB())

categories = ['alt.atheism', 'talk.religion.misc', 'soc.religion.christian',
              'comp.graphics', 'sci.med', 'sci.space']

train = fetch_20newsgroups(categories=categories)
test = fetch_20newsgroups(categories=categories, subset='test')

model.fit(train.data, train.target)
labels = model.predict(test.data)

matrix = confusion_matrix(test.target, labels)
sns.heatmap(matrix.T, square=True, annot=True, xticklabels=train.target_names,
            yticklabels=train.target_names)

plt.xlabel('true')
plt.ylabel('predicted')

plt.show()


def predict_text_category(text):
    """convert phrase into list of phrases, return text label"""

    label = model.predict([text])
    return train.target_names[label[0]]


text_to_predict = ['some space ship', 'some religion stuff',
                   'big red church', 'new colors']

for phrase in text_to_predict:
    print(predict_text_category(phrase))

exit()

# unix time util on Macbook Air i5 I5-5250U without plt.show()
# real    0m3.856s
# user    0m3.627s
# sys     0m0.429s

# with predict func
# real    0m4.434s
# user    0m4.194s
# sys     0m0.458s


# unix time util on Ubuntu, Intel® Core™ i5-4460, without plt.show()
# real    0m2,197s
# user    0m2,176s
# sys     0m0,229s

# unit time on AMD Ryzen 5 3600 6-core with predict func
# real    0m1,851s
# user    0m1,871s
# sys     0m0,327s
