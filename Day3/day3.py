def main():
    priority_score = 0

    with open('rucksack.txt') as f:
        rucksacks = f.readlines()

    for sack in rucksacks:
        sack_size = len(sack) - 1
        # Check if item in the first half is in the second half
        for item in sack[0 : int(sack_size/2)]:
            if item in sack[int(sack_size/2):sack_size + 1]:
                # If the item is there, add it to the priority score then break to the next rucksack
                priority_score += (ord(item) - 96) if item.islower() else (ord(item) - 38)
                break

    print("Part 1 Answer: " + str(priority_score))


    rucksack_num = 0
    priority_score = 0
    
    for sack in rucksacks:
        rucksack_num += 1
        # Only run the checker starting on every third elf ex. 1, 4, 7...
        if rucksack_num % 3 != 1:
            continue
        for item in sack:
            #Check if the item is in the next rucksack
            if item in rucksacks[rucksack_num]:
                #Check if it's in the thrird rucksack
                if item in rucksacks[rucksack_num + 1]:
                    #If item is in all three add it's priority
                    priority_score += (ord(item) - 96) if item.islower() else (ord(item) - 38)
                    break
                else:
                    continue
            else:
                continue

    print("Part two answer: " + str(priority_score))


if __name__ == "__main__":
    main()
