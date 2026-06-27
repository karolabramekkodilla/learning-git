import pandas as pd
import numpy as np
import missingno as msno

df_with_nulls = pd.DataFrame({'A':[1,100,np.nan,1000,10000],
                             'B':[2,4,2,4,np.nan],
                             'C':[40,np.nan,20,np.nan,np.nan]})
df_with_nulls

print(df_with_nulls.isnull().mean())
print()
print(df_with_nulls.isnull().sum())

df_with_nulls[df_with_nulls['C'].isnull()]

# msno.matrix(df_with_nulls)
df_with_nulls.dropna()
df_with_nulls.dropna(thresh=2)

df_with_nulls['B'].fillna(df_with_nulls['B'].mean())