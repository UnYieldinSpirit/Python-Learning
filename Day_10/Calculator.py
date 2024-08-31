import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def result_print(op, n1, n2, result):
    print(f"{n1} {op} {n2} = {result}")

def operation_decision(op, n1, n2):
    if op == "+":
        result = add(n1, n2)
    elif op == "-":
        result = subtract(n1, n2)
    elif op == "*":
        result = multiply(n1, n2)
    elif op == "/":
        result = divide(n1, n2)

    result_print(op, n1, n2, result)
    return result

final_result = 0
proceed = False
restart = True
print(art.logo)

while restart == True:
    if proceed == True:
        first_num = final_result
    else:
        first_num = float(input("What is the first number?\n"))

    operation = input("+\n*\n/\n-\nPick an operation: ")

    second_num = float(input("What is the second number?\n"))

    final_result = operation_decision(operation, first_num, second_num)

    cont_calc = input(f"Type 'y' to continue calculating with {first_num}, or type 'n' to start a new calculation: ")

    if cont_calc == "y":
        proceed = True
    else:
        proceed = False