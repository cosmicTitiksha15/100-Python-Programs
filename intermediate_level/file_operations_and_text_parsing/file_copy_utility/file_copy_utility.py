# Read content from one text file and write it to another

# Reads content from 'file.txt'
f = open('file.txt', 'r')
data = f.read()

# writes content into 'write_into.txt' from 'file.txt'
g = open('write_into.txt', 'w')
g.write(data)

# close both files
f.close()
g.close()