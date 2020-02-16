import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

sns.set()

columns = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness', 'mean compactness',
           'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension', 'radius error',
           'texture error', 'perimeter error', 'area error', 'smoothness error', 'compactness error', 'concavity error',
           'concave points error', 'symmetry error', 'fractal dimension error', 'worst radius', 'worst texture',
           'worst perimeter', 'worst area', 'worst smoothness', 'worst compactness', 'worst concavity',
           'worst concave points', 'worst symmetry', 'worst fractal dimension']
dataset = load_breast_cancer()
data = pd.DataFrame(dataset['data'], columns=columns)
data['cancer'] = dataset['target']

X = data.drop(columns=['cancer'])
y = data['cancer']

x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=2020)

ss = StandardScaler()
X_train_scaled = ss.fit_transform(x_train)
X_test_scaled = ss.transform(x_test)
y_train = np.array(y_train)

rfc = RandomForestClassifier()
rfc.fit(X_train_scaled, y_train)
rfc.score(X_train_scaled, y_train)

feats = {}
for feature, importance in zip(data.columns, rfc.feature_importances_):
    feats[feature] = importance

importances = pd.DataFrame.from_dict(feats, orient='index').rename(columns={0: 'Gini-Importance'})
importances = importances.sort_values(by='Gini-Importance', ascending=False)
importances = importances.reset_index()
importances = importances.rename(columns={'index': 'Features'})
sns.set(font_scale=5)
sns.set(style="whitegrid", font_scale=1.7)
fig, ax = plt.subplots()
fig.set_size_inches(30, 15)
sns.barplot(x=importances['Gini-Importance'], y=importances['Features'], data=importances, color='skyblue')
plt.xlabel('Importance', fontsize=25, weight='bold')
plt.ylabel('Features', fontsize=25, weight='bold')
plt.title('Feature Importance', fontsize=25, weight='bold')
plt.show()
