# Matrix diagonal slice problem

# 9 3 2 4
# 8 6 1 2
# 5 5 6 7
# 1 2 8 4

# 9
# 3 8
# 2 6 5
# 4 1 5 1
# 2 6 2
# 7 8
# 4


def m_slice(coord, matrix):
    coordx = coord[0]
    coordy = coord[1]     

    x = coordx
    y = coordy
    
    m_height = len(matrix)
    if matrix[0]:
        m_width = len(matrix[0])
    
    ret_list = []
    
    while (x < m_height and y >= 0 and x >= 0 and y < m_width):
        ret_list.append(matrix[x][y])
        x += 1
        y -= 1
    return ret_list


def matrix_slice(matrix):
    m_height = len(matrix)
    if matrix[0]:
        m_width = len(matrix[0])
    
    for i, row in enumerate(matrix):
        if i == 0:
            for j, element in enumerate(row):
                print m_slice((i, j), matrix)
        else:
            print m_slice((i, m_width-1), matrix)

            
matrix = [[9, 3, 2, 4],
          [8, 6, 1, 2],
          [5, 5, 6, 7],
          [1, 2, 8, 4]]
   
# print m_slice((2,3), matrix)
matrix_slice(matrix)

matrix2 = [[9, 3, 2, 4],
          [8, 6, 1, 2],
          [5, 5, 6, 7],
          [8, 6, 1, 2],
          [5, 5, 6, 7],
          [1, 2, 8, 4]]
   
# print m_slice((1,3), matrix2)
matrix_slice(matrix2)

matrix3 = [[9, 3, 2, 4, 3, 5],
          [8, 6, 1, 2, 2, 4],
          [5, 5, 6, 7, 2, 1]]
   
# print m_slice((1,3), matrix2)
matrix_slice(matrix3)