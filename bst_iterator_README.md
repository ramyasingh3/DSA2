# Binary Search Tree Iterator

## Problem Description
Design and implement an iterator for Binary Search Tree (BST) that supports standard iterator operations in an efficient manner.

## Features
1. `next()` - Returns the next smallest number in the BST
2. `hasNext()` - Returns whether there exists a next number
3. `peek()` - Returns the next number without advancing the iterator

## Implementation Details

### Data Structures Used
1. **Stack**: Used to maintain the path to the next smallest element
2. **Binary Search Tree**: The underlying data structure being traversed

### Key Concepts
1. **Controlled Inorder Traversal**:
   - Instead of generating all elements at once
   - Only processes nodes when needed
   - Maintains O(h) space complexity

2. **Stack-based Iteration**:
   - Stores path to current node
   - Enables efficient navigation
   - Supports peek operation

### Time Complexity
- Constructor: O(h) - where h is tree height
- next(): O(1) amortized
- hasNext(): O(1)
- peek(): O(1)

### Space Complexity
- O(h) where h is the height of the BST
- In worst case (skewed tree): O(n)
- In balanced tree: O(log n)

## Edge Cases Handled
- Empty tree
- Single node tree
- Left-heavy tree
- Right-heavy tree
- Balanced tree
- Null values in tree

## Usage Example
```python
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

iterator = BSTIterator(root)
print(iterator.next())    # 3
print(iterator.next())    # 7
print(iterator.peek())    # 9
print(iterator.hasNext()) # True
```

## Applications
1. In-order traversal of BST
2. Memory-efficient tree iteration
3. Lazy evaluation of tree elements
4. Stream processing of BST data
5. Iterator pattern implementation

## Design Decisions
1. Used stack instead of recursion for better space efficiency
2. Implemented peek() for look-ahead functionality
3. Lazy loading of nodes for better performance
4. Proper null handling for robustness
5. Amortized O(1) operations for efficiency

## Testing Strategy
1. Basic operations on standard BST
2. Edge cases (empty tree, single node)
3. Different tree shapes (left-heavy, balanced)
4. Sequence of operations
5. Invalid operations handling
