import pandas as pd
import numpy as np
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],

                    'B': ['B0', 'B1', 'B2', 'B3'],

                    'C': ['C0', 'C1', 'C2', 'C3'],

                    'D': ['D0', 'D1', 'D2', 'D3']},

                    index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],

                    'B': ['B4', 'B5', 'B6', 'B7'],

                    'C': ['C4', 'C5', 'C6', 'C7'],

                    'D': ['D4', 'D5', 'D6', 'D7']},

                    index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],

                    'B': ['B8', 'B9', 'B10', 'B11'],

                    'C': ['C8', 'C9', 'C10', 'C11'],

                    'D': ['D8', 'D9', 'D10', 'D11']},

                    index=[8, 9, 10, 11])

def make_keys(n):
    return [f'key{n}' for n in range(n)]


left = df1.copy()
left['key'] = make_keys(4)
right = df3.copy()
right['key'] = make_keys(4)
print(left)
print(right)

d1 = pd.merge(left,right,how='inner',on='key')
print(d1)

new_right = pd.DataFrame({'E': ['E1','E2','E3','E4','E5','E6'],
                          'key': make_keys(6)})
new_right

d2 = pd.merge(left,new_right,how='inner',on='key')
print(d2)
d3 = pd.merge(left,new_right,how='outer',on='key')
print(d3)

other = pd.DataFrame({'E':['E1','E2','E3','E4','E5','E6']},index=['B1','B2','B3','B4','B5','B6'])
d4 = left.join(other,on='B')
print(d4)

d5 = left.join(
    right.set_index('key'),
    on='key',
    lsuffix='_left',
    rsuffix='_right'
)

print(d5)