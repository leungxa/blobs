# Suppose we are writing the backend for a search engine. 
# The search fetches n >= 2 sorted lists of IDs (ints) 
# representing the search results. Return their union as
# a single sorted list without duplicates.

list1 = [1, 3, 5]
list2 = [2, 4, 6]
list3 = [1, 7]
lists = [list1, list2, list3]

# [1, 2, 3, 4, 5, 6, 7]

list1 = [1]
list2 = [2]
list3 = [3]
list4 = [4]
lists = [list1, list2, list3, list4]
# [1, 2, 3, 4]

def uniq_merge(list1, list2):
    i,j = 0, 0
    ret_list = []
    while (i < len(list1) and j < len(list2)):
        if list1[i] == list2[j]:
            ret_list.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            ret_list.append(list1[i])
            i += 1
        else:
            ret_list.append(list2[j])
            j += 1
    while (i < len(list1)):
        ret_list.append(list1[i])
        i += 1
    while (j < len(list2)):
        ret_list.append(list2[j])
        j += 1
            
    return ret_list

def merge_all(list_lists):
    im_list = []
    while len(list_lists) > 1:
        for i in range(0, len(list_lists), 2):
            if i+1 < len(list_lists):
                im_list.append(uniq_merge(list_lists[i], list_lists[i+1]))
            else:
                im_list.append(list_lists[i])
        list_lists = im_list
        im_list = []
    return list_lists[0]

list1 = [1, 3, 5]
list2 = [2, 4, 6]
list3 = [1, 7, 10]
list4 = []
ll = [list1, list2, list3, list4]
print merge_all(ll)

# M items in total, N lists O(M*N)
# list1 = [1, 2, 3, ...., 10000000000]
# list2 = [0]
# list3 = [213]
# list4 = [4211]
# list5 = [213]
# list6 = [4211]
