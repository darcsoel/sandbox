import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

bli = pd.read_csv('../../../BetterLifeIndex2015.csv')
bli['Life satisfaction'] *= 10
bli['Employment rate'] *= 10

life_satisfaction = np.c_[bli['Life satisfaction'].astype(int)]
rate = np.c_[bli['Employment rate'].astype(int)]

model = LogisticRegression()
model.fit(rate, life_satisfaction)

plt.scatter(rate, life_satisfaction, facecolor='red', alpha=0.5)
plt.show()

test = [[730]]
print(model.predict(test))

test = [[330]]
print(model.predict(test))

test = [[500]]
print(model.predict(test))

exit()
