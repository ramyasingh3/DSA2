from typing import List, Optional, Dict, Tuple
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Perform vertical order traversal of a binary tree.
    Nodes in the same column and row should be ordered from left to right.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of lists containing node values in vertical order
    """
    if not root:
        return []
    
    # Dictionary to store nodes by their column index
    column_table = defaultdict(list)
    # Queue for BFS, storing (node, column, row)
    queue = deque([(root, 0, 0)])
    min_col = max_col = 0
    
    while queue:
        node, col, row = queue.popleft()
        
        # Update column range
        min_col = min(min_col, col)
        max_col = max(max_col, col)
        
        # Store node with its position
        column_table[col].append((row, node.val))
        
        # Enqueue children with updated positions
        if node.left:
            queue.append((node.left, col - 1, row + 1))
        if node.right:
            queue.append((node.right, col + 1, row + 1))
    
    # Sort nodes in each column by row and value
    result = []
    for col in range(min_col, max_col + 1):
        # Sort by row first, then by value
        column_table[col].sort()
        # Extract just the values in order
        result.append([val for _, val in column_table[col]])
    
    return result

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

def test_vertical_order():
    """Test cases for the binary tree vertical order traversal solution."""
    
    test_cases = [
        # Basic cases
        ([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]),
        ([1], [[1]]),
        
        # Edge cases
        ([], []),
        ([1, 2, None], [[2], [1]]),
        ([1, None, 2], [[1], [2]]),
        
        # Complete binary tree
        ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]]),
        
        # Left-skewed tree
        ([1, 2, None, 3, None, 4], [[4], [3], [2], [1]]),
        
        # Right-skewed tree
        ([1, None, 2, None, None, None, 3], [[1], [2], [3]]),
        
        # Complex cases
        ([3, 9, 8, 4, 0, 1, 7], [[4], [9], [3, 0, 1], [8], [7]]),
        ([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5], [[4], [9, 5], [3, 0, 1], [8, 2], [7]]),
        
        # Large tree
        (list(range(1, 16)), [[8], [4], [2, 9, 10], [1, 5, 6], [3, 11, 12], [7, 13, 14], [15]]),
        
        # Edge cases with None values
        ([1, None, 2, None, None, 3, None], [[1], [2], [3]]),
        ([1, 2, None, 3, None, None, None], [[3], [2], [1]]),
        
        # Mixed values
        ([10, 5, 15, 3, 7, 12, 20], [[3], [5], [10, 7, 12], [15], [20]]),
        
        # All negative numbers
        ([-1, -2, -3, -4, -5], [[-4], [-2], [-1, -5], [-3]]),
        
        # Single negative number
        ([-1], [[-1]])
    ]
    
    print("Testing Binary Tree Vertical Order Traversal Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get vertical order traversal
        result = vertical_order(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_vertical_order() 