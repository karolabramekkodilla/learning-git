import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt


df = pd.DataFrame({'A':np.random.randn(200),
                 'B':[dt.datetime(2019,1,1)+dt.timedelta(days=x) for x in range(200)],
                  'C':np.arange(1,201)})

df['A'].hist(bins=30)

df['C'].loc[:10].plot(kind='bar')
df.plot.line(x='B',y='A',figsize=(12,5), c='red',lw=2)
plt.show()