import pandas as pd
import numpy as np

df = pd.DataFrame({'A':[100,44,56,99,85,100],
                  'B':['Panda','Snake','Snake','Rat','Dog','Panda']})

d1 = df['B'].unique()
d2 = df['B'].nunique()
d3 = df['B'].value_counts()
d4 = df['B'].value_counts(normalize=True)
d5 = df.sort_values(by='A')
d6 = df.drop_duplicates()
print (d1)
print (d2)
print (d3)
print (d4)
print (d5)
print (d6)