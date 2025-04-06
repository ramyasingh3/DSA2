# Binary Tree Vertical Order Traversal

## Problem Description
Given a binary tree, return the vertical order traversal of its nodes' values. For each vertical line, nodes are ordered from top to bottom. If two nodes are in the same row and column, they are ordered by their values.

## Examples

### Example 1: Tree with Multiple Levels
```
    3
   / \
  9   20
     /  \
    15   7
```
Vertical order traversal: [[9], [3, 15], [20], [7]]

### Example 2: Tree with Overlapping Nodes
```
    1
   / \
  2   3
 / \   \
4   5   6
```
Vertical order traversal: [[4], [2], [1, 5], [3], [6]]

## Solution Approach
The solution uses a breadth-first search (BFS) approach with coordinate tracking:

1. **Coordinate System**:
   - Root node is at (0, 0)
   - Left child is at (row + 1, col - 1)
   - Right child is at (row + 1, col + 1)

2. **Basic Vertical Order**:
   - Use BFS to traverse the tree
   - Track column index for each node
   - Group nodes by their column index
   - Sort columns and return values

3. **Vertical Order with Level Consideration**:
   - Track both row and column indices
   - Store nodes with their coordinates
   - Sort by column, then by row, then by value
   - Return values in sorted order

4. **Time Complexity**: O(N log N), where N is the number of nodes
   - O(N) for BFS traversal
   - O(N log N) for sorting nodes in each column

5. **Space Complexity**: O(N)
   - O(N) for queue and dictionary storage
   - O(N) for result storage

## Usage
```python
# Create a binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

# Create Solution instance
solution = Solution()

# Get vertical order traversal
vertical_order = solution.verticalOrder(root)
print(f"Vertical order: {vertical_order}")

# Get vertical order with level consideration
vertical_order_level = solution.verticalOrderWithLevel(root)
print(f"Vertical order with level: {vertical_order_level}")
```

## Test Cases
The implementation includes three test cases:

1. **Tree with Multiple Levels**:
   - Tests basic vertical order traversal
   - Expected output: [[9], [3, 15], [20], [7]]

2. **Tree with Overlapping Nodes**:
   - Tests handling of nodes in same column
   - Expected output: [[4], [2], [1, 5], [3], [6]]

3. **Tree with Same Structure**:
   - Tests consistency of implementation
   - Expected output: [[4], [2], [1, 5], [3], [6]]

## Running the Tests
```bash
python vertical_order_traversal.py
```

## Implementation Details
The implementation includes:
1. `TreeNode` class for creating binary tree nodes
2. `Solution` class with two methods:
   - `verticalOrder`: Basic vertical order traversal
   - `verticalOrderWithLevel`: Vertical order with level consideration
3. Helper functions:
   - `print_tree`: Visualizes the tree structure
   - `build_test_tree*`: Creates test trees
4. Comprehensive test cases with visual output

## Common Applications
- Tree visualization
- Hierarchical data representation
- Tree structure analysis
- UI layout optimization 