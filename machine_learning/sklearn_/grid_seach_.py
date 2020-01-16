from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, train_test_split, cross_val_score
from sklearn.svm import SVC

X, y = load_iris(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=1)

svc = SVC()
model = GridSearchCV(svc, param_grid={'kernel': ('linear', 'rbf'), 'C': [1, 10]})

cv = cross_val_score(model, X, y, cv=5)
print(cv)
print(cv.mean())
