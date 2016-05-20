# You have a matrix of size N * N with rows numbered through 1 to N from top to bottom
# and columns through 1 to N from left to right. It contains all values from 1 to N2,
# i.e. each value from 1 to N2 occurs exactly once in the matrix.

# Now, you start from the cell containing value 1, and from there visit the cell with value 2,
# and then from there visit the cell with value 3, and so on till you have visited cell
# containing the number N2. In a single step, you can move from a cell to one of its adjacent
# cells. Two cells are said to be adjacent to each other if they share an edge between them.

# Find out minimum number of steps required.

# For example, if matrix is
# 1 3
# 2 4

def create_matrix(n):
    base = []
    for x in range(0, n):
        line = []
        for i in range(0, n):
            line.append('x')
        base.append(line)
    return base

def print_matrix(matrix):
    for line in matrix:
        print line


# matrix = create_matrix(3)
# print_matrix(matrix)

position_map = []

def position_diff(pos_a, pos_b):
    a_x, a_y = pos_a
    b_x, b_y = pos_b
    return abs(a_x - b_x) + abs(a_y - b_y)

def calculate_total(position_map):
    total = 0
    for i in range(0, len(position_map)):
        if i < len(position_map) - 1:
            total += position_diff(position_map[i], position_map[i+1])
    return total

def main():
    test_cases = input()
    for test in range(0, test_cases):
        matrix_size = input()
        matrix = []
        position_map = [None] * matrix_size * matrix_size
        for x in range(0, matrix_size):
            matrix_row = []
            matrix_line = raw_input()
            matrix_line = matrix_line.split()
            for y in range(0, matrix_size):
                number = int(matrix_line[y])
                matrix_row.append(number)
                position_map[number - 1] = (x,y)
            matrix.append(matrix_row)
        print calculate_total(position_map)

main()
    
#Input:
#2
#2
#1 3
#2 4
#3
#1 7 9
#2 4 8
#3 6 5
#Output:
#4
#12
