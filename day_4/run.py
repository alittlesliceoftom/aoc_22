
def get_data():
    with open('advent4.txt', 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

        # Print the number of lines
        print(len(lines))

        print(lines[0])
    return lines


def parse_input(lines):
    pairs = []
    # Iterate over the lines
    for line in lines:
        # Split the line on the ',' character to separate the assignments
        assignments = line.split(',')
        # Iterate over the assignments
        line_pairs = [map(int, assignment.split('-')) for assignment in assignments ]

        pairs.append(line_pairs)
    return pairs

def subsection(start1,end1,start2,end2):
    return (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1)

def overlap(start1,end1,start2,end2):
    return start1 <= end2 and start2 <= end1


# Define a function to compare the two assignments in each pair
def compare_assignments(pairs):
    # Create a counter variable to store the number of pairs where one assignment fully contains the other
    subsection_counter , overlap_counter= 0,0

    # Iterate over the pairs
    for i, [(start1, end1), (start2, end2)] in enumerate(pairs):
        # if start1 == start2 and end1 == end2):
        #     continue
        # # Check if one assignment fully contains the other
        if subsection(start1,end1,start2,end2):
            # If one assignment fully contains the other, increment the counter
            subsection_counter += 1
            # print([(start1, end1), (start2, end2)])
        if overlap(start1,end1,start2,end2):
            overlap_counter += 1
            
            


    # Return the counter
    return subsection_counter, overlap_counter


lines = get_data()
pairs = parse_input(lines)
result = compare_assignments(pairs)

print(result)
## answer was too high. 