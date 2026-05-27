#  Generate the first $N$ numbers in the Fibonacci sequence.

def fibonacci_sequence(num):
    list_fibonacci = [0, 1]
    for i in range(num-2):
        output = list_fibonacci[-1] + list_fibonacci[-2]
        list_fibonacci.append(output)
    return list_fibonacci

while True:
    try: 
        entry = int(input("How many terms of Fibonacci sequence is wanted ? : "))
        print(f"{entry} terms of Fibonacci sequence are = {fibonacci_sequence(entry)}")
    except ValueError:
        print("Number of Terms must be an Integer. ")
        continue

    query = input("Do you want to continue? (y/n) ").lower()
    if query == 'n':
        break
