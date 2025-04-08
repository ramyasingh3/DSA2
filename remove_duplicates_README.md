# Remove Duplicates from Sorted List

## Problem Description
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

## Examples
1. Basic case:
   ```
   Input: head = [1,1,2]
   Output: [1,2]
   ```

2. Multiple duplicates:
   ```
   Input: head = [1,1,2,3,3]
   Output: [1,2,3]
   ```

3. No duplicates:
   ```
   Input: head = [1,2,3,4,5]
   Output: [1,2,3,4,5]
   ```

## Solution Approaches

### 1. Iterative Solution (O(n))
- Use a single pointer to track current node
- Compare current node with next node
- Skip duplicates by updating next pointer
- Time Complexity: O(n)
- Space Complexity: O(1)
- Best for performance and memory efficiency

### 2. Recursive Solution (O(n))
- Recursively process the list
- Skip duplicates by returning next node
- Time Complexity: O(n)
- Space Complexity: O(n) (stack space)
- Best for code elegance and understanding

## Time Complexity
- Both solutions: O(n), where n is the length of the list

## Space Complexity
- Iterative: O(1)
- Recursive: O(n) (stack space)

## Usage
```python
from remove_duplicates import Solution, ListNode

solution = Solution()

# Create a list
head = ListNode(1, ListNode(1, ListNode(2)))

# Using iterative solution
result = solution.delete_duplicates_iterative(head)

# Using recursive solution
result = solution.delete_duplicates_recursive(head)
```

## Common Applications
- Data cleaning and preprocessing
- Database query optimization
- Stream processing
- Memory optimization
- Data compression 