class Node:
    def __init__(self, val, nxt):
        self.value = val
        self.next_node = nxt


def build_ll():
    head = None
    for x in range(5):
        new_node = Node(x, head)
        head = new_node
    return head

a = build_ll()

head = a
def print_ll(head):
    while head:
        print head.value
        head = head.next_node

print_ll(a)

def reverse_ll(head):
    current_node = head
    prev_node = None
    while current_node:
        next_node = current_node.next_node
        current_node.next_node = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node

print "reversed"

a = reverse_ll(a)
print_ll(a)

