#!/bin/python3

import pprint

dir_dict = {}

with open("day7_input.txt") as file:
    lines = file.readlines()

for i in range(len(lines)):
    if str(lines[i]).startswith("$ cd"):
        cd = lines[i].split()
        if (str(cd[2]) != ".."):
            dir_dict.update({cd[2]:[]})
            # Get all files under that dir and add them to an array in the dir_dict
            j = 1
            while not str(lines[i + j]).startswith("$ cd"):
                j += 1
                if i + j == len(lines):
                    break
                ls = lines[i + j].split()
                try:
                    dir_dict[cd[2]].append(int(ls[0]))
                except:
                    continue

pprint.pprint(dir_dict)


lt100k_sum = 0

for item in dir_dict:
    print(dir_dict[item])
    if sum(dir_dict[item]) <= 100000:
        lt100k_sum += sum(dir_dict[item])

print(lt100k_sum)

dir_count = 0
for line in lines:
    if line.startswith("dir"):
        dir_count += 1

print(dir_count)
print(len(dir_dict))
