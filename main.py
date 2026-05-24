shopping_dict = {'piekarnia' : ['chleb','pączek','bułki'],
                 'warzywniak' : ['marchew', 'seler', 'rulkola']}

print('Shopping list')

counter = 0
for key, value in shopping_dict.items():
    capitalized_items = []
    for item in value:
        capitalized_items.append(item.capitalize())
        counter += 1

    print('Idę do ', key.capitalize(),', kupuje tu następujące rzeczy:', capitalized_items)
print('W sumie kupuję ',counter,' produktów')
