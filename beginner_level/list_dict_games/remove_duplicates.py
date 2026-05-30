# Strip duplicate entries out of a list.

def remove_duplicates(list_num):
    new_list = []
    for i in list_num:
        if i not in new_list:
            new_list.append(i)

    return new_list

while True:
    print(f"Enter the elements of list :", end=" ")
    list_values = list(map(str, input().split()))
    print(f"List of unique elements : {remove_duplicates(list_values)}")

    query = input("Do you want to continue? (y/n) ").lower()
    if query == 'n':
        break