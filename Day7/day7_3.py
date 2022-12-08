#!/bin/python3

import anytree
from anytree import AnyNode, Node, RenderTree

import pprint
import time

dirs = []

with open("day7_input.txt") as file:
    lines = file.readlines()

root = AnyNode(id="/", directory=True)
working_node = root
working_line = 0

for line in lines:
    working_line += 1
    if line.startswith("$ cd /") and not line.endswith("..\n"):
        continue
    elif line.startswith("dir"):
        #check if current node already has the dir
        child_ids = []
        for item in working_node.children:
            child_ids.append(item.id)
        if line.split()[1] not in child_ids:
            AnyNode(id=line.split()[1], directory=True, parent=working_node)
    elif line.startswith("$ cd") and not line.endswith("..\n"):
        chdir = line.split()[2]
        #print(line)
        #print(working_node.children)
        for item in working_node.children:
            if item.id == chdir:
                working_node = item
        #working_node = anytree.search.find_by_attr(working_node, name="id", value=chdir, maxlevel=working_node.depth + 2)
    elif line.startswith("$ cd") and line.endswith("..\n"):
        working_node = working_node.parent
    elif not line.startswith("$"):
        dir_line = line.split()
        AnyNode(id=dir_line[1], parent=working_node, file=True, file_size=int(dir_line[0]))
    else:
        continue

for pre, fill, node in RenderTree(root):
     print("%s%s" % (pre, node.id))
    
sums = []
for item in anytree.search.findall_by_attr(root, name="directory", value=True):
    running_sum=0
    for node in anytree.search.findall_by_attr(item, name="file", value=True):
        running_sum += node.__dict__["file_size"]
    sums.append(running_sum)


part1_sum = 0
for item in sums:
    if item <= 100000:
        part1_sum += item

print("Part 1 Sum:")
print(part1_sum)

print("Part 2")

unused_space = 70000000 - sums[0]
space_needed = 30000000 - unused_space
sums.sort()

for item in sums:
    if space_needed - item <= 0:
        print(item)
        break
