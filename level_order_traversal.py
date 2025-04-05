from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        Perform level order traversal of a binary tree.
        Returns a list of lists, where each inner list represents one level of the tree.
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            List of lists containing values at each level
        """
        if not root:
            return []
        
        result = []
        queue = deque([(root, 0)])  # (node, level)
        
        while queue:
            node, level = queue.popleft()
            
            # Add a new level list if needed
            if len(result) == level:
                result.append([])
            
            # Add current node's value to its level
            result[level].append(node.value)
            
            # Add children to queue with next level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return result
    
    def levelOrderSpiral(self, root):
        """
        Variant: Spiral (Zigzag) Level Order Traversal
        Odd levels are traversed left to right, even levels right to left
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            List of lists containing values at each level in spiral order
        """
        if not root:
            return []
        
        result = []
        queue = deque([(root, 0)])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node, level = queue.popleft()
                current_level.append(node.value)
                
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
            
            # Reverse alternate levels
            if level % 2 == 1:
                current_level.reverse()
            
            result.append(current_level)
        
        return result

def build_test_tree1():
    """
    Builds test tree 1:
         1
        / \
       2   3
      / \
     4   5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root

def build_test_tree2():
    """
    Builds test tree 2:
           1
          / \
         2   3
        /     \
       4       5
      /         \
     6           7
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.right.right.right = TreeNode(7)
    return root

def build_test_tree3():
    """
    Builds test tree 3:
         1
        / \
       2   3
      /   / \
     4   5   6
        /     \
       7       8
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.right.right = TreeNode(8)
    return root

def print_tree(node, level=0, prefix="Root: "):
    """Helper function to print the tree structure"""
    if not node:
        return
    
    print("  " * level + prefix + str(node.value))
    if node.left or node.right:
        if node.left:
            print_tree(node.left, level + 1, "L--- ")
        if node.right:
            print_tree(node.right, level + 1, "R--- ")

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Simple balanced tree
    print("\nTest Case 1: Simple balanced tree")
    root1 = build_test_tree1()
    print("Tree structure:")
    print_tree(root1)
    print("Level order traversal:", solution.levelOrder(root1))
    print("Spiral level order:", solution.levelOrderSpiral(root1))
    
    # Test case 2: Unbalanced tree
    print("\nTest Case 2: Unbalanced tree")
    root2 = build_test_tree2()
    print("Tree structure:")
    print_tree(root2)
    print("Level order traversal:", solution.levelOrder(root2))
    print("Spiral level order:", solution.levelOrderSpiral(root2))
    
    # Test case 3: Complex tree
    print("\nTest Case 3: Complex tree")
    root3 = build_test_tree3()
    print("Tree structure:")
    print_tree(root3)
    print("Level order traversal:", solution.levelOrder(root3))
    print("Spiral level order:", solution.levelOrderSpiral(root3)) 