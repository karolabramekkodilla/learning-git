import pandas as pd
import gmplot

zip_codes = pd.read_csv('us-zip-code-latitude-and-longitude.csv',sep=';')
zip_codes.head()

df = pd.read_csv('HRDataset.csv')
df.head()
df_mapping = df[['Zip','PayRate']].copy()
df_mapping.head()

df_mapping = df_mapping.join(zip_codes.set_index('Zip')[['Latitude','Longitude']],on='Zip',how='left')