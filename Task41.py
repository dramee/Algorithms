import random


class Node:
    def __init__(self, value):
        self.value = value
        self.priority = random.randint(0, 1000)
        self.size = 1
        self.left = None
        self.right = None


class ImplicitTreap:
    def __init__(self):
        self.root = None

    @staticmethod
    def _size(node):
        return node.size if node else 0

    def _update_size(self, node):
        if node:
            node.size = self._size(node.left) + self._size(node.right) + 1

    def _merge(self, left, right):
        if not left or not right:
            return left if not right else right

        if left.priority < right.priority:
            left.right = self._merge(left.right, right)
            self._update_size(left)
            return left
        else:
            right.left = self._merge(left, right.left)
            self._update_size(right)
            return right

    def _split(self, node, index):
        if not node:
            return None, None

        if index <= self._size(node.left):
            left, right = self._split(node.left, index)
            node.left = right
            self._update_size(node)
            return left, node
        else:
            left, right = self._split(node.right, index - self._size(node.left) - 1)
            node.right = left
            self._update_size(node)
            return node, right

    def insert(self, index, value):
        left, right = self._split(self.root, index)
        new_node = Node(value)
        self.root = self._merge(self._merge(left, new_node), right)

    def build(self, array):
        for i in range(len(array)):
            self.insert(i, array[i])

    def sum(self, frm, to):
        left, mid = self._split(self.root, frm)
        mid, right = self._split(mid, to - frm + 1)
        total_sum = self._get_sum(mid)
        self.root = self._merge(left, self._merge(mid, right))
        return total_sum

    def _get_sum(self, node):
        return node.value + self._get_sum(node.left) + self._get_sum(node.right) if node else 0


treap = ImplicitTreap()

# Test building the treap with an initial array
initial_array = [10, 20, 30, 40, 50]
treap.build(initial_array)
print("Treap built with initial array:", initial_array)

# Test summing a range
from_idx, to_idx = 1, 3
sum_result = treap.sum(from_idx, to_idx)
print(f"Sum from index {from_idx} to {to_idx}:", sum_result)

# Test inserting a new value
new_value = 25
insert_index = 2
treap.insert(insert_index, new_value)
print(f"Inserted {new_value} at index {insert_index}, all sum is:", treap.sum(0, len(initial_array)))


# Ensure the treap maintains correct structure and values after operations
# This might involve in-order traversal to verify the treap's shape and values
# For example:
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(f"Value: {node.value}, Priority: {node.priority}, Size: {node.size}")
        in_order_traversal(node.right)


print("In-order traversal of the treap after insertion:")
in_order_traversal(treap.root)
