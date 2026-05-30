def shopping(items, payment='card', shop='local'):
    shopping_cart = "Koszyk zawiera: "
    for item in items:
        shopping_cart += item + '\n'
    return shopping_cart


shopping_items = [
    "jajka",
    "bułka",
    "ser feta",
    "masło",
    "pomidor",
    "chusteczki",
    "papier toaletowy"
]

basket = shopping(shopping_items, payment= 'card')
print(basket)

def fun_default(x,y,key = 'key', type = 'type'):
    pass
def fun_positional(x,y):
    pass
def fun_keyword(key = 'key', type = 'type'):
    pass


def count_them_all(*args, **kwargs):
    positional_args_count = len(args)
    print(f"I have received {positional_args_count} positional arguments")
    keywords_args_count = len(kwargs)
    print(f"I have received {keywords_args_count} keywords arguments")

count_them_all(1, 2, 3, "A")