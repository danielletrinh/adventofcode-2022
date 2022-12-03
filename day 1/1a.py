# Part 1: How many total Calories is that Elf carrying? [ 71023 ]

with open('1_data.txt', 'rt') as data:
    data_list = [line.strip() for line in data.readlines()]
for i in range(len(data_list)):
    data_list[i] = data_list[i].split()

largestNum = 0
sum = 0
for line in data_list:
    if (len(line) < 1):
        if (sum > largestNum):
            largestNum = sum
        sum = 0
    else:
        sum += int(line[0])

print(largestNum)