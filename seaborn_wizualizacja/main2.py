import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
bike_data = pd.read_csv('daily-bike-share.csv', index_col='instant')

print(bike_data.head())

sns.pairplot(bike_data[['temp', 'hum', 'windspeed', 'rentals']])

sns.pairplot(bike_data[['season', 'temp', 'hum', 'windspeed', 'rentals']], hue='season', palette='bright')

plt.figure(figsize=(9, 6))
sns.heatmap(bike_data[['temp', 'hum', 'windspeed', 'rentals']].corr(), vmin=-1, vmax=1, annot=True)

plt.show()
