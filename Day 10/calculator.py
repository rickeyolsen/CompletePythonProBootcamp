from os import system
from art import logo

print(logo)

# Add Function
def add(n1, n2):
    return n1 + n2

# Subtract Function
def subtract(n1, n2):
    return n1 - n2

# Multiply Function
def multiply(n1, n2):
    return n1 * n2

# Devide Function
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = int(input("What's the first number?: "))
    for i in operations:
            print(i)
    calculating = True
    
    while calculating:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the second number?: "))
        calc_funct = operations[operation_symbol]
        answer = calc_funct(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        if input("Do you want to keep calculating? Type 'y' or 'n': ") == "y":
            num1 = answer
        else:
            calculating = False
            calculator()
            
calculator()
    