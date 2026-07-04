import numpy as np
import pandas as pd

# wizualizacja

import matplotlib.pyplot as plt
import seaborn as sns

# Raport,do tworzenia podstawowego EDA

from ydata_profiling import ProfileReport

titanic_train = pd.read_csv('Titanic_train.csv')
print(titanic_train)

# profile = ProfileReport(titanic_train, title="Titanic -  Report")
# profile.to_file("titanic_report.html")

print(titanic_train.isnull().mean())
print(titanic_train.describe())

titanic_train_prepared = titanic_train.copy()

titanic_train_prepared.drop(['PassengerId'], axis=1, inplace=True)
print(titanic_train_prepared)

print(titanic_train_prepared['Survived'].value_counts(normalize=True))
print(titanic_train_prepared['Pclass'].value_counts(normalize=True))
sns.barplot(x='Pclass', y='Survived', data=titanic_train_prepared)
plt.show()

titanic_train_prepared = pd.concat([titanic_train_prepared, pd.get_dummies(titanic_train_prepared['Pclass'], drop_first=True)],  axis=1)
print(titanic_train_prepared)

titanic_train_prepared['Title'] = titanic_train_prepared['Name'].str.split(', ', expand=True)[1].str.split('.',  expand=True)[0]
titanic_train_prepared.drop(['Name'], axis=1, inplace=True)
print(titanic_train_prepared)

plt.figure(figsize=(20, 9))
sns.barplot(x='Title', y='Survived', data=titanic_train_prepared)
plt.show()

print(titanic_train_prepared['Title'].value_counts(normalize=True))

titanic_train_prepared.loc[~titanic_train_prepared['Title'].isin(['Mr', 'Miss', 'Mrs']), 'Title'] = 'Other'
print(titanic_train_prepared)

titanic_train_prepared = pd.concat([titanic_train_prepared, pd.get_dummies(titanic_train_prepared['Title'], drop_first=True)], axis=1)
titanic_train_prepared.drop(['Title'], axis=1, inplace=True)
print(titanic_train_prepared)

titanic_train_prepared = pd.concat([titanic_train_prepared, pd.get_dummies(titanic_train_prepared['Sex'], drop_first=True)], axis=1)
titanic_train_prepared.drop(['Sex'], axis=1, inplace=True)
print(titanic_train_prepared)

sns.boxplot(y='Age', x='Survived', data=titanic_train_prepared)
plt.show()

# jeśli wiek niższy niż 18 lat to jest to dziecko
titanic_train_prepared.loc[titanic_train_prepared['Age']<18, 'Child'] = 1

# osoba która nie jest dzieckiem otrzymała wartość 0
titanic_train_prepared.loc[titanic_train_prepared['Child']!=1, 'Child'] = 0
sns.barplot(x='Child', y='Survived', data=titanic_train_prepared)
plt.show()

age_median = titanic_train_prepared['Age'].median()
titanic_train_prepared['Age'] = titanic_train_prepared['Age'].fillna(age_median)
print(titanic_train_prepared)