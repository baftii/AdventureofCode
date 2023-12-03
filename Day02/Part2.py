import re

with open('text.txt', 'r') as file:
    line_count = len(file.readlines())

with open('text.txt', 'r') as file:
    lines = file.readlines()

sets = []
sum = 0

for i in range(0, line_count):
    sets = lines[i].split(':')
    set = sets[1].split(';')
    tries = []
    for j in range(0, len(set)):
        tries.append(set[j].split(','))

    max_red = 1
    max_green = 1
    max_blue = 1
    for k in range(0, len(tries)):
        for l in range(0, len(tries[k])):
            number = re.findall('\d+', tries[k][l])
            if tries[k][l].find('red') > 0:
                if int(number[0]) > max_red:
                    max_red = int(number[0])

            elif tries[k][l].find('green') > 0:
                if int(number[0]) > max_green:
                    max_green = int(number[0])

            elif tries[k][l].find('blue') > 0:
                if int(number[0]) > max_blue:
                    max_blue = int(number[0])

    sum += max_red * max_green * max_blue

print(sum)
