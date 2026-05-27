# Count the number of vowels in a user-provided string

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
def count_vowels(string_exp):
    count = 0
    for x in string_exp:
        if x in vowels:
            count += 1

    return count

while True:
    try:
        string_exp = input("Enter the String, you want to count No. of vowels in : ").strip()
        print(f"Number of vowels in '{string_exp}' is : {count_vowels(string_exp)}")
    except ValueError:
        print("Enter must be a STRING only.")
        continue

    query = input("Do you want to continue ? (y/n) ").lower()
    if query == 'n':
        break