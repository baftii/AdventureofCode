import re

with open('text.txt', 'r') as file:
    line_count = len(file.readlines())

with open('text.txt', 'r') as file:
    lines = file.readlines()


sum = 0

for i in range(0, line_count):
    counter = 0
    lines[i] = lines[i].split(':')
    sets = lines[i][1]
    sets = sets.split('|')
    winning = re.findall('\d+', sets[0])
    users = re.findall('\d+', sets[1])
    for j in range(0, len(winning)):
        for k in range(0, len(users)):
            if winning[j] == users[k]:
                counter += 1

    if counter > 0:
        sum += 2**(counter-1)

print(sum)
