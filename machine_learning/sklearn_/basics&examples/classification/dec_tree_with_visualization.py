from subprocess import call

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.tree import DecisionTreeClassifier, export_graphviz

if __name__ == '__main__':
    x, y = make_blobs(n_samples=300, centers=4)

    tree = DecisionTreeClassifier(random_state=241)
    tree.fit(x, y)

    # for some reason visualization does not work for pandas dataframe
    # from prev dec_tree example
    export_graphviz(tree, out_file='tree.dot', rounded=True, proportion=False,
                    precision=2, filled=True)

    call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])

    plt.figure(figsize=(14, 18))
    plt.imshow(plt.imread('tree.png'))
    plt.axis('off')
    plt.show()

    exit()
