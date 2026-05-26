# Performs addition, subtraction, multiplication, and division based on user input.

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Divisor can not be 0!")
        

# Used loops so as one can try calculating multiple times.
while True:
    # Used try-except block to take 'number' entries
    try :
        num1 = float(input("Enter first number : "))
        
        num2 = float(input("Enter the second number : "))
    except ValueError:
        print("Entries must be numbers.")
        continue

    # Used .strip() function so as to remove trailing and leading whitespaces in operation symbol
    operation = input("Enter the operation(+,-,*,/) : ").strip()

    if operation == '+':
        print(addition(num1, num2))
    elif operation == '-':
        print(subtraction(num1, num2))
    elif operation == '*':
        print(multiplication(num1, num2))
    elif operation == '/':
        print(division(num1, num2))
    

    query = input("Do you want to continue ? (y/n) : ").lower()
    if query == 'n':
        break