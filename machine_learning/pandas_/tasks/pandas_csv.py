import sys

import pandas as pd

data = pd.read_csv('../../../titanic.csv')

# LESSON_1
male_count = data[data.Sex == 'male']['PassengerId'].value_counts()
female_count = data[data.Sex == 'female']['PassengerId'].value_counts()
print(f'Male count = {male_count}')
print(f'Female count = {female_count}')

survived = data['Survived'].value_counts(normalize=True) * 100
print(f'Survived = {survived}')

first_class_trip = data['Pclass'].value_counts(normalize=True) * 100
print(f'First class trip count = {first_class_trip}')

age_avg = data['Age'].mean()
print(f'Average age = {age_avg}')

age_median = data['Age'].median()
print(f'Age median = {age_median}')

"""
Method corr() get param - value to correlate
Without param it will return matrix - all to all correlations

Коэффициент корреляции Пирсона (r-Пирсона) применяется для исследования
взаимосвязи двух переменных, измеренных в метрических шкалах на одной и той же
выборке. Он позволяет определить, насколько пропорциональная
изменчивость двух переменных.

"""
pearsonn_corr = data['SibSp'].corr(data['Parch'])
print(f'Pearsonn correlation = {pearsonn_corr}')


data['first_name'] = data['Name'].str.extract(r'(\.\s.[a-z]+)', expand=False)
data['first_name'] = data['first_name'].str.replace('. ', '')

most_pop_women_name = data[data['Sex'] == 'female']['first_name']\
    .value_counts().idxmax()
print(f'Most popular women name = {most_pop_women_name}')

names = pd.crosstab(data['Name'], data['Sex'])
print(names)

sys.exit()
