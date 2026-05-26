# Exchange values using a temporary variable and Pythonic tuple unpacking

def swap_val(num1, num2):
    # Tuple unpacking
    num1, num2 = num2, num1
    return num1, num2

while True:
    val_1 = input("Enter first value : ").strip()
    val_2 = input("Enter second value : ").strip()

    print("Swapping happening...................................")
    swapped_val = swap_val(val_1, val_2)
    print(f"First value = {swapped_val[0]}\nSecond value = {swapped_val[1]}")

    query = input("Do you want to continue? (y/n) ").strip().lower()
    if query == 'n':
        break