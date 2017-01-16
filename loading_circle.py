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

def get_percent_quad(percent):
  count = 25
  quad = 1
  while (count <= 100):
    if percent < count:
      return quad
    else:
      count += 25
      quad += 1
  return 4

def test_get_percent_quad():
  assert get_percent_quad(0) == 1
  assert get_percent_quad(15) == 1
  assert get_percent_quad(25) == 2
  assert get_percent_quad(50) == 3
  assert get_percent_quad(51) == 3
  assert get_percent_quad(66) == 3
  assert get_percent_quad(100) == 4

test_get_percent_quad()

def get_dist_from_origin_in_float(X, Y):
  return math.sqrt( (X - ORIGIN)**2 + (Y - ORIGIN)**2 )

# print get_percent_quad(25)

# def get_circle_coord(percent):
#   angle_quad = get_percent_quad(percent)
#   deg_angle = percent % 25 * 3.6
#   rad_angle = math.radians(deg_angle)
  
#   x_d = RADIUS * math.sin(rad_angle)
#   y_d = RADIUS * math.cos(rad_angle)

#   if angle_quad == 2:
#     x_d, y_d = y_d, x_d
#   if angle_quad == 3:
#     x_d, y_d = -x_d, -y_d
#   if angle_quad == 4:
#     x_d, y_d = -y_d, x_d
    
#   x_coord = ORIGIN + x_d
#   y_coord = ORIGIN + y_d
#   return (int(x_coord), int(y_coord))
  
# def test_get_circle_coord():
#   assert(get_circle_coord(0) == (50, 100))
#   assert(get_circle_coord(10) == (79, 90))
#   assert(get_circle_coord(25) == (100, 50))
#   assert(get_circle_coord(60) == (20, 9))
#   assert(get_circle_coord(99) == (46, 99))

# test_get_circle_coord()

def percent_to_degrees(percent):
  return float(percent) / 100 * 360

def coord_to_angle(X, Y):
  x_d = X - ORIGIN
  y_d = Y - ORIGIN
  
  d = get_dist_from_origin_in_float(X, Y)
  
  angle_quad = get_coord_quad(X, Y)
  if angle_quad == 2:
    x_d, y_d = y_d, x_d
  if angle_quad == 3:
    x_d, y_d = -x_d, -y_d
  if angle_quad == 4:
    x_d, y_d = -y_d, x_d
  
  deg_angle = math.degrees(math.asin(float(x_d) / d))
  total = math.fabs(deg_angle) + (angle_quad - 1) * 90
  return total

def test_coord_to_angle():
  assert(int(round(coord_to_angle(55, 55))) == 45)
  assert(int(round(coord_to_angle(20, 30))) == 236)
  assert(int(round(coord_to_angle(40, 70))) == 333)
  
test_coord_to_angle()  


def get_point_color(percent, X, Y):
  if percent == 0:
    return FILL_WHITE

  dist = get_dist_from_origin_in_float(X, Y)

  if dist <= RADIUS:
    if percent == 100:
      return FILL_BLACK

    else:
      coord_quad = get_coord_quad(X, Y)
      angle_quad = get_percent_quad(percent)
  
      if coord_quad < angle_quad:
        return FILL_BLACK
      elif coord_quad > angle_quad:
        return FILL_WHITE
      elif percent % 25 == 0 and coord_quad == angle_quad:
        return FILL_BLACK
      else:
        percent_angle = percent_to_degrees(percent)
        coord_angle = coord_to_angle(X, Y)
        print percent_angle, coord_angle
        filled = percent_angle > coord_angle
        return FILL_BLACK if filled else FILL_WHITE
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
    
  # assert(get_point_color(0, 55, 55) == FILL_WHITE)
  # assert(get_point_color(12, 55, 55) == FILL_WHITE)
  # assert(get_point_color(13, 55, 55) == FILL_BLACK)
  # assert(get_point_color(99, 99, 99) == FILL_WHITE)
  # assert(get_point_color(87, 20, 40) == FILL_BLACK)
  
  
  print get_point_color(20, 46, 39)
  print get_point_color(69, 44, 38)
  print get_point_color(3, 82, 67)
  print get_point_color(54, 8, 62)

  
  
test_get_point_color()

# def handle_input():
#   i = raw_input()
#   count = 1
#   for x in range(int(i)):
#     case = raw_input()
#     case = [int(c) for c in case.split(' ')]
#     color = get_point_color(case[0], case[1], case[2])
#     print 'Case #{}: {}'.format(count, color)
#     count += 1
    
# handle_input()
