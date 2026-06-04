# Find intersecting values between two lists

def common_elements_finder(list_1, list_2):
    common_list = []
    for i in list_1:
        if i in list_2:
            common_list.append(i)
    return common_list


list_1 = list(map(str, input("Enter elements of first list separated by space: ").split()))
list_2 = list(map(str, input("Enter elements of second list separated by space: ").split()))
result = common_elements_finder(list_1, list_2)
print("Common elements between the two lists are:", result)