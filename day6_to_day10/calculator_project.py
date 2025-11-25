calculator_pic = """
-----------------
|   CALC 1.0    |
|---------------|
|   [   0   ]   |
| ------------- |
| [7][8][9][/]  |  CALCULATOR!
| [4][5][6][*]  |
| [1][2][3][-]  |
| [0][.][=][+]  |
-----------------
"""
print(calculator_pic)

def add(n1, n2):
    """Take two inputs and sum them"""
    return n1 + n2

def subtract(n1, n2):
    """Take two inputs and subtract them"""
    return n1 - n2

def multiply(n1, n2):
    """Take two inputs and multiply them"""
    return n1 * n2

def divide(n1, n2):
    """Take two inputs and divide them"""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

import os

while True:
    
    f_number = float(input("What's the first number: "))

    while True:
        operator = str(input("Pick an operation:\n + \n - \n * \n / \n"))
        s_number = float(input("What's the second number: "))

        result = operations[operator](f_number, s_number)
        print(f"{f_number} {operator} {s_number} = {result} ")

        continue_number = str(input("Type 'y' to continue calculating with or 'n' to restart calculator: "))
        if continue_number == "y":
            f_number = result
        
        else:
            os.system("cls")
            break