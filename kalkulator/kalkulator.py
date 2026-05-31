import os
import logging
os.makedirs("my_file_log", exist_ok=True)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="my_file_log/logfile.log")

def add_numbers(args):
    temp=args[0]
    for i in args[1:]:
        temp += i
    logging.debug(f"Suma liczb {args} wynosi {temp}")
    return temp

def multiply_numbers(args):
    temp=args[0]
    for i in args[1:]:
        temp *= i
    logging.debug(f"Mnożenie liczb {args} wynosi {temp}")
    return temp
def divide_numbers(args):
    temp=args[0]
    if args[1] == 0:
        logging.debug("Próba dzielenia przez 0")
        return "Infinity"
    for i in args[1:]:
        temp /= i
    logging.debug(f"Dzielenie liczb {args} wynosi {temp}")
    return temp
def subtract_numbers(args):
    temp=args[0]
    for i in args[1:]:
        temp -= i
    logging.debug(f"Odejmowanie liczb {args} wynosi {temp}")
    return temp

def input_two_numbers():
    try:
        a = float(input("Podaj składnik 1.\t"))
        b = float(input("Podaj składnik 2.\t"))
        return a,b
    except ValueError:
        logging.error("Podano wartość niebędącą liczbą")
        print("Podana wartość nie jest liczbą")
        return None
    
def input_many_numbers():
    arguments=[]
    value = None
    try:
        while value != "q":
            value = input("Podaj liczbę do działania lub -> q - zakończ")
            if value != "q":
                arguments.append(value)
            
    except ValueError:
        logging.error("Podano wartość niebędącą liczbą")
        print("Podana wartość nie jest liczbą")


if __name__ == "__main__":

    case = input(
        "Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "
    )
    try:
        if case == "1":
            args = input_two_numbers()
            result = add_numbers(args)
            print(f"Dodaję {args[0]:.2f} i {args[1]:.2f} ")
            print(f"Wynik to  {result:.2f}")
        elif case == "2":
            args = input_two_numbers()
            result = subtract_numbers(args)
            print(f"Odejmuję {args[0]:.2f} i {args[1]:.2f} ")
            print(f"Wynik to  {result:.2f}")
        elif case == "3":
            args = input_two_numbers()
            result = multiply_numbers(args)
            print(f"Mnożę {args[0]:.2f} i {args[1]:.2f} ")
            print(f"Wynik to  {result:.2f}")
        elif case == "4":
            args = input_two_numbers()
            result = divide_numbers(args)
            print(f"Dzielę {args[0]:.2f} i {args[1]:.2f} ")
            if type(result) == float:
                print(f"Wynik to  {result:.2f}")
            else:
                print(f"Wynik to Infinity")
        else:
            logging.debug("Wybrano nieprawidłowy case")
    except Exception as e:
        logging.exception(f"Wystąpił wyjątek: {e}")
