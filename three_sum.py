def three_sum(i_array):
    i_map = {}
    for value in i_array:
        if value not in i_map:
            i_map[value] = 1
        else:
            i_map[value] += 1
    
    ret_values = []
    key_set = set()
    
    for i in range(len(i_array)):
        for j in range(i+1, len(i_array)):
            num_to_find = -(i_array[i] + i_array[j])
            key = ''.join([str(x) for x in sorted([i_array[i], i_array[j], num_to_find])])
            if key in key_set:
                continue
            count = 0
            if i_array[i] == num_to_find:
                count += 1
            if i_array[j] == num_to_find:
                count += 1
            if num_to_find in i_map and count < i_map[num_to_find]:
                ret_values.append(sorted([i_array[i], i_array[j], num_to_find]))
                key_set.add(key)

    return ret_values

S = [-1, 0, 1, 2, -1, -4]
print three_sum(S)
S = [-1, 0]
print three_sum(S)
