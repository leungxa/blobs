image = [
  [1, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 1, 1],
  [1, 0, 1, 0, 0, 1, 1],
  [1, 1, 1, 0, 0, 1, 1],
  [1, 1, 1, 1, 1, 1, 0],
]

def get_coords(image, row, col, seen_rect):
    coords = []
    original_col = col
    while(row < len(image)):
        while(col < len(image[0])):
            curr = (row, col)
            if image[row][col] == 0 and curr not in seen_rect:
                coords.append(curr)
            if image[row][col] == 1:
                break
            col += 1
        row += 1
        col = original_col
        if row < len(image):
            if image[row][col] == 1:
                break
    return coords
              
              
def rect(image):
    seen_rect = set()
    rect_coords = []
    n_rows = len(image)
    n_cols = len(image[0])
    for i in range(n_rows):
        for j in range(n_cols):
            if image[i][j] == 0:
                coords = get_coords(image, i, j, seen_rect)
                if coords:
                    for coord in coords:
                        seen_rect.add(coord)
                    rect_coords.append((coords[0], coords[-1]))
    return rect_coords

print rect(image)
