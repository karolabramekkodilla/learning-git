import pandas as pd
import matplotlib.pyplot as plt

bike_data_raw = pd.read_csv('daily-bike-share.csv')
print(bike_data_raw)
bike_data_raw['dteday'] = pd.to_datetime(bike_data_raw['dteday'])
print(bike_data_raw.info())

print(bike_data_raw['rentals'].describe())

plt.figure(figsize=(10, 6))

plt.plot(
    bike_data_raw["rentals"],
    bins=30,          # liczba przedziałów
    edgecolor="black" # obramowanie słupków
    
)

plt.title("Histogram liczby wypożyczeń")
plt.xlabel("Liczba wypożyczeń")
plt.ylabel("Liczba dni")

plt.show()

plt.figure(figsize=(16, 7))
plt.plot(bike_data_raw['dteday'], bike_data_raw['rentals'], label='Liczba wypożyczeń')
plt.plot(bike_data_raw['dteday'], bike_data_raw['rentals'].rolling(30).mean(), linewidth=3.0, label='30 dniowa średnia krocząca')
plt.xlim([bike_data_raw['dteday'].min(), bike_data_raw['dteday'].max()])
plt.ylim([0, bike_data_raw['rentals'].max()*1.025])
plt.legend(loc='upper left')
plt.show()

print('Przed usunięciem:')
display(bike_data_raw)
print('Po usunięciu:')
bike_data = bike_data_raw.copy()
bike_data.drop(['instant', 'dteday', 'yr'], axis=1, inplace=True)
display(bike_data)