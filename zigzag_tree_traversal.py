"""
Problem: Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).

Example:
    3
   / \
  9  20
    /  \
   15   7

Output:
[
  [3],
  [20, 9],
  [15, 7]
]
"""

from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform zigzag level order traversal of a binary tree.
    Uses a deque for level-by-level processing.
    
    Time complexity: O(n) where n is number of nodes
    Space complexity: O(w) where w is maximum width of tree
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        # Process current level
        for _ in range(level_size):
            node = queue.popleft()
            
            # Add to current level based on direction
            if left_to_right:
                current_level.append(node.val)
            else:
                current_level.insert(0, node.val)
            
            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
        left_to_right = not left_to_right
    
    return result

def create_tree(values: List[Optional[int]], index: int = 0) -> Optional[TreeNode]:
    """Create a binary tree from a list of values using level-order traversal."""
    if not values or index >= len(values) or values[index] is None:
        return None
    
    root = TreeNode(values[index])
    root.left = create_tree(values, 2 * index + 1)
    root.right = create_tree(values, 2 * index + 2)
    
    return root

def print_tree(root: Optional[TreeNode], level: int = 0, prefix: str = "Root: "):
    """Print a binary tree in a readable format."""
    if not root:
        return
    
    print("  " * level + prefix + str(root.val))
    if root.left or root.right:
        print_tree(root.left, level + 1, "L--- ")
        print_tree(root.right, level + 1, "R--- ")

def test_zigzag_traversal():
    test_cases = [
        # Test 1: Standard case from example
        [3, 9, 20, None, None, 15, 7],
        
        # Test 2: Perfect binary tree
        [1, 2, 3, 4, 5, 6, 7],
        
        # Test 3: Left-skewed tree
        [1, 2, None, 3, None, None, None],
        
        # Test 4: Right-skewed tree
        [1, None, 2, None, None, None, 3],
        
        # Test 5: Single node
        [1],
        
        # Test 6: Empty tree
        [],
        
        # Test 7: Deep tree
        [1, 2, 3, 4, None, None, 5, 6, None, None, None, None, None, None, 7]
    ]
    
    for i, values in enumerate(test_cases, 1):
        print(f"\nTest {i}:")
        root = create_tree(values)
        
        print("Tree structure:")
        print_tree(root)
        
        result = zigzag_level_order(root)
        print("\nZigzag traversal:")
        for level_num, level in enumerate(result):
            direction = "Left->Right" if level_num % 2 == 0 else "Right->Left"
            print(f"Level {level_num} ({direction}): {level}")
        print("-" * 50)

if __name__ == "__main__":
    test_zigzag_traversal()
