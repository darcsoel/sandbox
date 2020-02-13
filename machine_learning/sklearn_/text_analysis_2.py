from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

model = make_pipeline(TfidfVectorizer(), MultinomialNB())

categories = ['alt.atheism', 'talk.religion.misc', 'soc.religion.christian', 'comp.graphics', 'sci.med']

train = fetch_20newsgroups(categories=categories)
test = fetch_20newsgroups(categories=categories, subset='test')

model.fit(train.data, train.target)
labels = model.predict(test.data)

matrix = confusion_matrix(test.target, labels)
sns.heatmap(matrix.T, square=True, annot=True, xticklabels=train.target_names, yticklabels=train.target_names)

plt.xlabel('true')
plt.ylabel('predicted')

plt.show()

exit()

# unix time util on Macbook Air without plt.show()
# real    0m3.856s
# user    0m3.627s
# sys     0m0.429s
