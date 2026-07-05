import matplotlib.pyplot as plt
import numpy as np


# # fig = plt.figure()
# # axes = fig.add_axes([0,0,1,1]) # left, bottom, width, height
# # axes2 = fig.add_axes([.2,.2,.8,.8])
# x = np.arange(11)
# y = x ** 2
# # axes.plot(x,y)

# # axes.set_xlabel('oś X')
# # axes.set_ylabel('oś Y')
# # axes.set_title('Tytuł wykresu')
# rand_arr = np.random.randint(0, 100, (100, 2))
# # axes2.scatter(rand_arr[:,0],rand_arr[:,1])
# # axes2.set_xlabel('Random')


# # print(axes.get_xlabel())
# # print(axes2.get_xlabel())

# fig = plt.figure()
# axes1 = fig.add_axes([0,0,1,1])
# axes2 = fig.add_axes([.2,.2,.8,.8])
# axes1.plot(x,y)
# axes2.scatter(rand_arr[:,0],rand_arr[:,1])
# axes1.set_xlabel('Exponential')
# axes2.set_xlabel('Random')

# plt.show()

# fig,axes = plt.subplots(nrows=1,ncols=2)
x = np.arange(11)
y = x ** 2
# axes[0].plot(x,y)
# axes[1].plot(y,x)



fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
# axes.plot(x,x**2,label='x^2')
# axes.plot(x,x**3,label='x^3')

# axes.plot(x,x**2,label='x^2',color='red',linewidth=3)
# axes.plot(x,x**3,label='x^3',linewidth=3,alpha=0.3)

axes.plot(x,x**2,label='x^2',
          color='red',
          linewidth=3,
          marker='o',
          markersize=20,
          markerfacecolor='orange',
          markeredgewidth=2)
axes.plot(x,x**3,label='x^3',linewidth=3,
          marker='*',
          markersize=10)
axes.legend(loc=(1.05,0.0))
fig2 = plt.figure()
axes2 = fig2.add_axes([0.1, 0.1, 0.8, 0.8])
axes2.bar(np.array(['a'*n for n in range(1,11)]),np.arange(1,11))
axes2.xaxis.set_major_locator(plt.MaxNLocator(7))


fig, ax = plt.subplots()

years = np.array(['2017','2018','2019','2020F'])
money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]

ax.bar(years, money)
def million(x, pos):
        return 'PLN {:2.1f}M'.format(x*1e-6)
formatter = plt.FuncFormatter(million)
ax.yaxis.set_major_formatter(formatter)
ax.yaxis.set_major_locator(plt.MultipleLocator(5e6))
ax.set_ylim(0,8e6)
ax.bar(years, money)
plt.show()