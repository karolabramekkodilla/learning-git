shopping_dict = {'piekarnia' : ['chleb','pączek','bułki'],
                 'warzywniak' : ['marchew', 'seler', 'rulkola']}

print('Lista zakupów')

for key, value in shopping_dict.items():
    print('Idę do ', key,', kupuje tu następujące rzeczy:', value)