def maxDifference(a):
    if len(a) == 1:
        return 0
    max_diff = -1
    v_min = a[0]
    v_max = None
    for i, num in enumerate(a):
        if i > 0:
            if num < v_min:
                if v_max and v_max - v_min > max_diff:
                    max_diff = v_max - v_min
                v_min = num
                v_max = None
            else:
                if num >= v_min:
                    if v_max is None:
                        v_max = num
                    elif num >= v_max:
                        v_max = num
                    if v_max - v_min > max_diff:
                        max_diff = v_max - v_min
    
    return max_diff

print maxDifference([3,10,3,3])
print maxDifference([0,1,0,1])
print maxDifference([10,9,8,6])
print maxDifference([-1,10,-10,6])
