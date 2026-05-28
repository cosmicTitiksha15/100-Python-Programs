# Find the maximum value in a user-defined list.

def largest_num(list_num):
    largest = 0
    for i in list_num:
        if i >= largest:
            largest = i
    return largest

while True:
    try:
        print("Enter the space-seperated numbers, out tof which you want to find the largest :", end = " ")
        list_num = list(map(float, input().split()))
        print(f"Largest number is : {largest_num(list_num)}")
    except ValueError:
        print("Entries should be a number. ")
        continue

    query = input("Do you want to continue? (y/n) ").lower()
    if query == 'n':
        break