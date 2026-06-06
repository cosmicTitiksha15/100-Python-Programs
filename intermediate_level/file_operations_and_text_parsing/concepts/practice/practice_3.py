# from a file containing numbers seperated by comma, print the count of even numbers

f = open("practice_a.txt", "r")
data = f.read()

list_nums = data.strip().split(",")

count = 0
for num in list_nums:
    if int(num) % 2 ==  0:
        count += 1

print(f"There are {count} even numbers in the list.")
