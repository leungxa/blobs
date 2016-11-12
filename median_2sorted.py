# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

import math
from collections import deque

def median(l1, l2):
    i, j = 0, 0
    median_index = float(len(l1) + len(l2) - 1) / 2
    end = int(math.ceil(median_index))
    count = 0
    q = deque(maxlen=2)
    while (i < len(l1) and j < len(l2) and count <= end):
        val = None
        if l1[i] < l2[j]:
            val = l1[i]
            i += 1
        else:
            val = l2[j]
            j += 1
        q.append(val)
        count += 1
    while (i < len(l1) and count <= end):
        q.append(l1[i])
        i += 1
        count += 1
    while (j < len(l2) and count <= end):
        q.append(l2[j])
        j += 1
        count += 1
    if math.floor(median_index) == math.ceil(median_index):
        return q.pop()
    else:
        return float(q.pop() + q.pop()) / 2

l1 = [1,2,2,4,5,6]
l2 = [3]
print median(l1, l2)
        
