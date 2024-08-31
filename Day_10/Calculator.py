def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def operation_decision(op, n1, n2):
    if op == "+":
        add(n1, n2)
    elif op == "-":
        subtract(n1, n2)
    elif op == "*":
        multiply(n1, n2)
    elif op == "/"
        divide(n1, n2)


first_num = int(input("What is the first number?\n"))
operation = input("What operation would you like to execute?\n+\n*\n/\n-\n")
second_num = int(input("What is the second number?\n"))

operation_decision(operation)