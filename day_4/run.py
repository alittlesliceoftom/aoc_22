
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
        for assignment in assignments:
            # Split the assignment on the '-' character to extract the start and end IDs
            start, end = assignment.split('-')

            # Convert the start and end IDs to integers
            start = int(start)
            end = int(end)

            pairs.append((start,end))
    return pairs
            
    

# # Define a function to compare the two assignments in each pair
# def compare_assignments(pairs):
#     # Create a counter variable to store the number of pairs where one assignment fully contains the other
#     counter = 0

#     # Iterate over the pairs
#     for start1, end1 in pairs:
#         for start2, end2 in pairs:
#             # Check if one assignment fully contains the other
#             if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
#                 # If one assignment fully contains the other, increment the counter
#                 counter += 1

#     # Return the counter
#     return counter

# Define a function to compare the two assignments in each pair
def compare_assignments(pairs):
    # Create a counter variable to store the number of pairs where one assignment fully contains the other
    counter = 0

    # Iterate over the pairs
    for i, (start1, end1) in enumerate(pairs):
        for j, (start2, end2) in enumerate(pairs):
            # Skip pairs that have already been compared
            # if i >= j:
            if i>= j or (start1 == start2 and end1 == end2):
                continue
            # Check if one assignment fully contains the other
            if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
                # If one assignment fully contains the other, increment the counter
                counter += 1

    # Return the counter
    return counter


lines = get_data()
pairs = parse_input(lines)
result = compare_assignments(pairs)

print(result)
## answer was too high. 