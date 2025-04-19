from typing import List, Optional, Tuple
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def width_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    Find the maximum width of a binary tree.
    The width of a level is defined as the number of nodes between the leftmost and rightmost non-null nodes.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        Maximum width of the binary tree
    """
    if not root:
        return 0
    
    max_width = 0
    # Queue stores tuples of (node, position)
    queue = deque([(root, 0)])
    
    while queue:
        level_size = len(queue)
        # Get the position of the first and last nodes in the current level
        first_pos = queue[0][1]
        last_pos = queue[-1][1]
        # Calculate width of current level
        current_width = last_pos - first_pos + 1
        max_width = max(max_width, current_width)
        
        # Process all nodes in the current level
        for _ in range(level_size):
            node, pos = queue.popleft()
            # Calculate positions of children
            if node.left:
                queue.append((node.left, 2 * pos))
            if node.right:
                queue.append((node.right, 2 * pos + 1))
    
    return max_width

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

def test_width_of_binary_tree():
    """Test cases for the binary tree maximum width solution."""
    
    test_cases = [
        # Basic cases
        ([1, 3, 2, 5, 3, None, 9], 4),
        ([1, 3, 2, 5], 2),
        ([1], 1),
        
        # Edge cases
        ([], 0),
        ([1, None, 2], 1),
        ([1, 2, None], 1),
        
        # Complete binary tree
        ([1, 2, 3, 4, 5, 6, 7], 4),
        
        # Left-skewed tree
        ([1, 2, None, 3, None, 4], 1),
        
        # Right-skewed tree
        ([1, None, 2, None, None, None, 3], 1),
        
        # Complex cases
        ([1, 2, 3, 4, 5, None, 6, None, None, 7, 8, None, None, 9, 10], 8),
        ([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, 9, 10], 7),
        
        # Large tree
        (list(range(1, 16)), 8),
        
        # Edge cases with None values
        ([1, None, 2, None, None, 3, None], 1),
        ([1, 2, None, 3, None, None, None], 1),
        
        # Mixed values
        ([10, 5, 15, 3, 7, 12, 20], 4),
        
        # All negative numbers
        ([-1, -2, -3, -4, -5], 2),
        
        # Single negative number
        ([-1], 1),
        
        # Special case with large width
        ([1, 1, 1, 1, None, None, 1, 1, None, None, 1], 8),
        ([1, 1, 1, 1, 1, 1, 1, None, None, None, 1, None, None, None, None, None, None, None, None, None, None, 1], 8)
    ]
    
    print("Testing Binary Tree Maximum Width Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Get maximum width
        result = width_of_binary_tree(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_width_of_binary_tree() 