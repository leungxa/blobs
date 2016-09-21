def merge_sort(a_list):
    if len(a_list) <= 1:
        return a_list

    half = len(a_list)/2
    list1 = a_list[:half]
    list2 = a_list[half:]
    m1 = merge_sort(list1)
    m2 = merge_sort(list2)
    
    return _merge(m1, m2)
    
def _merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if len(l1) == 1 and len(l2) == 1:
        return [min(l1[0],l2[0]), max(l1[0],l2[0])]
    else:
        total = []
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                total.append(l1[i])
                i += 1
            else:
                total.append(l2[j])
                j += 1
        while i < len(l1):
            total.append(l1[i])
            i += 1
        while j < len(l2):
            total.append(l2[j])
            j += 1
        return total
            
# a = [1,3,4,10,11]
# b = [4]
# print _merge(a,b)
# c = [2,10,1,10,2]
# print merge_sort(c)
# c = [2,1,100,10,11,2,3,12,7,20]
# print merge_sort(c)
# c = []
# print merge_sort(c)
