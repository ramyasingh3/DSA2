# Binary Tree Level Order Traversal

## Problem Description
Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).

## Examples
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Explanation:
    3
   / \
  9  20
     /  \
    15   7

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
```

## Constraints
- The number of nodes in the tree is in the range [0, 2000]
- -1000 <= Node.val <= 1000

## Approach 1: Queue-based BFS
1. Use a queue to store nodes at each level
2. Process nodes level by level:
   - Get current level size
   - Process all nodes at current level
   - Add their children to queue
3. Time Complexity: O(n)
4. Space Complexity: O(w) where w is the maximum width of the tree

## Approach 2: Recursive DFS
1. Use recursion to traverse the tree
2. Keep track of current level
3. Add nodes to appropriate level lists
4. Time Complexity: O(n)
5. Space Complexity: O(h) where h is the height of the tree

## Approach 3: DFS with Pre-calculated Height
1. Calculate tree height first
2. Create result array with correct size
3. Fill levels using DFS
4. Time Complexity: O(n)
5. Space Complexity: O(h)

## Approach 4: Zigzag Level Order
1. Similar to queue-based approach
2. Alternate between left-to-right and right-to-left
3. Reverse alternate levels
4. Time Complexity: O(n)
5. Space Complexity: O(w)

## Time and Space Complexity Comparison
| Approach          | Time Complexity | Space Complexity | Notes                    |
|------------------|-----------------|------------------|--------------------------|
| Queue-based BFS  | O(n)           | O(w)            | Most intuitive          |
| Recursive DFS    | O(n)           | O(h)            | Uses recursion stack    |
| DFS with Height  | O(n)           | O(h)            | Pre-allocates space    |
| Zigzag Order     | O(n)           | O(w)            | Handles special pattern |

## Key Points
- This is a fundamental tree traversal problem
- Multiple valid approaches exist
- Edge cases to consider:
  - Empty tree
  - Single node
  - Perfect binary tree
  - Skewed tree (left/right)
  - Irregular tree
- BFS vs DFS tradeoffs

## Common Applications
- Tree visualization
- Level-wise processing
- Tree serialization
- UI rendering (hierarchical)
- File system traversal
- Network topology analysis
- Organization hierarchy

## Example Walkthrough
For tree:
```
    3
   / \
  9  20
     /  \
    15   7
```

### Queue-based BFS:
1. Start with root (3):
   - Queue: [3]
   - Result: []
2. Process level 0:
   - Add 3 to result
   - Add children to queue
   - Queue: [9,20]
   - Result: [[3]]
3. Process level 1:
   - Add 9,20 to result
   - Add children to queue
   - Queue: [15,7]
   - Result: [[3],[9,20]]
4. Process level 2:
   - Add 15,7 to result
   - Queue: []
   - Result: [[3],[9,20],[15,7]]

## Follow-up Questions
1. What if we need to print the tree vertically?
2. What if we need to find the largest value in each level?
3. What if we need to connect nodes at the same level?
4. What if we need to find the average of each level?
5. What if we need to find the leftmost value in each level?

## Optimization Tips
1. Use queue for level-wise processing
2. Consider recursion for simpler code
3. Handle edge cases early
4. Pre-calculate height if needed
5. Use deque for O(1) operations
6. Consider memory vs speed tradeoffs
7. Use level size for batch processing 