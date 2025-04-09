# Reverse Linked List

## Problem Description
Given the head of a singly linked list, reverse the list and return the reversed list.

## Examples
1. Simple case:
   ```
   Input: 1 -> 2 -> 3 -> 4 -> 5
   Output: 5 -> 4 -> 3 -> 2 -> 1
   ```

2. Single node:
   ```
   Input: 1
   Output: 1
   ```

3. Empty list:
   ```
   Input: None
   Output: None
   ```

## Solution Approaches

### 1. Iterative Approach (O(n))
- Uses three pointers: prev, current, and next
- Time Complexity: O(n)
- Space Complexity: O(1)
- Best for most cases

### 2. Recursive Approach (O(n))
- Uses recursion to reverse the list
- Time Complexity: O(n)
- Space Complexity: O(n)
- Best for understanding recursion

### 3. Stack-based Approach (O(n))
- Uses a stack to reverse the list
- Time Complexity: O(n)
- Space Complexity: O(n)
- Best for educational purposes

## Time Complexity
- All approaches: O(n)
- n is the number of nodes in the list

## Space Complexity
- Iterative: O(1)
- Recursive: O(n) due to recursion stack
- Stack-based: O(n) due to stack usage

## Usage
```python
from reverse_linked_list import Solution, ListNode

# Create a linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Reverse the list
solution = Solution()
reversed_head = solution.reverse_list_iterative(head)

# Print the reversed list
current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next
```

## Common Applications
- Linked list manipulation
- Data structure implementations
- Algorithm design
- Memory management
- System design
- Interview preparation 