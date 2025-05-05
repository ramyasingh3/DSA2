"""
Binary Tree Level Order Traversal Implementation

This file contains multiple implementations to perform level order traversal of a binary tree.

Problem Statement:
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Time Complexity: O(n) for optimal solution
Space Complexity: O(w) for optimal solution, where w is the maximum width of the tree
"""

from collections import deque
from typing import List, Optional

class TreeNode:
    """Binary Tree Node class"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_queue(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level order traversal using queue (BFS).
    Time Complexity: O(n)
    Space Complexity: O(w) where w is the maximum width of the tree
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

def level_order_recursive(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level order traversal using recursion.
    Time Complexity: O(n)
    Space Complexity: O(h) where h is the height of the tree (due to recursion stack)
    """
    def traverse(node: Optional[TreeNode], level: int, result: List[List[int]]) -> None:
        if not node:
            return
        
        # Add a new level list if needed
        if level >= len(result):
            result.append([])
        
        # Add current node's value to its level
        result[level].append(node.val)
        
        # Recursively process children
        traverse(node.left, level + 1, result)
        traverse(node.right, level + 1, result)
    
    result = []
    traverse(root, 0, result)
    return result

def level_order_dfs(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level order traversal using DFS.
    Time Complexity: O(n)
    Space Complexity: O(h) where h is the height of the tree
    """
    def get_height(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))
    
    def process_level(node: Optional[TreeNode], level: int, result: List[List[int]]) -> None:
        if not node:
            return
        
        result[level].append(node.val)
        
        if node.left:
            process_level(node.left, level + 1, result)
        if node.right:
            process_level(node.right, level + 1, result)
    
    if not root:
        return []
    
    height = get_height(root)
    result = [[] for _ in range(height)]
    process_level(root, 0, result)
    return result

def level_order_zigzag(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level order traversal in zigzag pattern.
    Time Complexity: O(n)
    Space Complexity: O(w) where w is the maximum width of the tree
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if not left_to_right:
            current_level.reverse()
        
        result.append(current_level)
        left_to_right = not left_to_right
    
    return result

def create_tree(values: List[Optional[int]], index: int = 0) -> Optional[TreeNode]:
    """Helper function to create a binary tree from a list of values"""
    if index >= len(values) or values[index] is None:
        return None
    
    root = TreeNode(values[index])
    root.left = create_tree(values, 2 * index + 1)
    root.right = create_tree(values, 2 * index + 2)
    return root

def test_level_order_traversal():
    """Test cases for level order traversal implementations"""
    test_cases = [
        ([3,9,20,None,None,15,7],
         [[3],[9,20],[15,7]]),                    # Standard case
        ([1],
         [[1]]),                                   # Single node
        ([],
         []),                                      # Empty tree
        ([1,2,3,4,5,6,7],
         [[1],[2,3],[4,5,6,7]]),                  # Perfect binary tree
        ([1,None,2],
         [[1],[2]]),                              # Right skewed
        ([1,2,None,3],
         [[1],[2],[3]]),                          # Left skewed
        ([1,2,3,4,None,None,5],
         [[1],[2,3],[4,5]]),                      # Irregular tree
    ]
    
    for values, expected in test_cases:
        root = create_tree(values)
        
        # Test queue-based approach
        result = level_order_queue(root)
        assert result == expected, f"Queue test failed for {values}"
        
        # Test recursive approach
        result = level_order_recursive(root)
        assert result == expected, f"Recursive test failed for {values}"
        
        # Test DFS approach
        result = level_order_dfs(root)
        assert result == expected, f"DFS test failed for {values}"
        
        # Test zigzag approach (only test length and elements, not order)
        result = level_order_zigzag(root)
        assert len(result) == len(expected), f"Zigzag test failed for {values}"
        assert sorted([x for level in result for x in level]) == \
               sorted([x for level in expected for x in level]), \
               f"Zigzag test failed for {values}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_level_order_traversal()
    
    # Example usage
    test_trees = [
        [3,9,20,None,None,15,7],
        [1],
        [],
        [1,2,3,4,5,6,7],
        [1,None,2],
        [1,2,None,3],
        [1,2,3,4,None,None,5]
    ]
    
    print("\nTesting various trees:")
    for values in test_trees:
        root = create_tree(values)
        print(f"\nTree values: {values}")
        print(f"Using queue-based BFS: {level_order_queue(root)}")
        print(f"Using recursion: {level_order_recursive(root)}")
        print(f"Using DFS: {level_order_dfs(root)}")
        print(f"Using zigzag traversal: {level_order_zigzag(root)}") 