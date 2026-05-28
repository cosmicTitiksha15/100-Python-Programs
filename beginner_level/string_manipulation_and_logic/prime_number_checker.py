#  Verify if a given number is prime.

def check_prime(num):
    is_prime = True
    if num <= 1:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return is_prime

while True:
    try:
        number = int(input("Enter the number to check if it is prime : "))
        print(f"Is {number} prime? = {check_prime(number)}")
    except ValueError:
        print("Number must be an Integer.")
        continue

    query = input("Do you want to continue? (y/n) ").lower()
    if query == 'n':
        break