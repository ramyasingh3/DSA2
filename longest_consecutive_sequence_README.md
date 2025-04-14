# Longest Consecutive Sequence

## Problem Description
Given an unsorted array of integers `nums`, find the length of the longest consecutive elements sequence and return both the length and the sequence itself.

## Examples
```python
Input: nums = [100,4,200,1,3,2]
Output: 4
Sequence: [1,2,3,4]

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Sequence: [0,1,2,3,4,5,6,7,8]
```

## Solution Approach
The solution uses a hash set to achieve O(n) time complexity with these key steps:

1. Convert the input array to a hash set for O(1) lookups
2. For each number in the set:
   - Only start checking sequences if it's the start of a sequence (no number-1 exists)
   - Keep incrementing and checking for consecutive numbers
   - Track the current sequence length and numbers
3. Return the longest sequence found

### Key Optimizations
- Using a hash set for O(1) lookups
- Only starting sequences from the smallest number prevents redundant checks
- Avoiding sorting keeps time complexity at O(n)

## Time Complexity
- O(n) where n is the length of the input array
- Each number is visited at most twice:
  - Once when adding to the set
  - Once when checking for consecutive numbers

## Space Complexity
- O(n) for storing the hash set
- O(k) for storing the longest sequence found, where k is the length of that sequence

## Edge Cases Handled
- Empty array
- Single element array
- Array with duplicates
- Array with no consecutive sequences
- Array that is already sorted
- Array in reverse order
