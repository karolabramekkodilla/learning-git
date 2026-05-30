def shopping(items, payment='card', shop='local'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupię następujące rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić, używam %s." % payment
    return result

items = ["cola", "whiskey", "lód"]
text = shopping(items, 'card', 'small local shop')
print(text)