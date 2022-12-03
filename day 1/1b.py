# Part 2: How many Calories are those Elves carrying in total? [ 206289 ]

with open('1_data.txt', 'rt') as data:
    data_list = [line.strip() for line in data.readlines()]
for i in range(len(data_list)):
    data_list[i] = data_list[i].split()

sum = 0
numList = []
for line in data_list:
    if (len(line) < 1):
        numList.append(sum)
        sum = 0
    else:
        sum += int(line[0])

numList.sort(reverse=True)
print(numList[0] + numList[1] + numList[2])