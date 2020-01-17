import pandas as pd

data = pd.read_csv('../../titanic.csv')

# LESSON_1
male_count = data[data.Sex == 'male']['PassengerId'].value_counts()
female_count = data[data.Sex == 'female']['PassengerId'].value_counts()
print(male_count)
print(female_count)

survived = data['Survived'].value_counts(normalize=True) * 100
print(survived)

first_class_trip = data['Pclass'].value_counts(normalize=True) * 100
print(first_class_trip)

age_avg = data['Age'].mean()
print(age_avg)

age_median = data['Age'].median()
print(age_median)

"""
Method corr() get param - value to correlate
Without param it will return matrix - all to all correlations

Коэффициент корреляции Пирсона (r-Пирсона) применяется для исследования 
взаимосвязи двух переменных, измеренных в метрических шкалах на одной и той же 
выборке. Он позволяет определить, насколько пропорциональная 
изменчивость двух переменных.

"""
pearsonn_corr = data['SibSp'].corr(data['Parch'])
print(pearsonn_corr)

data.Name = data.apply(lambda x: x['Name'][x['Name'].find('. ') + 2:], axis=1)
data.Name = data.apply(lambda x: x['Name'] + ' ', axis=1)
data.Name = data.apply(lambda x: x['Name'][:x['Name'].find(' ')], axis=1)

"""
Return wrong data but works fine
Error in data, some male names have female sex
Need to fix somehow

"""
most_pop_women_name = data[data['Sex'] == 'female']['Name'].value_counts().idxmax()
print(most_pop_women_name)

names = pd.crosstab(data['Name'], data['Sex'])
print(names)
