# Binary Tree Level Order Traversal

## Problem Description
Given a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level). Additionally, implement a spiral (zigzag) level order traversal where alternate levels are traversed in opposite directions.

## Examples

### Example 1: Simple Balanced Tree
```
Tree:
     1
    / \
   2   3
  / \
 4   5

Level Order: [[1], [2, 3], [4, 5]]
Spiral Order: [[1], [3, 2], [4, 5]]
```

### Example 2: Unbalanced Tree
```
Tree:
        1
       / \
      2   3
     /     \
    4       5
   /         \
  6           7

Level Order: [[1], [2, 3], [4, 5], [6, 7]]
Spiral Order: [[1], [3, 2], [4, 5], [7, 6]]
```

### Example 3: Complex Tree
```
Tree:
     1
    / \
   2   3
  /   / \
 4   5   6
    /     \
   7       8

Level Order: [[1], [2, 3], [4, 5, 6], [7, 8]]
Spiral Order: [[1], [3, 2], [4, 5, 6], [8, 7]]
```

## Solution Approach

### Regular Level Order Traversal
1. Use a queue to store nodes at each level
2. For each node:
   - Add its value to the current level's list
   - Add its children to the queue
3. Keep track of levels using a tuple (node, level) in the queue

### Spiral (Zigzag) Level Order Traversal
1. Similar to regular level order traversal
2. Additional steps:
   - Process entire level at once using level_size
   - Reverse alternate levels (odd-numbered levels)
   - Store result level by level

## Key Points
1. BFS (Breadth-First Search) approach
2. Queue-based implementation
3. Level tracking
4. Handling of null nodes
5. Efficient array operations

## Time Complexity
- Both traversals: O(N) where N is the number of nodes
- Each node is processed exactly once
- Array operations (append, reverse) are O(1) or O(k) where k is level size

## Space Complexity
- O(W) where W is the maximum width of the tree
- In worst case (complete binary tree), this becomes O(N/2) ≈ O(N)
- Queue stores at most one level of nodes at a time

## Usage
```python
# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Create solution object
solution = Solution()

# Get level order traversal
level_order = solution.levelOrder(root)  # Returns [[1], [2, 3]]

# Get spiral order traversal
spiral_order = solution.levelOrderSpiral(root)  # Returns [[1], [3, 2]]
```

## Implementation Details

### Node Structure
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

### Main Functions
1. `levelOrder(root)`:
   - Regular level order traversal
   - Returns list of lists (levels)

2. `levelOrderSpiral(root)`:
   - Zigzag level order traversal
   - Alternates direction by level

### Helper Functions
1. `build_test_tree1()`, `build_test_tree2()`, `build_test_tree3()`:
   - Create different tree structures for testing
   - Include visual representations

2. `print_tree()`:
   - Prints tree structure visually
   - Helps verify test cases

## Test Cases
The implementation includes three test cases:
1. Simple balanced tree
2. Unbalanced tree with deep paths
3. Complex tree with multiple levels

Each test case demonstrates:
- Different tree structures
- Both regular and spiral traversals
- Visual tree representation
- Expected outputs

## Running the Tests
```bash
python level_order_traversal.py
```

## Common Applications
1. Tree visualization
2. Level-based tree processing
3. Tree serialization
4. Web UI rendering of tree structures
5. File system representation 