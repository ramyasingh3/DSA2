"""
Problem: Binary Search Tree Iterator

Implement an iterator over a Binary Search Tree (BST) that supports:
1. next() - Returns the next smallest number in the BST (inorder traversal)
2. hasNext() - Returns whether there exists a next number
3. peek() - Returns the next number without advancing the iterator

The iterator should run in O(h) space complexity, where h is the height of the tree.
Example:
   7
  / \
 3   15
    /  \
   9    20

Iterator iter = BSTIterator(root)
iter.next()    # returns 3
iter.next()    # returns 7
iter.peek()    # returns 9
iter.next()    # returns 9
iter.hasNext() # returns true
iter.next()    # returns 15
iter.next()    # returns 20
iter.hasNext() # returns false
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        """Initialize stack and push all left nodes."""
        self.stack = []
        self._push_left(root)
    
    def _push_left(self, node: Optional[TreeNode]) -> None:
        """Push all left nodes of the given node onto the stack."""
        while node:
            self.stack.append(node)
            node = node.left
    
    def hasNext(self) -> bool:
        """Return whether there exists a next smallest number."""
        return len(self.stack) > 0
    
    def peek(self) -> Optional[int]:
        """Return the next smallest number without advancing the iterator."""
        if not self.hasNext():
            return None
        return self.stack[-1].val
    
    def next(self) -> Optional[int]:
        """Return the next smallest number and advance the iterator."""
        if not self.hasNext():
            return None
        
        # Get the next smallest node
        curr = self.stack.pop()
        # Push all left nodes of its right subtree
        self._push_left(curr.right)
        
        return curr.val

def create_tree(values: List[Optional[int]], index: int = 0) -> Optional[TreeNode]:
    """Create a binary tree from a list of values using level-order traversal."""
    if not values or index >= len(values) or values[index] is None:
        return None
    
    root = TreeNode(values[index])
    root.left = create_tree(values, 2 * index + 1)
    root.right = create_tree(values, 2 * index + 2)
    
    return root

def test_bst_iterator():
    print("Test 1: Basic BST Iterator Operations")
    # Create BST: [7, 3, 15, None, None, 9, 20]
    root = create_tree([7, 3, 15, None, None, 9, 20])
    iterator = BSTIterator(root)
    
    print("next():", iterator.next())      # Should be 3
    print("next():", iterator.next())      # Should be 7
    print("peek():", iterator.peek())      # Should be 9
    print("next():", iterator.next())      # Should be 9
    print("hasNext():", iterator.hasNext()) # Should be True
    print("next():", iterator.next())      # Should be 15
    print("next():", iterator.next())      # Should be 20
    print("hasNext():", iterator.hasNext()) # Should be False
    print("-" * 50)
    
    print("\nTest 2: Empty Tree")
    iterator = BSTIterator(None)
    print("hasNext():", iterator.hasNext()) # Should be False
    print("next():", iterator.next())      # Should be None
    print("peek():", iterator.peek())      # Should be None
    print("-" * 50)
    
    print("\nTest 3: Single Node Tree")
    root = TreeNode(1)
    iterator = BSTIterator(root)
    print("peek():", iterator.peek())      # Should be 1
    print("hasNext():", iterator.hasNext()) # Should be True
    print("next():", iterator.next())      # Should be 1
    print("hasNext():", iterator.hasNext()) # Should be False
    print("-" * 50)
    
    print("\nTest 4: Left-heavy Tree")
    # Create BST: [3, 2, None, 1]
    root = create_tree([3, 2, None, 1])
    iterator = BSTIterator(root)
    print("next():", iterator.next())      # Should be 1
    print("next():", iterator.next())      # Should be 2
    print("next():", iterator.next())      # Should be 3
    print("hasNext():", iterator.hasNext()) # Should be False

if __name__ == "__main__":
    test_bst_iterator()
