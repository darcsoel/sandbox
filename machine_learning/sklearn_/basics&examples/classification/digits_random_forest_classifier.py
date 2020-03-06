import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split


def main():
    sns.set()

    digits = load_digits()
    figure = plt.figure(figsize=(6, 6))
    figure.subplots_adjust(left=0, right=1, top=1, bottom=0, hspace=0.05, wspace=0.05)

    for i in range(64):
        ax = figure.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
        ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
        ax.text(0, 7, str(digits.target[i]))

    plt.show()

    x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=0)

    model = RandomForestClassifier(n_estimators=1000, n_jobs=-1, verbose=3)
    model.fit(x_train, y_train)

    y_model = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_model)

    print(f'Accuracy = {accuracy}')

    matrix = confusion_matrix(y_test, y_model)
    sns.heatmap(matrix.T, fmt='d', cbar=False, square=True, annot=True)
    plt.xlabel('true')
    plt.ylabel('predicted')
    plt.show()


if __name__ == '__main__':
    main()

