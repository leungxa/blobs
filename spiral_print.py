array = [
    [ 1,  2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7]
]

def spiral_print(array):
    min_row, min_col = 0, 0
    max_row = len(array)
    max_col = len(array[0])
    
    cur_row, cur_col = 0, 0
    while min_row < max_row and min_col < max_col:
        # print right
        if cur_row < max_row and cur_row >= min_row:
            for i in range(min_col, max_col):
                cur_col = i
                print array[cur_row][cur_col]
            min_row += 1
        # print down
        if cur_col < max_col and cur_col >= min_col:
            for i in range(min_row, max_row):
                cur_row = i
                print array[cur_row][cur_col]
            max_col -= 1
        # print left
        if cur_row < max_row and cur_row >= min_row:
            for i in list(reversed(range(min_col, max_col))):
                cur_col = i
                print array[cur_row][cur_col]
            max_row -= 1
        # print up
        if cur_col < max_col and cur_col >= min_col:
            for i in list(reversed(range(min_row, max_row))):
                cur_row = i
                print array[cur_row][cur_col]
            min_col += 1
    return



array = [
    [ 1,  2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7],
    [ 1,  2,  3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10,  9,  8, 7]
]

spiral_print(array)
