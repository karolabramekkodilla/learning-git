import sys

def customized_hello(first_name, last_name, x):
    print("Hello %s %s %s!" % (x,first_name, last_name))

if __name__ == "__main__":
    print(sys.argv[1:])
    # if len(sys.argv) < 3:
    #     exit(1)
    # customized_hello(input("Podaj imie\n"), input("Podaj nazwisko\n"))
    customized_hello(sys.argv[1],sys.argv[2],sys.argv[3])