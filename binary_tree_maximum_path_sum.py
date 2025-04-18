from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root: Optional[TreeNode]) -> int:
    """
    Find the maximum path sum in a binary tree.
    A path is defined as any sequence of nodes from some starting node to any node
    in the tree along the parent-child connections.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        Maximum path sum
    """
    max_sum = float('-inf')
    
    def max_gain(node: Optional[TreeNode]) -> int:
        nonlocal max_sum
        if not node:
            return 0
            
        # Max path sum from left and right subtrees
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        
        # Current path sum including the current node
        current_path_sum = node.val + left_gain + right_gain
        
        # Update the global maximum
        max_sum = max(max_sum, current_path_sum)
        
        # Return the maximum gain if we continue the path
        return node.val + max(left_gain, right_gain)
    
    max_gain(root)
    return max_sum

def list_to_tree(lst: list) -> Optional[TreeNode]:
    """Convert a list representation to a binary tree."""
    if not lst:
        return None
        
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    
    while queue and i < len(lst):
        node = queue.pop(0)
        
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    
    return root

def test_max_path_sum():
    """Test cases for the binary tree maximum path sum solution."""
    
    test_cases = [
        # Basic cases
        ([1, 2, 3], 6),  # Path: 2 -> 1 -> 3
        ([-10, 9, 20, None, None, 15, 7], 42),  # Path: 15 -> 20 -> 7
        ([1], 1),
        # Complete binary tree
        ([1, 2, 3, 4, 5, 6, 7], 18),  # Path: 4 -> 2 -> 1 -> 3 -> 7
        # Left skewed tree
        ([1, 2, None, 3, None, 4], 10),  # Path: 4 -> 3 -> 2 -> 1
        # Right skewed tree
        ([1, None, 2, None, 3, None, 4], 10),  # Path: 1 -> 2 -> 3 -> 4
        # Complex cases
        ([5, 3, 6, 2, 4, None, None, 1], 20),  # Path: 1 -> 2 -> 3 -> 4 -> 6
        # Large tree
        (list(range(1, 16)), 45),  # Path: 8 -> 4 -> 2 -> 1 -> 3 -> 7 -> 15
        # Edge cases
        ([1, None, None], 1),
        ([1, 2, None], 3),  # Path: 1 -> 2
        # Mixed values
        ([10, 5, 15, 3, 7, 12, 20], 57),  # Path: 3 -> 5 -> 10 -> 15 -> 20
        # All negative numbers
        ([-1, -2, -3], -1),
        # Single negative number
        ([-1], -1)
    ]
    
    print("Testing Binary Tree Maximum Path Sum Solution...")
    for tree_list, expected in test_cases:
        # Convert list to tree
        root = list_to_tree(tree_list)
        
        # Calculate maximum path sum
        result = max_path_sum(root)
        
        print(f"\nInput: {tree_list}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_max_path_sum() 