with open('text.txt', 'r') as file:
    line_count = len(file.readlines())

with open('text.txt', 'r') as file:
    lines = file.readlines()


def text_to_number(text):
    number = 0
    if text == 'one':
        number = 1
    elif text == 'two':
        number = 2
    elif text == 'three':
        number = 3
    elif text == 'four':
        number = 4
    elif text == 'five':
        number = 5
    elif text == 'six':
        number = 6
    elif text == 'seven':
        number = 7
    elif text == 'eight':
        number = 8
    elif text == 'nine':
        number = 9
    return number

def number_to_number(number):
    number2 = 0
    if number == '1':
        number2 = 1
    elif number == '2':
        number2 = 2
    elif number == '3':
        number2 = 3
    elif number == '4':
        number2 = 4
    elif number == '5':
        number2 = 5
    elif number == '6':
        number2 = 6
    elif number == '7':
        number2 = 7
    elif number == '8':
        number2 = 8
    elif number == '9':
        number2 = 9
    return number2



sum = 0
for i in range(0, line_count):
    check_digit = 0
    max_digit = None
    min_digit = None
    digit_list = []
    digit_counter = -1
    min_digit_location = None
    max_digit_location = None
    check_digit_0 = 0
    check_digit_1 = 0
    check_text_1 = 0
    check_text_0 = 0
    check_text = False

    for j in range(0, len(lines[i])):
        # Digit check
        check_digit = lines[i][j].isdigit()

        if check_digit:
            digit_counter += 1
            digit_list.append([lines[i][j], j])

        if digit_counter == 0:
            min_digit_location = digit_list[0][1]

        # print(f'digit list is: {digit_list}')
        # print(f'digit counter is: {digit_counter}')

    if len(digit_list) == 1:
        check_digit_1 = 1
        min_digit = digit_list[0][0]

    elif len(digit_list) == 0:
        check_digit_0 = 1

    elif len(digit_list) > 1:
        max_digit = digit_list[digit_counter][0]
        max_digit_location = digit_list[digit_counter][1]
        min_digit = digit_list[0][0]

    if 'one' or 'two' or 'three' or 'four' or 'five' or 'six' or 'seven' or 'eight' or 'nine' in lines[i]:
        check_text = True
    index_number = []
    max_text = -1
    max_text_location = None
    min_text = 999999999999
    min_text_location = None

    if check_text:
        if 'one' in lines[i]:
            index_number.append([lines[i].find('one'), 'one'])

        for delta in range(0, lines[i].count('two')):
            if 'two' in lines[i]:
                index_number.append([lines[i].find('two'), 'two'])

        if 'three' in lines[i]:
            index_number.append([lines[i].find('three'), 'three'])

        if 'four' in lines[i]:
            index_number.append([lines[i].find('four'), 'four'])

        if 'five' in lines[i]:
            index_number.append([lines[i].find('five'), 'five'])

        if 'six' in lines[i]:
            index_number.append([lines[i].find('six'), 'six'])

        if 'seven' in lines[i]:
            index_number.append([lines[i].find('seven'), 'seven'])

        if 'eight' in lines[i]:
            index_number.append([lines[i].find('eight'), 'eight'])

        if 'nine' in lines[i]:
            index_number.append([lines[i].find('nine'), 'nine'])

        for k in range(0, len(index_number)):
            if len(index_number) == 1:
                min_text = index_number[k][0]
                min_text_location = k

            else:
                if max_text < index_number[k][0]:
                    max_text = index_number[k][0]
                    max_text_location = k

                if min_text > index_number[k][0]:
                    min_text = index_number[k][0]
                    min_text_location = k

        # if min_text_location <= 9:
        #    print(index_number[min_text_location][1])

        # if max_text_location >= 0 and (min_text_location != max_text_location):
        #    print(index_number[max_text_location][1])

    if min_digit_location != None and min_text_location != None:
        min_value = min(min_digit_location, min_text)

    elif min_digit_location == None and min_text_location != None:
        min_value = min_text

    elif min_digit_location != None and min_text_location == None:
        min_value = min_digit_location

    if min_text_location == None and max_text_location == None:
        min_text = 0
        max_text = 9999999
    if max_digit_location != None and max_text_location != None:
        max_value = max(max_digit_location, max_text)

    elif max_digit_location == None and max_text_location != None:
        if min_digit_location != None:
            max_value = max(max_text, min_digit_location)

        else:
            max_value = max_text

    elif max_digit_location != None and max_text_location == None:
        max_value = max(max_digit_location, min_text)

    else:
        max_value = max(min_digit_location, min_text)

    if len(index_number) == 1:
        check_text_1 = 1

    elif len(index_number) == 0:
        check_text_0 = 1

    if check_text_0 == 1 and check_digit_1 == 1:
        sum += number_to_number(min_digit) * 11

    elif check_text_1 == 1 and check_digit_0 == 1:
        sum += text_to_number(index_number[min_text_location][1]) * 11

    else:
        if min_value == min_digit_location and max_value == max_digit_location:
            sum += number_to_number(min_digit) * 10 + number_to_number(max_digit)

        elif min_value == min_digit_location and max_value == max_text:
            sum += number_to_number(min_digit) * 10 + text_to_number(index_number[max_text_location][1])

        elif min_value == min_digit_location and max_value == min_text:
            sum += number_to_number(min_digit) * 10 + text_to_number(index_number[min_text_location][1])

        elif min_value == min_text and max_value == max_digit_location:
            sum += text_to_number(index_number[min_text_location][1]) * 10 + number_to_number(max_digit)

        elif min_value == min_text and max_value == min_digit_location:
            sum += text_to_number(index_number[min_text_location][1]) * 10 + number_to_number(min_digit)

        elif min_value == min_text and max_value == max_text:
            sum += text_to_number(index_number[min_text_location][1]) * 10 + text_to_number(index_number[max_text_location][1])
print(index_number)
print(sum)

