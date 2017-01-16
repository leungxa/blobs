import math

ORIGIN = 50
RADIUS = 50
FILL_WHITE = 'white'
FILL_BLACK = 'black'

def get_coord_quad(X, Y):
  coord_quad = 0
  if X > ORIGIN:
    coord_quad = 1 if Y > ORIGIN else 2
  else:
    coord_quad = 4 if Y > ORIGIN else 3
  return coord_quad

def get_dist_from_origin_in_float(X, Y):
  return math.sqrt( (X - ORIGIN)**2 + (Y - ORIGIN)**2 )

def get_point_color(percent, X, Y):
  if percent == 0:
    return FILL_WHITE

  dist = get_dist_from_origin_in_float(X, Y)

  if dist <= RADIUS:
    if percent == 100:
      return FILL_BLACK
  
    else:
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
      
# print get_point_color(100, 100, 100)
# print get_point_color(50, 51, 20)
# print get_point_color(75, 20, 49)

def test_get_point_color():
  # cases = [(0, 55, 55),
  #   (12, 55, 55),
  #   (13, 55, 55),
  #   (99, 99, 99),
  #   (87, 20, 40)]
    
  assert(get_point_color(0, 55, 55) == FILL_WHITE)
  assert(get_point_color(12, 55, 55) == FILL_WHITE)
  assert(get_point_color(13, 55, 55) == FILL_BLACK)
  assert(get_point_color(99, 99, 99) == FILL_WHITE)
  assert(get_point_color(87, 20, 40) == FILL_BLACK)
  
test_get_point_color()

