shopping_dict = {'piekarnia' : ['chleb','pączek','bułki'],
                 'warzywniak' : ['marchew', 'seler', 'rulkola']}

print('Lista zakupów')

for key, value in shopping_dict.items():
    capitalized_items = []
    for item in value:
        capitalized_items.append(item.capitalize())

    print('Idę do ', key.capitalize(),', kupuje tu następujące rzeczy:', capitalized_items)