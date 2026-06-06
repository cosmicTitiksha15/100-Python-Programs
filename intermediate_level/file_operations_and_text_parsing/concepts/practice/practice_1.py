with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")

with open("practice.txt", "r") as f:
    data = f.read()

# .replace(former, latter), replaces former substring into latter in strings
new_data = data.replace('Java', 'Python')
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

# Check if word "learning" exists:
with open("practice.txt", "r") as f:
    data = f.read()
    # .find(sub_string) in strings is used to find if some substring exists, returns the starting index of word or else -1, if not found.
    if data.find("learning") != -1:
        print("The word 'learning' exists in the file.")
    else:
        print("Does not exist")