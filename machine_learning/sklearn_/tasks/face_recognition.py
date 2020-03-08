import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.datasets import fetch_lfw_people
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC

sns.set()

faces = fetch_lfw_people(min_faces_per_person=100)
n_samples, h, w = faces.images.shape
target_names = faces.target_names
n_classes = target_names.shape[0]
x_train, x_test, y_train, y_test = train_test_split(faces.data, faces.target, test_size=0.25, random_state=42)

n_components = 150
pca = PCA(svd_solver='randomized', whiten=True)
svc = SVC(kernel='rbf', class_weight='balanced')
model = make_pipeline(pca, svc)

parameters = {'pca__n_components': list(range(40, 140, 5)),
              'svc__C': [1e3, 5e3, 1e4, 5e4, 6e4, 1e5],
              'svc__gamma': np.linspace(0.001, 0.1, 100)}

grid = GridSearchCV(model, parameters, n_jobs=3, verbose=3)
grid.fit(x_train, y_train)

print(f'best params {grid.best_params_}')

model = grid.best_estimator_
test_model = model.predict(x_test)  # another option - grid.predict(x_test)
accuracy = accuracy_score(y_test, test_model)
print('accuracy = {0:.2f} percents'.format(accuracy * 100))

matrix = confusion_matrix(y_test, test_model)
sns.heatmap(matrix.T, square=True, annot=True, xticklabels=target_names, yticklabels=target_names)

plt.xlabel('true')
plt.ylabel('predicted')
plt.show()

exit()

# [Parallel(n_jobs=-1)]: Done 60000 out of 60000 | elapsed: 35.5min finished
# best params {'pca__n_components': 65, 'svc__C': 1000.0, 'svc__gamma': 0.011}
# accuracy = 90.88 percents
