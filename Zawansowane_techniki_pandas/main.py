import pandas as pd
import numpy as np
import math

df = pd.read_excel('Pivot.xlsx')
print(df.head())

print(df.pivot_table(values='Sprzedaż',index='Przedstawiciel',columns='Region',aggfunc=np.sum))
print(df.pivot_table(values='Sprzedaż',index='Przedstawiciel',columns='Region',aggfunc=np.sum).fillna(0).round(2))
print(df.pivot_table(values='Sprzedaż',index=['Region','Przedstawiciel'],aggfunc=np.sum).round(2))
print(df.pivot_table(values='Sprzedaż',index='Region',aggfunc=[len,np.max,np.min]).round(0))

def commission_fee(x):


    if x <= 300:
        return 0
    elif x <= 900:
        return x * 0.03
    else:
        return x * 0.06
def bonus(row):

    margin = (row['Sprzedaż'] - row['Koszty'])/row['Sprzedaż']

    if margin > 0.55:
        return 200
    else:
        return 0    
df['commission_fee'] = df['Sprzedaż'].apply(lambda x: commission_fee(x))
print(df)

df['Produkt_len'] = df['Produkt'].apply(len)
print(df)

df['#_opakowań'] = df['Sztuki'].apply(lambda x: math.ceil(x/5))
print(df)

df['Bonus'] = df.apply(lambda row: bonus(row),axis=1)
print(df.sample(10))

car_dict = dict(zip(df['Przedstawiciel'].unique(),['Mazda','Toyota','BMW','Audi','Fiat','Seat']))
df['Marka_samochodu'] = df['Przedstawiciel'].map(car_dict)
print(df)

df.map(lambda x: x.upper() if isinstance(x,str) else x)

df['Data'] = pd.to_datetime(df['Data'])
df['Data'].dt.day_name().head()
df['Data'].dt.month_name().head()
df[df['Data'].dt.day_name()=='Thursday'].head()
df['Produkt'].str.upper().head()

print(df['Region'].str.endswith('ód').head())

print(df[df['Region'].str.contains('Zachód')].sample(5))