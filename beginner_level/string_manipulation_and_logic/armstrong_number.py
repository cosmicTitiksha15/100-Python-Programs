# Check if a number equals the sum of its own digits raised to the power of the number of digits. 
# 153 = 1**3 + 5**3 + 3**3

# Algorithm
# 1. count the number of digits in the number.
# 2. Raise each individual digit to the power of len(num).
# 3. Add all those powered values together.
# 4. If the total sum equals the original number, it is an Armstrong number.

def check_armstrong(num):
    number = num # Shallow Copy of original num, because when we compare values in later lines, num itself would be 0.
    output = False
    len_num = len(str(num))
    sum = 0
    for i in range(len_num):
        rem = num % 10
        sum += rem ** len_num
        num = num // 10
    if number == sum: # Comparing 'number' not 'num', bcz num = 0 after looping.
        output = True
    return output

while True:
    try:
        value = int(input("Enter a number to check if it is ARMSTRONG number: "))
        print(f"Is {value} Armstrong? : {check_armstrong(value)}")
    except ValueError:
        print("Entry should be an INTEGER.")
        continue

    query = input("Do you want to continue? (y/n) ").lower()
    if query == 'n':
        break