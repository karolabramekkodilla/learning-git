import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
df = pd.read_csv('HRDataset.csv')
print(df.head())

plt.figure(figsize=(15,10))
sns.heatmap(df.isnull())
df.drop(['LastPerformanceReview_Date','DaysLateLast30'],axis=1,inplace=True)
df.dropna(thresh=2,inplace=True)

df[['DateofTermination','DOB','DateofHire']].dtypes
df['DOB'] = pd.to_datetime(df['DOB'],format='%m/%d/%y')
df['DateofTermination'] = pd.to_datetime(df['DateofTermination'],format='%m/%d/%y')
df['DateofHire'] = pd.to_datetime(df['DateofHire'],format='%m/%d/%Y')
print(df[['DateofTermination','DOB','DateofHire']].head())

# plt.figure(figsize=(10,6))
# sns.histplot(df['PayRate'])

sns.displot(df['PayRate'])
plt.show()
sns.kdeplot(df['PayRate'], fill=True, bw_adjust=.05, color="green")
sns.kdeplot(df['PayRate'], fill=True, bw_adjust=.5, color="red")
sns.kdeplot(df['PayRate'], fill=True, bw_adjust=.95, color="gray")
plt.show()
sns.jointplot(x='PayRate',y='EngagementSurvey',data=df)
plt.show()

import datetime as dt

def count_seniority(row):

    if pd.isnull(row['DateofTermination']):
        end_date = dt.datetime(2019,9,27)
    else:
        end_date = row['DateofTermination']

    return (end_date - row['DateofHire']).days / 365.25

df['Seniority'] = df.apply(lambda row: count_seniority(row),axis=1)
print(df[['DateofHire','DateofTermination','Seniority']].head())

sns.jointplot(x='PayRate',y='Seniority',data=df,kind='hex')


sns.pairplot(df[df.columns[~df.columns.str.endswith('ID')]].select_dtypes(float))
plt.show()
