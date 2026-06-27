import pandas as pd
import numpy as np

labels  = ['Student A', 'Student B', 'Student C', 'Student D']
exam1 = [89,85,93,83]
exam2 = [74,56,44,92]
exam3=[67,59,79,84]
df = pd.DataFrame({'e1':exam1, 'e2':exam2, 'e3':exam3}, index=labels)
df['semester1'] = df['e1']+df['e2']+df['e3']

schools = ['High School X','High School X','High School Y','High School Y']
multi_index_list = [(school,student) for school,student in zip(schools,df.index)]
multi_index_list

df.index = pd.MultiIndex.from_tuples(multi_index_list,names=['School','Student'])
d1 = df

exam4 = np.random.randint(0, 101, size=4)
exam5 = np.random.randint(0, 101, size=4)
exam6 = np.random.randint(0, 101, size=4)

df = pd.DataFrame({'e4':exam4, 'e5':exam5, 'e6':exam6}, index=labels)
df['semester2'] = df['e4']+df['e5']+df['e6']
df.index = d1.index
d2 = df


d3 = pd.concat([d1, d2], axis=1)

d3.drop('semester1',axis=1,inplace=True)
d3.drop('semester2',axis=1,inplace=True)

multi_index_list = [
    ('semester1', 'e1'),
    ('semester1', 'e2'),
    ('semester1', 'e3'),
    ('semester2', 'e4'),
    ('semester2', 'e5'),
    ('semester2', 'e6')
]
d3.columns = pd.MultiIndex.from_tuples(multi_index_list,names=['semester','exam'])

print("d1")
print(d1)
print("d2")
print(d2)
print("d3")
print(d3)
# print(d1)
# print(d1)
# print(d1)