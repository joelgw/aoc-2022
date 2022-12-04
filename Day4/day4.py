import re

def main():
    with open('cleaning_assignments.txt') as f:
        clean_assign = f.readlines()
    
    in_range_duplicates = 0

    for line in clean_assign:
        # Split the line into an array 0-1, 2-3 give the ranges
        assignments = re.split('-|,|\n', line)
        # Check if first two numbers are in the range made up by the second pair
        if (
                int(assignments[0]) in range(int(assignments[2]), int(assignments[3])+1) and 
                int(assignments[1]) in range(int(assignments[2]), int(assignments[3])+1)
           ):
            in_range_duplicates += 1

            # Need a continue to not double count if there are duplicate numbers
            continue

        # Check if second two numbers are in the range made up by the first pair
        if (
                int(assignments[2]) in range(int(assignments[0]), int(assignments[1])+1) and
                int(assignments[3]) in range(int(assignments[0]), int(assignments[1])+1)
           ):
            in_range_duplicates += 1
            
    print("Answer 1: " + str(in_range_duplicates))


    overlap = 0

    for line in clean_assign:
        # Split the line into an array 0-1, 2-3 give the ranges
        assignments = re.split('-|,|\n', line)

        #Check middle two numbers, then outer two numbers
        if (
                int(assignments[1]) >= int(assignments[2]) and
                int(assignments[0]) <= int(assignments[3])
            ):
            overlap += 1
            continue

       # if (
       #         int(assignments[0]) <= int(assignments[3]) and
       #         int(assignments[0]) >= int(assignments[2])
       #    ):
       #     print(assignments)
       #     overlap += 1
        
    print(overlap)
if __name__ == "__main__":
    main()
