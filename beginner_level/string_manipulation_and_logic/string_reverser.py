# Take a string and print it backwards.

def string_reverser(string_exp):
    reversed_str = string_exp[::-1]
    return reversed_str

while True:
    string_exp = input("Enter the String you want to reverse : ").strip()
    print(f"Reversed string = {string_reverser(string_exp)}")

    query = input("Do you want to continue ? (y/n) ").lower()
    if query == 'n':
        break