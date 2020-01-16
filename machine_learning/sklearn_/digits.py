import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.manifold import Isomap
from sklearn.metrics import accuracy_score, plot_confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

digits = load_digits()

iso = Isomap()
iso.fit(digits.data)
projected_data = iso.transform(digits.data)

plt.scatter(projected_data[:, 0], projected_data[:, 1], alpha=0.3,
            c=digits.target, cmap=plt.cm.get_cmap('Spectral', 10))
plt.colorbar(label='digit label', ticks=range(10))
plt.clim(-0.5, 9.5)
plt.show()

x, y = digits.data, digits.target

model = SVC(C=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
model.fit(x_train, y_train)

y_model = model.predict(x_test)
accuracy = accuracy_score(y_test, y_model)

print(f'Accuracy = {accuracy}')

matrix = plot_confusion_matrix(model, x_test, y_test)
plt.show()
