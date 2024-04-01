# Check if two BST in order traversal are same

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        temp = node.right
        while temp:
            self.stack.append(temp)
            temp = temp.left
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

def parallel_in_order_traversal(tree_a, tree_b):
    iterator_a = BSTIterator(tree_a)
    iterator_b = BSTIterator(tree_b)

    while iterator_a.hasNext() and iterator_b.hasNext():
        value_a = iterator_a.next()
        value_b = iterator_b.next()
        if value_a != value_b:
            return False

    return False if iterator_a.hasNext() or iterator_b.hasNext() else True


# Constructing Tree A
# Constructing Tree A
root_a = TreeNode(5)
root_a.right = TreeNode(8)
root_a.right.right = TreeNode(10)
root_a.right.right.right = TreeNode(15)
root_a.right.right.right.right = TreeNode(20)
root_a.right.right.right.right.right = TreeNode(25)

# Constructing Tree B
root_b = TreeNode(15)
root_b.left = TreeNode(8)
root_b.right = TreeNode(20)
root_b.left.left = TreeNode(5)
root_b.left.right = TreeNode(10)
root_b.right.right = TreeNode(25)
# in-order traversal should be - [5, 8, 10, 15, 20,25] for both trees and it should return true
result = parallel_in_order_traversal(root_a, root_b)
print(result)
