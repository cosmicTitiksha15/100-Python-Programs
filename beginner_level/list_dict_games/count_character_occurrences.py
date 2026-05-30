# Use a dictionary to count how often each character appears in a string. 

def count_occurrences(str_of_chars):
    dict_of_str = dict()
    for i in str_of_chars:
        if i != " ":
            if i in dict_of_str:
                dict_of_str[i] += 1
            else:
                dict_of_str[i] = 1
    return dict_of_str


while True:
    string_chars = input("Enter the string : ").lower()
    print(f"Dictionary of count of characters : {count_occurrences(string_chars)}")

    query = input("Do you want to continue? (y/n) ").lower()
    if query == 'n':
        break