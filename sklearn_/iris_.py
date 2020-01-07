"""Basic dataset"""

import reprlib
from sklearn import datasets, decomposition, metrics, mixture, model_selection, naive_bayes, svm

X, y = datasets.load_iris(return_X_y=True)
x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, random_state=1)

gaussian_model = naive_bayes.GaussianNB()
gaussian_model.fit(x_train, y_train)
gaussian_y_model = gaussian_model.predict(x_test)

gaussian_accuracy = metrics.accuracy_score(y_test, gaussian_y_model)
print(f'Gaussian model accuracy = {gaussian_accuracy}')

svc_model = svm.SVC(kernel='linear', C=1)
svc_model.fit(x_train, y_train)
svc_y_model = svc_model.predict(x_test)

svc_accuracy = metrics.accuracy_score(y_test, svc_y_model)
print(f'SVC model accuracy = {svc_accuracy}')

decomposition_model = decomposition.PCA(n_components=2)
decomposition_model.fit(x_train)
x2d = decomposition_model.transform(x_train)

print(f'Decomposition to 2d array - {reprlib.repr(x2d)}')

gmm_model = mixture.GaussianMixture(n_components=3)
gmm_model.fit(x_train, y_train)
gmm_y_model = gmm_model.predict(x_test)

gmm_accuracy = metrics.accuracy_score(y_test, gmm_y_model)
print(f'GMM model accuracy = {gmm_accuracy}')
