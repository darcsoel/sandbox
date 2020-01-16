from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.utils import tokenize

corpus = []

corpus = [list(tokenize(doc)) for doc in corpus]

text = [TaggedDocument(w, i) for i, w in enumerate(corpus)]

model = Doc2Vec(corpus, size=10, min_count=0)
