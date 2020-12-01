import sys

import pandas as pd


# not sure, maybe need refactoring
def find_first_name(name):
    try:
        dot_index = name.index('.')
    except ValueError:
        dot_index = False

    try:
        bracket_index = name.index('(')
    except ValueError:
        bracket_index = False

    if dot_index and not bracket_index:
        try:
            space_index = name.index(' ', dot_index + 2)
            result = name[dot_index:space_index]
        except ValueError:
            result = name[dot_index:]

        return result.replace('.', '').replace(' ', '')
    elif bracket_index:
        try:
            return name[bracket_index + 1:name.index(' ', bracket_index + 2)]
        except ValueError:
            return name[bracket_index + 1:name.index(')')]
    else:
        return name


if __name__ == '__main__':
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
    взаимосвязи двух переменных, измеренных в метрических шкалах на одной и
    той же выборке. Он позволяет определить, насколько пропорциональная
    изменчивость двух переменных.
    """
    pearsonn_corr = data['SibSp'].corr(data['Parch'])
    print(f'Pearsonn correlation = {pearsonn_corr}')

    data['first_name'] = data['Name'].apply(find_first_name)
    most_pop_women_name = data[data['Sex'] == 'female']['first_name'] \
        .value_counts().idxmax()
    print(f'Most popular women name = {most_pop_women_name}')

    sys.exit()
