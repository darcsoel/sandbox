import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

bli = pd.read_csv('../../../BetterLifeIndex2015.csv')

life_satisfaction = np.c_[bli['Life satisfaction']]
rate = np.c_[bli['Employment rate']]

model = LinearRegression()
model.fit(rate, life_satisfaction)

plt.scatter(rate, life_satisfaction, facecolor='red', alpha=0.5)
plt.show()

test = [[73]]
print(model.predict(test))

test = [[33]]
print(model.predict(test))

test = [[50]]
print(model.predict(test))

exit()
