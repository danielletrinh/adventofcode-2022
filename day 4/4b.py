# Part 2: In how many assignment pairs do the ranges overlap? [ 938 ]

with open('4_data.txt', 'rt') as data:
    data_list = [line.strip() for line in data.readlines()]
for i in range(len(data_list)):
    data_list[i] = data_list[i].split(',')
    data_list[i][0] = list(map(int, data_list[i][0].split('-')))
    data_list[i][1] = list(map(int, data_list[i][1].split('-')))

total = 0
for item in data_list:
    if item[0][0] in range(item[1][0], item[1][1] + 1) or item[0][1] in range(item[1][0], item[1][1] + 1):
        total += 1
    elif item[1][0] in range(item[0][0], item[0][1] + 1) or item[1][1] in range(item[0][0], item[0][1] + 1):
        total += 1

print(total)