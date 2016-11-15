# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

region = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
]

ans = [
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X'],
]

NONISLAND_FILL = '-'
ISLAND_PREFILL = 'O'
REST_FILL = 'X'

from collections import deque
def fill(region, row, col, fill_char):
    num_rows = len(region)
    num_cols = len(region[0])
    cur_fill = region[row][col]

    q = deque([(row,col)])
    while len(q):
        row, col = q.pop()
        cur_fill = region[row][col]
        if cur_fill != fill_char:
            region[row][col] = fill_char
            # do for surrounding
            choices = []
            if row - 1 >= 0:
                choices.append((row - 1, col))
            if row + 1 < num_rows:
                choices.append((row + 1, col))
            if col - 1 >= 0:
                choices.append((row, col - 1))
            if col + 1 < num_cols:
                choices.append((row, col + 1))
            for r, c in choices:
                if region[r][c] == cur_fill:
                    # fill(region, r, c, fill_char)
                    q.append((r,c))

def block_ni(region, r, c, num_rows, num_cols):
    if r == 0 or r == num_rows - 1 or c == 0 or c == num_cols - 1:
        if region[r][c] == ISLAND_PREFILL:
            fill(region, r, c, NONISLAND_FILL)

def fill_i(region, r, c, num_rows, num_cols):
    if region[r][c] == ISLAND_PREFILL:
        fill(region, r, c, REST_FILL)

def unblock_ni(region, r, c, num_rows, num_cols):
    if region[r][c] == NONISLAND_FILL:
        fill(region, r, c, ISLAND_PREFILL)
    
def for_each(region, function):
    num_rows = len(region)
    num_cols = len(region[0])
    for r in range(num_rows):
        for c in range(num_cols):
            function(region, r, c, num_rows, num_cols)

def main(region):
    if len(region) and len(region[0]):
        for_each(region, block_ni)
        for_each(region, fill_i)
        for_each(region, unblock_ni)

main(region)

