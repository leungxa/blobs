# https://www.codechef.com/SEP12/problems/CHEFTOWN/

import bisect

def parade(heights, len_parade):
    if len_parade > len(heights):
        return 0
    
    num_interesting = 0
    running_str = []
    sorted_heights = []
    for i in range(len_parade):
        bisect.insort(sorted_heights, heights[i])
    
    while (i < len(heights)):
        m_min = sorted_heights[0]
        m_max = sorted_heights[-1]
        is_interesting = (m_max - m_min) == (len_parade - 1)
        if is_interesting:
            num_interesting += 1
        t_remove = heights[i - (len_parade - 1)]
        # remove from the list
        sorted_heights.remove(t_remove)
        if i < len(heights) - 1:
            t_add = heights[i + 1]
            bisect.insort(sorted_heights, t_add)
        i += 1
    return num_interesting
        
        
print parade([5,4,6,2,1,3], 3)
print parade([2,1,3], 2)
print parade([1,2,3], 2)
print parade([1,2,3,4], 2)
