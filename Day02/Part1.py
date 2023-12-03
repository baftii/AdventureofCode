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

    red_check = False
    green_check = False
    blue_check = False
    for k in range(0, len(tries)):
        for l in range(0, len(tries[k])):
            number = re.findall('\d+', tries[k][l])
            if tries[k][l].find('red') > 0:
                if int(number[0]) > 12:
                    red_check = True
                    break

            elif tries[k][l].find('green') > 0:
                if int(number[0]) > 13:
                    green_check = True
                    break

            elif tries[k][l].find('blue') > 0:
                if int(number[0]) > 14:
                    blue_check = True
                    break

        if red_check != False and blue_check != False and green_check != False:
            break

    if red_check == False and blue_check == False and green_check == False:
        sum += (i+1)

print(sum)
