class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.path = []

from collections import deque
def longest_path(root):
    # BFS, longest path
    root.path = [root]
    longest_path = root.path
    queue = deque([root])
    while len(queue):
        cur_node = queue.popleft()
        if len(cur_node.path) > len(longest_path):
            longest_path = cur_node.path
        for child in [cur_node.left, cur_node.right]:
            if child:
                path = cur_node.path + [child]
                child.path = path
                queue.append(child)
    return longest_path
    
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.right = b
b.right = c
c.right = d
b.left = e

# print a.value
print [x.value for x in longest_path(e)]
print [x.value for x in longest_path(a)]
