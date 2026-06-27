import pandas as pd
import numpy as np

df = pd.DataFrame({'Category':['Games','Games','Games',

                               'Film&Video','Film&Video','Film&Video'],

                  'Project_Title':['The Last Faith','Magic Puzzles','Dinosaur Fossil Hunter',

                                   'Beyond Your Eyes','5150','8-Bit Wars'],

                  'Pledged':[92774,2873519,7962,

                             276,23963,6950],

                  'Country':['UK','USA','Poland',

                             'Bulgaria','USA','UK'],

                  'Date_Start':['2020-03-21','2020-03-11','2020-04-16',

                                '2020-02-09','2020-04-10','2020-03-19']})
df.groupby('Category')
print(df.groupby('Category').sum())
d2=df.groupby('Category').count()
d3 = df[['Category', 'Pledged']].groupby('Category').mean()
print(d2)
print(d3)

df['Date_Start'] = pd.to_datetime(df['Date_Start'])
d4 = df.groupby(pd.Grouper(key='Date_Start',freq='ME')).sum()
print(d4)

d5 = df.groupby(pd.Grouper(key='Date_Start',freq='ME')).agg({'Pledged':'sum','Project_Title':'count'})
print(d5)

d6 = df.groupby(['Country', 'Category'])['Pledged'].sum()
print(d6)