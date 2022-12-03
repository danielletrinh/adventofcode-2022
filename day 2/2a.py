# Part 1: What would your total score be if everything goes exactly according to your strategy guide? [ 11150 ]

with open('2_data.txt', 'rt') as data:
    data_list = [line.strip() for line in data.readlines()]
for i in range(len(data_list)):
    data_list[i] = data_list[i].split()

totalScore = 0

for item in data_list:
    if item[1] == 'X':
        totalScore += 1
        item[1] = 'A'
    elif item[1] == 'Y':
        totalScore += 2
        item[1] = 'B'
    else:
        totalScore += 3
        item[1] = 'C'

    if item[0] == item[1]:
        totalScore += 3
    elif item[0] == 'A' and item[1] == 'B':
        totalScore += 6
    elif item[0] == 'B' and item[1] == 'C':
        totalScore += 6
    elif item[0] == 'C' and item[1] == 'A':
        totalScore += 6

print(totalScore)