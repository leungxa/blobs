class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def level_order_traversal(node):
    if not node:
        return
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        print current_node.value
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

# testing
new_node = Node(1, None, None)
print new_node.value

left_node = Node(2, None, None)
new_node.left = left_node
print new_node.left.value

right_node = Node(3, None, None)
new_node.right = right_node
print new_node.right.value

print 'testNone'
level_order_traversal(None)
print 'testOneNode'
level_order_traversal(right_node)
print 'testNewNode'
level_order_traversal(new_node)

right_left = Node(4, None, None)
right_node.left = right_left
right_right = Node(5, None, None)
right_node.right = right_right
print 'testExpandedRight'
level_order_traversal(new_node)
