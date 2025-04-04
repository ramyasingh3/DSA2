# Maximum Path Sum in Binary Tree

## Problem Description
Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

## Examples

### Example 1:
```
Input:
     1
    / \
   2   3

Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6
```

### Example 2:
```
Input:
    -10
    /  \
   9    20
       /  \
      15   7

Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42
```

### Example 3:
```
Input:
     -3
    /  \
  -2    3
 /     / \
-1    4   5

Output: 12
Explanation: The optimal path is 4 -> 3 -> 5 with a path sum of 4 + 3 + 5 = 12
```

## Solution Approach

The solution uses a recursive approach with the following key points:

1. For each node, we calculate:
   - Maximum path sum that can be achieved through this node
   - Maximum sum that can be passed up to its parent

2. For each node, we consider four possibilities:
   - Node value only
   - Node value + left subtree
   - Node value + right subtree
   - Node value + both subtrees (only for paths that go through current node as highest point)

3. Key insights:
   - We don't include negative sums from subtrees
   - We maintain a global maximum to track the best path found
   - For recursion, we only return the maximum sum possible using at most one child

## Time Complexity
- O(N) where N is the number of nodes in the tree
- We visit each node exactly once

## Space Complexity
- O(H) where H is the height of the tree
- This space is used by the recursion stack
- In worst case (skewed tree), this becomes O(N)
- In balanced tree, this becomes O(log N)

## Usage
```python
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Create solution object
solution = Solution()

# Find maximum path sum
result = solution.maxPathSum(root)  # Returns 6
```

## Running the Tests
```bash
python max_path_sum.py
```

The program includes three test cases:
1. Simple tree with all positive values
2. Tree with negative root but positive path sum
3. Tree with multiple negative values

Each test case demonstrates different scenarios and edge cases for the problem. 