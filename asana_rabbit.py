import math

def get_max_value_coord(garden, coords):
    mapm = {}
    for (r, c) in coords:
        mapm[garden[r][c]] = (r, c)
    maxm = max(mapm.keys())
    max_coord = mapm[maxm]
    return max_coord, maxm

def get_start_pos(garden):
    start_row, start_col = None, None
    num_rows = len(garden)
    num_cols = len(garden[0])
    # get middle or biggest count
    if (num_rows % 2 != 0):
        start_row = int(math.floor(float(num_rows) / 2))
    if (num_cols % 2 != 0):
        start_col = int(math.floor(float(num_cols) / 2))
    if start_row is not None and start_col is not None:
        return start_row, start_col
    else:
        center_row = float(num_rows) / 2
        center_col = float(num_cols) / 2
        if start_row is None and start_col is None:
            row1 = int(math.floor(center_row)) - 1
            row2 = row1 + 1
            col1 = int(math.floor(center_col)) - 1
            col2 = col1 + 1
            choices =  [(row1, col1), (row1, col2), (row2, col1), (row2, col2)]
            coord, val = get_max_value_coord(garden, choices)
            return coord
        if start_row is not None:
            # find start_col
            col1 = int(math.floor(center_col)) - 1
            col2 = col1 + 1
            choices = [(start_row, col1), (start_row, col2)]
            coord, val =  get_max_value_coord(garden, choices)
            return coord
        if start_col is not None:
            # find start_row
            row1 = int(math.floor(center_row)) - 1
            row2 = row1 + 1
            choices = [(row1, start_col), (row2, start_col)]
            coord, val = get_max_value_coord(garden, choices)
            return coord
    return start_row, start_col

def eat(garden, row, col):
    # eat current
    # figure out which square to eat next
    # check up down left right
    # move to next square
    num_rows = len(garden)
    num_cols = len(garden[0])
    count = 0
    while True:
        count += garden[row][col]
        garden[row][col] = 0
        choices = []
        if row + 1 < num_rows:
            choices.append((row + 1, col))
        if row - 1 >= 0:
            choices.append((row - 1, col))
        if col + 1 < num_cols:
            choices.append((row, col + 1))
        if col - 1 >= 0:
            choices.append((row, col - 1))
        coord, val = get_max_value_coord(garden, choices)
        if val != 0:
            row = coord[0]
            col = coord[1]
        else:
            return count

garden = [
    [5, 7, 8, 6, 3],
    [0, 0, 7, 0, 4],
    [4, 6, 3, 4, 9],
    [3, 1, 0, 5, 8],
]
        
def start_rabbit(garden):
    start_row, start_col = get_start_pos(garden)
    return eat(garden, start_row, start_col)

print start_rabbit(garden)

    
