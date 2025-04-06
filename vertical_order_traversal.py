class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> list:
        """
        Given a binary tree, return the vertical order traversal of its nodes' values.
        For each vertical line, nodes are ordered from top to bottom.
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            List of lists containing node values in vertical order
        """
        if not root:
            return []
        
        # Dictionary to store nodes by their column index
        column_dict = {}
        # Queue for BFS: (node, column)
        queue = [(root, 0)]
        
        while queue:
            node, col = queue.pop(0)
            
            # Add node to its column
            if col not in column_dict:
                column_dict[col] = []
            column_dict[col].append(node.value)
            
            # Add children to queue with updated column indices
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
        
        # Sort columns and return values
        return [column_dict[col] for col in sorted(column_dict.keys())]

    def verticalOrderWithLevel(self, root: TreeNode) -> list:
        """
        Given a binary tree, return the vertical order traversal of its nodes' values.
        For each vertical line, nodes are ordered from top to bottom.
        If two nodes are in the same row and column, order them by their values.
        
        Args:
            root: Root node of the binary tree
            
        Returns:
            List of lists containing node values in vertical order
        """
        if not root:
            return []
        
        # Dictionary to store nodes by their column index: {col: [(row, value), ...]}
        column_dict = {}
        # Queue for BFS: (node, row, column)
        queue = [(root, 0, 0)]
        
        while queue:
            node, row, col = queue.pop(0)
            
            # Add node to its column
            if col not in column_dict:
                column_dict[col] = []
            column_dict[col].append((row, node.value))
            
            # Add children to queue with updated coordinates
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        
        # Sort columns and values within each column
        result = []
        for col in sorted(column_dict.keys()):
            # Sort by row, then by value
            column_dict[col].sort()
            result.append([val for (_, val) in column_dict[col]])
        
        return result

def build_test_tree1():
    """
    Builds test tree 1:
         3
        / \
       9   20
          /  \
         15   7
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

def build_test_tree2():
    """
    Builds test tree 2:
         1
        / \
       2   3
      / \   \
     4   5   6
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root

def build_test_tree3():
    """
    Builds test tree 3:
         1
        / \
       2   3
      / \   \
     4   5   6
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
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
    
    print("Test Case 1: Tree with multiple levels")
    root1 = build_test_tree1()
    print("Tree structure:")
    print_tree(root1)
    print("Vertical order traversal:")
    print(solution.verticalOrder(root1))  # Expected: [[9], [3, 15], [20], [7]]
    print("Vertical order with level consideration:")
    print(solution.verticalOrderWithLevel(root1))  # Expected: [[9], [3, 15], [20], [7]]
    
    print("\nTest Case 2: Tree with overlapping nodes")
    root2 = build_test_tree2()
    print("Tree structure:")
    print_tree(root2)
    print("Vertical order traversal:")
    print(solution.verticalOrder(root2))  # Expected: [[4], [2], [1, 5], [3], [6]]
    print("Vertical order with level consideration:")
    print(solution.verticalOrderWithLevel(root2))  # Expected: [[4], [2], [1, 5], [3], [6]]
    
    print("\nTest Case 3: Tree with same structure as Test Case 2")
    root3 = build_test_tree3()
    print("Tree structure:")
    print_tree(root3)
    print("Vertical order traversal:")
    print(solution.verticalOrder(root3))  # Expected: [[4], [2], [1, 5], [3], [6]]
    print("Vertical order with level consideration:")
    print(solution.verticalOrderWithLevel(root3))  # Expected: [[4], [2], [1, 5], [3], [6]] 