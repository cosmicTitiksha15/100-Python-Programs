# Check if a string reads the same forward and backward

def palindrome_checker(string_exp):
    if string_exp == string_exp[::-1]:
        return True
    return False

while True:
    entry = input("Enter the string you want to check palindrome for : ").strip()
    print(f"Is {entry} palindrome? = {palindrome_checker(entry)}")

    query = input("Do you want to continue ? (y/n) ").lower()
    if query == 'n':
        break