def maxDifference(a):
    if len(a) == 1:
        return 0
    max_diff = -1
    i_min = 0
    v_min = a[0]
    i_max = None
    v_max = None
    for i, num in enumerate(a):
        if i > 0:
            if num < v_min:
                if v_max and v_max - v_min > max_diff:
                    max_diff = v_max - v_min
                v_min = num
                i_min = i
                i_max = None
                v_max = None
            else:
                if num >= v_min:
                    if i_max is None and v_max is None:
                        i_max = i
                        v_max = num
                    elif num >= v_max:
                            i_max = i
                            v_max = num
                    if v_max - v_min > max_diff:
                        max_diff = v_max - v_min
    
    return max_diff

print maxDifference([3,10,3,3])
print maxDifference([0,1,0,1])
print maxDifference([10,9,8,6])
print maxDifference([-1,10,-10,6])
