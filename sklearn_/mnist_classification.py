import sklearn

mnist = sklearn.datasets.fetch_mldata('MNIST original')

x, y = mnist['data'], mnist['target']
