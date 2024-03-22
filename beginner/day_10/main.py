from art import logo

print(logo)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}

more_calculations = True

while more_calculations:

    num1 = float(input("what is the first number: "))

    for o in operations:
        print(o)
    op = input("which operation do you want to perform? ")

    num2 = float(input("what is the second number: "))

    answer = operations[op](num1, num2)
    print(f"{num1} {op} {num2} = {answer}")

    if input("do you want to do another operation: y/n ") != "y":
        more_calculations = False
