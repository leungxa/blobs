import math

class Matrix:
  FILL_WHITE = 0
  FILL_BLACK = 1

  def __init__(self, width=10, height=10):
    self.coords = []
    for x in range(height):
      row = [Matrix.FILL_WHITE] * width
      self.coords.append(row)

  def print_m(self):
    for row in self.coords:
      print row
    print "============ END MATRIX ==============="

  def get_dist_from_origin_in_float(self, r, c):
    origin = float(len(self.coords) - 1) / 2
    dist = math.sqrt( (r - origin)**2 + (c - origin)**2 )
    return dist

  def draw_full_circle(self):
    radius = len(self.coords) / 2   # deal with odd numbers later
    for i,row in enumerate(self.coords):
      for j,value in enumerate(row):
        distance = self.get_dist_from_origin_in_float(i,j)
        # print distance
        if distance <= radius:
          self.coords[i][j] = Matrix.FILL_BLACK
  
  def clear(self):
    for i,row in enumerate(self.coords):
      for j,value in enumerate(row):
        self.coords[i][j] = Matrix.FILL_WHITE
        

# m = Matrix()
# m.draw_full_circle()
# m.print_m()
# m.clear()
# m.print_m()


# def loader(percent):
#   matrix = create_matrix(width=100, height=100)
#   print_m(matrix)
  
# def draw_full_circle():
#   radius = 50
#   matrix = create_matrix(width=radius*2, height=radius*2)
#   for row in matrix:
#     for point in row:
#       distance = get_dist_from_origin()
      

# loader(25)

ORIGIN = 50
RADIUS = 50
def get_coord_quad(X, Y):
  coord_quad = 0
  if x > ORIGIN:
    coord_quad = 1 if y > ORIGIN else 2
  else:
    coord_quad = 4 if y > ORIGIN else 3
  return coord_quad

def get_dist_from_origin_in_float(X, Y):
  dist = math.sqrt( (X - ORIGIN)**2 + (Y - ORIGIN)**2 )
  return dist

def get_point_color(percent, X, Y):
  FILL_WHITE = 'white'
  FILL_BLACK = 'black'
  if percent == 0:
    return FILL_WHITE
  if percent == 100:
    return FILL_BLACK

  dist = get_dist_from_origin_in_float(X, Y)
  if dist <= RADIUS:
    coord_quad = get_coord_quad(X, Y)
    angle_quad = percent / 25
    if coord_quad < angle_quad:
      return FILL_BLACK
    elif coord_quad > angle_quad:
      return FILL_WHITE
    elif percent % 25 == 0 and coord_quad == angle_quad:
      return FILL_BLACK
    else:
      deg_angle = percent % 25 * 3.6
      rad_angle = math.radians(degree)
      if angle_quad == 1:
        x = RADIUS * math.sin(rad_angle)
        y = RADIUS * math.cos(rad_angle)
  else:
    return FILL_WHITE
      
      
print get_point_color(100, 100, 100)

