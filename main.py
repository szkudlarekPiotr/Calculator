from art import logo

print(logo)


def add(n1,n2):
    return n1 + n2


def subtract(n1,n2):
    return n1 - n2


def multiply(n1,n2):
    return n1 * n2


def divide(n1,n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    keep_running = True
    num1 = float(input("Enter the first number: "))

    while keep_running:
        for keys in operations:
            print(keys)
        sign = input("Enter the operation sign: ")
        num2 = float(input("Enter the next number: "))

        function = operations[sign]
        answer = function(num1, num2)

        print(f'{num1} {sign} {num2} = {answer}')

        should_continue = input(f"Type 'c' to continue calculating with {answer}, type 'r' to start again, or type 'x' to exit : ")
        if should_continue == 'x':
            keep_running = False
            print('Goodbye')
        elif should_continue == 'c':
            num1 = answer
        elif should_continue == 'r':
            keep_running = False
            calculator()

calculator()