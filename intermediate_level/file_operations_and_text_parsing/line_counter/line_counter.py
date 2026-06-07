# Count rows, words, and characters inside an external target '.txt' file.
f = open('file.txt', "r")
data = f.read()

# Counting number of rows
rows = data.split("\n")
print(f"Number of rows = {len(rows)}")

# Counting number of words
no_of_words = 0
for line in rows:
    words = line.strip().split(" ")
    no_of_words += len(words)
print(f"Total number of words = {no_of_words}")

# Total number of characters
no_of_characters = len(data.strip()) - (len(rows) - 1)
print(f"Number of characters = {no_of_characters}")