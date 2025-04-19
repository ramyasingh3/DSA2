from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def boundary_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Perform boundary traversal of a binary tree in the following order:
    1. Left boundary (top-down)
    2. Leaf nodes (left to right)
    3. Right boundary (bottom-up)
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of node values in boundary traversal order
    """
    if not root:
        return []
    
    result = []
    
    # Add root if it's not a leaf
    if not is_leaf(root):
        result.append(root.val)
    
    # Add left boundary (excluding root and leaves)
    add_left_boundary(root.left, result)
    
    # Add leaves
    add_leaves(root, result)
    
    # Add right boundary (excluding root and leaves)
    add_right_boundary(root.right, result)
    
    return result

def is_leaf(node: Optional[TreeNode]) -> bool:
    """Check if a node is a leaf node."""
    return node is not None and node.left is None and node.right is None

def add_left_boundary(node: Optional[TreeNode], result: List[int]) -> None:
    """Add left boundary nodes to the result list."""
    while node:
        if not is_leaf(node):
            result.append(node.val)
        if node.left:
            node = node.left
        else:
            node = node.right

def add_right_boundary(node: Optional[TreeNode], result: List[int]) -> None:
    """Add right boundary nodes to the result list in reverse order."""
    stack = []
    while node:
        if not is_leaf(node):
            stack.append(node.val)
        if node.right:
            node = node.right
        else:
            node = node.left
    
    # Add right boundary in reverse order
    while stack:
        result.append(stack.pop())

def add_leaves(node: Optional[TreeNode], result: List[int]) -> None:
    """Add leaf nodes to the result list."""
    if not node:
        return
    
    if is_leaf(node):
        result.append(node.val)
        return
    
    add_leaves(node.left, result)
    add_leaves(node.right, result)

def list_to_tree(lst: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Convert a list representation to a binary tree.
    The list is in level-order traversal (breadth-first) order.
    None values represent null nodes.
    """
    if not lst or lst[0] is None:
        return None
    
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    
    while queue and i < len(lst):
        node = queue.pop(0)
        
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    
    return root

def test_boundary_traversal():
    """Test cases for the binary tree boundary traversal solution."""
    
    test_cases = [
        # Basic cases
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 6, 7, 3]),
        ([1], [1]),
        
        # Edge cases
        ([], []),
        ([1, 2, None], [1, 2]),
        ([1, None, 2], [1, 2]),
        
        # Complete binary tree
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 6, 7, 3]),
        
        # Left-skewed tree
        ([1, 2, None, 3, None, 4], [1, 2, 3, 4]),
        
        # Right-skewed tree
        ([1, None, 2, None, None, None, 3], [1, 2, 3]),
        
        # Complex cases
        ([1, 2, 3, 4, 5, None, 6, None, None, 7, 8, None, None, 9, 10], [1, 2, 4, 7, 8, 9, 10, 6, 3]),
        ([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, 9, 10], [1, 2, 4, 7, 9, 10, 6, 3]),
        
        # Large tree
        (list(range(1, 16)), [1, 2, 4, 8, 9, 10, 11, 12, 13, 14, 15, 7, 3]),
        
        # Edge cases with None values
        ([1, None, 2, None, None, 3, None], [1, 2, 3]),
        ([1, 2, None, 3, None, None, None], [1, 2, 3]),
        
        # Mixed values
        ([10, 5, 15, 3, 7, 12, 20], [10, 5, 3, 7, 12, 20, 15]),
        
        # All negative numbers
        ([-1, -2, -3, -4, -5], [-1, -2, -4, -5, -3]),
        
        # Single negative number
        ([-1], [-1])
    ]
    
    print("Testing Binary Tree Boundary Traversal Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get boundary traversal
        result = boundary_traversal(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_boundary_traversal() 