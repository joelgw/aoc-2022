#!/bin/python3

import sys

def main():
    with open("day8_input.txt") as file:
        lines = file.readlines()
    
    tree_grove = []
    
    for i in range(len(lines)):
        tree_grove.append(lines[i].strip())
    
    visible_trees = 0

    for i in range(len(tree_grove)):
        for j in range(len(tree_grove[i])):
            if check_north(i,j,tree_grove) or check_south(i,j,tree_grove) or check_east(i,j,tree_grove) or check_west(i,j,tree_grove):
                visible_trees += 1

    print(visible_trees)

    scores = []
    for i in range(len(tree_grove)):
        for j in range(len(tree_grove[i])):
            scores.append(scenic_north(i,j,tree_grove)*scenic_south(i,j,tree_grove)*scenic_east(i,j,tree_grove)*scenic_west(i,j,tree_grove))

    print(max(scores))
#Returns true if tree visible from the north
def check_north(i, j, tree_grove):
    if i == 0:
        return True
    for item in tree_grove[0:i]:
        if tree_grove[i][j] <= item[j]:
            return False
    return True
                        

#Returns true is tree visible from the south
def check_south(i, j, tree_grove):
    if i == len(tree_grove)-1:
        return True
    for item in tree_grove[i+1:len(tree_grove)]:
        if tree_grove[i][j] <= item[j]:
            return False
    return True

def check_east(i,j, tree_grove):
    if j == len(tree_grove[i])-1:
        return True
    for item in tree_grove[i][j+1:len(tree_grove[i])]:
        if tree_grove[i][j] <= item:
            return False
    return True

def check_west(i,j, tree_grove):
    if j == 0:
        return True
    for item in tree_grove[i][0:j]:
        if tree_grove[i][j] <= item:
            return False
    return True

def scenic_north(i,j,tree_grove):
    view = 1
    new_i = i
    if i == 0:
        return 0
    while tree_grove[i][j] > tree_grove[new_i-1][j] and new_i != 1:
        new_i -= 1
        view += 1
    return view

def scenic_south(i,j,tree_grove):
    view = 1
    new_i = i
    if i == len(tree_grove)-1:
        return 0
    while tree_grove[i][j] > tree_grove[new_i+1][j] and new_i != len(tree_grove)-2:
        new_i += 1
        view += 1
    return view

def scenic_east(i,j,tree_grove):
    view = 1
    new_j = j
    if j == len(tree_grove[i])-1:
        return 0
    while tree_grove[i][j] > tree_grove[i][new_j+1] and new_j != len(tree_grove[i])-2:
        new_j += 1
        view += 1
    return view

def scenic_west(i,j,tree_grove):
    view = 1
    new_j = j
    if j == 0:
        return 0
    while tree_grove[i][j] > tree_grove[i][new_j-1] and new_j != 1:
        new_j -= 1
        view += 1
    return view


if __name__ == "__main__":
    main()
