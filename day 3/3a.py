# Part 1: What is the sum of the priorities of those item types? [ 7737 ]

with open('3_data.txt', 'rt') as data:
    data_list = [line.strip() for line in data.readlines()]
for i in range(len(data_list)):
    line = data_list[i]
    data_list[i] = list([line[:len(line) // 2], line[len(line) // 2:]])

priorities = []
sumOfPriorities = 0

for item in data_list:
    priorities.append(list(set(item[0]) & set(item[1])))

for item in priorities:
    character = str(item[0])
    if character.islower():
        sumOfPriorities += (ord(character) - 96)
    else:
        sumOfPriorities += (ord(character) - 38)

print(sumOfPriorities)