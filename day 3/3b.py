# Part 2: What is the sum of the priorities of those item types? [ 2697 ]

with open('3_data.txt', 'rt') as data:
    data_list = [line.strip() for line in data.readlines()]

priorities = []
sumOfPriorities = 0

i = 0
while i < (len(data_list) - 2):
    priorities.append(list(set(data_list[i]) & set(data_list[i+1]) & set(data_list[i+2])))
    i += 3

for item in priorities:
    character = str(item[0])
    if character.islower():
        sumOfPriorities += (ord(character) - 96)
    else:
        sumOfPriorities += (ord(character) - 38)

print(sumOfPriorities)