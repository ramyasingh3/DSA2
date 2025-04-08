# Merge Two Sorted Lists

## Problem Description
Given two sorted linked lists `l1` and `l2`, merge them into one sorted list. The list should be made by splicing together the nodes of the first two lists.

## Examples
1. Basic case:
   ```
   Input: l1 = [1,2,4], l2 = [1,3,4]
   Output: [1,1,2,3,4,4]
   ```

2. One empty list:
   ```
   Input: l1 = [], l2 = [0]
   Output: [0]
   ```

3. Both empty lists:
   ```
   Input: l1 = [], l2 = []
   Output: []
   ```

## Solution Approaches

### 1. Iterative Solution (O(n+m))
- Use a dummy node to build the merged list
- Compare nodes from both lists and append the smaller one
- Time Complexity: O(n+m)
- Space Complexity: O(1)
- Best for performance and memory efficiency

### 2. Recursive Solution (O(n+m))
- Recursively merge the lists by comparing nodes
- Time Complexity: O(n+m)
- Space Complexity: O(n+m) (stack space)
- Best for code elegance and understanding

## Time Complexity
- Both solutions: O(n+m), where n and m are lengths of the input lists

## Space Complexity
- Iterative: O(1)
- Recursive: O(n+m) (stack space)

## Usage
```python
from merge_sorted_lists import Solution, ListNode

solution = Solution()

# Create lists
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

# Using iterative solution
merged = solution.merge_two_lists_iterative(l1, l2)

# Using recursive solution
merged = solution.merge_two_lists_recursive(l1, l2)
```

## Common Applications
- Merging sorted data streams
- Merge sort implementation
- Database query optimization
- External sorting algorithms
- Priority queue implementations 