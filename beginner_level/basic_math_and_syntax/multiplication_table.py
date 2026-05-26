# Generate a clean multiplication table for any user-defined number.

def table_generator(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")


while True:
    try:
        number = int(input("Enter the number you want to print table of : "))
        table_generator(number)
    except ValueError:
        print("Number must be an INTEGER")
        continue

    query = input("Do you want to continue? (y/n) ").strip().lower()
    if query == 'n':
        break