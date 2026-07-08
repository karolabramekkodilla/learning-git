import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
df = pd.read_csv('HRDataset.csv')

df['DateofHire'] = pd.to_datetime(df['DateofHire'])
df['Seniority'] = (pd.Timestamp.today() - df['DateofHire']).dt.days / 365

print(df.head())

plt.figure(figsize=(15,5))
sns.barplot(x='Department',y='PayRate',data=df)

plt.figure(figsize=(15,5))
sns.barplot(x='Department',y='PayRate',data=df,estimator=np.median)

plt.figure(figsize=(15,5))
sns.countplot(x='Department',data=df)

plt.figure(figsize=(15,5))
sns.boxplot(x='Sex',y='PayRate',data=df)

pd.crosstab(df['Department'],df['Sex'])
plt.figure(figsize=(15,5))
sns.boxplot(x='Sex',y='PayRate',data=df,hue='HispanicLatino')
plt.figure(figsize=(15,5))
df['HispanicLatino'] = df['HispanicLatino'].str.title()
sns.boxplot(x='Sex',y='PayRate',data=df,hue='HispanicLatino')

plt.figure(figsize=(15,5))
sns.violinplot(x='Sex',y='PayRate',data=df)
plt.figure(figsize=(15,5))
sns.violinplot(x='Sex',y='PayRate',data=df,hue='HispanicLatino',split=True)

plt.figure(figsize=(15,5))
g = sns.FacetGrid(data=df,col='Department',row='Sex')
g = sns.FacetGrid(data=df,col='Department',row='Sex')
g.map(plt.scatter,'Seniority','PayRate')

plt.figure(figsize=(15,5))
sns.lmplot(x='Seniority',y='PayRate',data=df[(df['Department']=='Production       ')],hue='Sex',markers=['o','v'],
          scatter_kws={'s':50})
plt.figure(figsize=(15,5))
sns.lmplot(x='Seniority',y='PayRate',data=df[(df['Department']=='Production       ')],col='Position',hue='Sex',aspect=0.7)

plt.figure(figsize=(15,5))
sns.heatmap(df.pivot_table(index=df['DateofHire'].dt.month,columns=df['DateofHire'].dt.day,values='EmpID',aggfunc='count').fillna(0))
plt.show()

