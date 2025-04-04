class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        Find the maximum path sum in a binary tree.
        A path is defined as any sequence of nodes from some starting node to any node
        in the tree along the parent-child connections.
        
        Args:
            root: The root node of the binary tree
        
        Returns:
            The maximum path sum in the tree
        """
        self.max_sum = float('-inf')  # Initialize global maximum
        
        def max_gain(node):
            if not node:
                return 0
            
            # Get the maximum path sum from left and right subtrees
            # If the path sum is negative, we don't include it (take 0 instead)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # The price to start a new path where `node` is the highest point
            price_newpath = node.value + left_gain + right_gain
            
            # Update max_sum if it's better to start a new path
            self.max_sum = max(self.max_sum, price_newpath)
            
            # For recursion: return the max gain if continue the same path
            return node.value + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum

def build_test_tree1():
    """
    Builds test tree 1:
         1
        / \
       2   3
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    return root

def build_test_tree2():
    """
    Builds test tree 2:
        -10
        / \
       9  20
          / \
         15  7
    """
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

def build_test_tree3():
    """
    Builds test tree 3:
         -3
        / \
      -2   3
     /    / \
    -1   4   5
    """
    root = TreeNode(-3)
    root.left = TreeNode(-2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(-1)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    return root

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Simple tree
    root1 = build_test_tree1()
    print("Test case 1 - Expected: 6, Got:", solution.maxPathSum(root1))
    
    # Test case 2: Tree with negative root
    root2 = build_test_tree2()
    print("Test case 2 - Expected: 42, Got:", solution.maxPathSum(root2))
    
    # Test case 3: Tree with negative values
    root3 = build_test_tree3()
    print("Test case 3 - Expected: 12, Got:", solution.maxPathSum(root3)) 