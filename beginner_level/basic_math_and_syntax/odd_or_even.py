# Check if a number entered by the user is odd or even.

def odd_even(num):
    if num % 2 == 0:
        output = "Even"
    else:
        output = "Odd"
    return output

while True:
    try:
        number = int(input("Enter an Integer to check if it is Even or Odd : "))
        answer = odd_even(number)
    except ValueError:
        print("Number must be integer only.")
        continue

    print(f"{number} is {odd_even(number)}")

    query = input("Do you want to continue ? (y/n) ").strip().lower()
    if query == 'n':
        break