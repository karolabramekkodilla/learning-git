def add_two(x,y):
    sum = x + y
    print(sum)

# add_two(10,2)

def shopping():
    shopping_items = [
        "jajka",
        "bułka",
        "ser feta",
        "masło",
        "pomidor"
    ]
    shopping_cart = "Koszyk zawiera: "
    for item in shopping_items:
        shopping_cart += item + '\n'
    return shopping_cart

# print(shopping())
# print(type(shopping()))
# print(type(add_two(2,2)))


def customized_hello(first_name, last_name, gender_prefix='Mr'):
    print(f"Hello {gender_prefix} {first_name} {last_name}!")

customized_hello("John", "Cleese")
customized_hello("Clara", "Cleese", "Ms")