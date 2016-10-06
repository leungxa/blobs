def maxProduct(l):
    largest_p = None
    cur_p = 1
    for x in l:
        cur_p = max(x ,cur_p * x)
        if cur_p >= largest_p:
            largest_p = cur_p
        else:
            cur_p = 1
    return largest_p

print maxProduct([0,2])


def largest_prod_subarray(l):
    largest = [0, 0]
    largest_p = None
    cur_substr = [0, 0]
    cur_p = 1
    for i,x in enumerate(l):
        cur_substr[1] = i
        if x >= cur_p * x:
            cur_substr[0] = i
        cur_p = max(x, cur_p * x)
        if cur_p >= largest_p:
            largest[0], largest[1] = cur_substr[0], cur_substr[1]
            largest_p = cur_p
        else:
            cur = [i+1, i+1]
            cur_p = 1
    return l[largest[0]:largest[1]+1]

print largest_prod_subarray([2,3,-2,4])
print largest_prod_subarray([0,2])
