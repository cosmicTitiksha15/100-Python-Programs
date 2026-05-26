# Find the factorial of a number using loops.

def factorial(num):
    factorial_val = 1
    if num == 0:
        factorial_val = 1
    elif num < 0:
        return "Does not exist."
    for i in range(1, num+1):
        factorial_val *= i

    return factorial_val

while True:
    try:
        value = int(input("Enter the number you want to print factorial of : "))
        print(f"Factorial of {value} = {factorial(value)}")
    except ValueError:
        print("Value must be an integer.")
        continue

    query = input("Do you want to continue? (y/n) ").strip().lower()
    if query == 'n':
        break
