import copy

class ElfBoat:
    def __init__(self):
        self.all_stacks = []
        self.all_stacks_copy = []
        self.first_line = True
    # Read the file and build the stacks. The stacks will be LIFO, but the file is reading
    # them starting with the last elements
    def build_stacks(self, line):
        # Build the boat with the correct number of stacks. The amount of chars divided by 4
        # this will only run when the first line is input, after that the stacks are built
        if self.first_line:
            for i in range(0, int(len(line)/4)):
                self.all_stacks.append([])
            
            self.first_line = False

        # The stack values will be on every fourth line starting at 2 '[' 'A' ']' ' '
        for i in range(0, len(line) + 1):
            if (i % 4 == 1) and (line[i] != ' '):
                self.all_stacks[int(i/4)].insert(0, line[i])

        # Make a working copy of initial configuration for part 2
        self.all_stacks_copy = copy.deepcopy(self.all_stacks)

    # Get the top values of each stack returned as a string
    def peek_stacks(self, problem):
        ret = ''
        if problem == 1: 
            stacks = self.all_stacks
        else:
            stacks = self.all_stacks_copy
        for stack in stacks:
            ret += str(stack[-1])
        return ret

    # Part 1, simple pop and push from stack to stack
    def move_crate(self, instruction):
        ins = instruction.split()
        for i in range(0, int(ins[1])):
            self.all_stacks[int(ins[5])-1].append(self.all_stacks[int(ins[3])-1].pop())

    # Part 2, used python's negative indexing to get last few elements of stacks
    def move_multi_crate(self, instruction):
        ins = instruction.split()
        to_add = self.all_stacks_copy[int(ins[3])-1][int("-" + ins[1]):]
        del self.all_stacks_copy[int(ins[3])-1][int("-" + ins[1]):]
        self.all_stacks_copy[int(ins[5])-1].extend(to_add)

def main():
    with open('day5_input.txt') as file:
        lines = file.readlines()

    boat = ElfBoat()

    for line in lines:
        if line.startswith(' 1'):
            break
        boat.build_stacks(line)

    #Sort them for Problem 1
    for line in lines:
        if line.startswith('move'):
            boat.move_crate(line)

    #Sort them for Problem 2
    for line in lines:
        if line.startswith('move'):
            boat.move_multi_crate(line)

    print(boat.peek_stacks(1))
    print(boat.peek_stacks(2))

if __name__ == "__main__":
    main()
