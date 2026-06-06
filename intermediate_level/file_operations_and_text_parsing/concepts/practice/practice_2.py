f = open("practice.txt", "r")
count = 0

for line in f.readlines():
    count += 1
    # if 'learning' in 'line'
    if line.find('learning') != -1:
        print(count)
        break