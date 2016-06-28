def check_num(n):
    while(n > 0):
        digit = n % 10
        if digit not in [0,1,4,9]:
            return False
        n = n / 10
    return True

print check_num(38809)


def test_check_num():
    for x in range(0, 3165):
        print 'check', x, check_num(x)

        
def create_squares():
    storage = []
    squares_count = 0
    for x in range(1,10*10*10*10*10+1):
        new_number = x*x
        # check number for 0 1 4 9
        if check_num(new_number):
            storage.append(new_number)
            squares_count += 1
    return storage, squares_count

proper_squares, len_squares = create_squares()

print len_squares
print ''
#test
#for x in range(0,50):
#    print x, proper_squares[x]
