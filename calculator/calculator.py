# import clear


def add(n1, n2):
    """adds the number """
    return n1 + n2


def substract(n1, n2):
    """perfroms subtraction of n1 , n2 """
    return n1 - n2


def multiply(n1, n2):
    """performs multiplication n1*n2"""

    return n1 * n2


def divide(n1, n2):
    """performs division n1/n2"""
    return n1 / n2


def fac(x):
    i = 1
    fac = 1
    while i <= x:
        fac = fac * i
        i = i + 1
    return fac

def power(n1 , n2):
    return n1**n2




# calculayionss


def calculator():
    logo = """
     _____________________
    |  _________________  |
    | |     AKSHXY    0.| |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """

    print(logo)

    operation = {
        "+": add,
        "-": substract,
        "*": multiply,
        "/": divide,
        "^(power)": power,
        "!": fac
    }

    num_1 = float(input("whats the first number ? \n"))
    should_continue = True
    while should_continue is True:

        # num_2 = float(input("whats the next number ? \n"))

        for symbol in operation:
            print(symbol)

        operation_symbol = input("what operation do you want to perform ? \n")
        if operation_symbol == "^":
            num_2 = float(input("Enter Power: \n"))
            answer = num_1 ** num_2
            print(f" {num_1}^{num_2} = {answer}")
            reply = input("do yu want to continue? 'y' to continue or 'n' for new calculation \n")
            if reply == "y":
                should_continue = True
                num_1 = answer
            else:
                should_continue = False
                # clear()
                calculator()
        elif operation_symbol == "!":
            answer = fac(num_1)
            print(f" {num_1}! = {answer}")
            reply = input("do yu want to continue? 'y' to continue or 'n' for new calculation \n")
            if reply == "y":
                should_continue = True
                num_1 = answer
            else:
                should_continue = False
                # clear()
                calculator()
        else:
            num_2 = float(input("whats the next number ? \n"))

            work = operation[operation_symbol]
            answer = work(num_1, num_2)

            print(f"{num_1} {operation_symbol} {num_2} = {answer} ")

            reply = input("do yu want to continue? 'y' to continue or 'n' for new calculation \n")
            if reply == "y":
                should_continue = True
                num_1 = answer
            else:
                should_continue = False
                # clear()
                calculator()


calculator()
