from art import logo


def add(n1, n2):
    """add two numbers"""
    return n1 + n2


def subtract(n1, n2):
    """subtract two numbers"""
    return n1 - n2


def multiply(n1, n2):
    """multiply two numbwrs"""
    return n1 * n2


def divide(n1, n2):
    """divide two numbers"""
    return n1 / n2


operations = {"-": subtract, "+": add, "*": multiply, "/": divide}


print(logo)


def calculator():
    areCalcOver = False
    n1 = float(input("Enter first number: "))
    for symbol in operations:
        print(symbol)
    operation = input("Pick an operation: ")
    n2 = float(input("Enter second number: "))

    calculation = operations[operation]
    answer = calculation(n1, n2)
    print(f"{n1} {operation} {n2} = {answer}")

    while not areCalcOver:
        choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if choice == "y":
            n1 = answer
            operation = input("Pick another operation: ")
            calculation = operations[operation]
            n2 = float(input("Enter next number: "))
            answer = calculation(n1, n2)
            print(f"{n1} {operation} {n2} = {answer}")
        else:
            areCalcOver = True
            calculator()


calculator()
