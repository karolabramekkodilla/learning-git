import pandas as pd
import numpy as np
exam1 = [89,85,93,83]
labels  = ['Student A', 'Student B', 'Student C', 'Student D']

print(pd.Series(exam1,labels))
print()

print(pd.Series(exam1,labels)['Student D'])
print()
d = {s:p for s,p in zip(labels,exam1)}
print(d)
print()
print(pd.Series(d))

exam2 = [74,56,44,92]

e1 = pd.Series(exam1,labels)
e2 = pd.Series(exam2,labels)

df = pd.DataFrame({'e1':exam1, 'e2':exam2},index=labels)
print(df)

data = np.array([exam1,exam2])
data.transpose()

df = pd.DataFrame(data.transpose(),index=labels,columns=['e1','e2'])
df

df.to_numpy()

df['e3'] = [67,59,79,84]
print(df)

df['semester1'] = df['e1'] + df['e2'] + df['e3']
print(df)
print()
print(df.loc['Student C'])
print()
print(df.iloc[1])
print()
print(df['e2'] > 70)
print(df[df['e2'] > 70])

print(df[(df['e2']<50)|(df['e2']>90)])

# print(df.drop('semester1',axis=1))
# print(df)
# df.drop(['e3','semester1'],axis=1,inplace=True)
# print(df)
# df.drop('Student B',inplace=True)
# print(df)
# print()
# df.reset_index(inplace=True)
# print(df)
print()
df_new_index = df.reset_index()

print(df_new_index)
print()
df_new_index['student_name'] = ['Adrian','Bartłomiej','Celina','Dagmara']
print(df_new_index)
df_new_index.set_index('student_name')
df_renamed = df_new_index.rename(columns={'e1':'exam1','e2':'exam2','e3':'exam3'})
print(df_renamed)