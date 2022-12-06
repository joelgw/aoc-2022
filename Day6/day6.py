#!/bin/python3

with open("day6_input.txt") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip("[")

    # Part 1
    for i in range(len(line)):
        if len(set(line[i:i+4])) == 4:
            print (i + 4)
            break
    # Part 2    
    for i in range(len(line)):
        if len(set(line[i:i+14])) == 14:
            print (i + 14)
            break

