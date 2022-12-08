import anytree
from anytree import AnyNode, Node, RenderTree

with open("day7_input.txt") as file:
    lines = file.readlines()

dirs = {}
dirs_with_sums = {}
dirs["/"] = AnyNode(id="/")

working_dir = ""

for line in lines:
    if line.startswith("$ cd") and not line.endswith("..\n"):
        working_dir = line.split()[2]
    elif line.startswith("dir"):
        dir_line = line.split()
        if dir_line[1] not in dirs:
            dirs[dir_line[1]] = AnyNode(id=dir_line[1], parent=dirs[working_dir])
            #dirs[dirs.index(dir_line[1])] = AnyNode(id=dir_line[1], parent=dirs[dirs.index(working_dir)])
    elif not line.startswith("$"):
        dir_line = line.split()
        AnyNode(id=dir_line[1], parent=dirs[working_dir], file=True, file_size=int(dir_line[0]))

for pre, fill, node in RenderTree(dirs["/"]):
     print("%s%s" % (pre, node.id))

for item in dirs:
    print(item)
    running_sum = 0
    for node in anytree.search.findall_by_attr(dirs[item], name="file", value=True):
        running_sum += node.__dict__["file_size"]
    dirs_with_sums[item] = running_sum

#print(anytree.search.findall_by_attr(dirs["zcsnqjj"], name="file", value=True)[0].__dict__["file_size"])
#print(anytree.search.find(dirs["/"]), lambda node: node.id == "/")

print(dirs_with_sums)

part1_sum = 0

for item in dirs_with_sums:
    if dirs_with_sums[item] <= 100000:
        part1_sum += dirs_with_sums[item]

print(part1_sum)
#print(dirs["/"].get(id))
