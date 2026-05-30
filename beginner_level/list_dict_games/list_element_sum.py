# Calculate the sum of all numerical items in a list.

def calc_sum(list_num):
    return sum(list_num)

while True:
    try:
        print("Enter the list of numbers, you want to print sum of :", end=" ")
        list_values = list(map(float, input().split()))
        print(f"Sum of all elements of list {list_values}: {calc_sum(list_values)}")
    except ValueError:
        print("Elements of list should all be NUMBERS.")
        continue

    query = input("Do you want to continue? (y/n) ").lower()
    if query == 'n':
        break