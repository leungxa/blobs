# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4. 

def longest_consecutive(numbers):
    cache = set()
    for num in numbers:
        cache.add(num)
    longest_len = 0
    for num in numbers:
        if num - 1 not in cache:
            start = num
            cur_len = 1
            while (start + 1 in cache):
                cur_len += 1
                start = start + 1
            longest_len = max(cur_len, longest_len)
    return longest_len

print longest_consecutive([100,4,200,1,3,2])
