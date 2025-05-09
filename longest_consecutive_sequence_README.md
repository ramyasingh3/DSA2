# Longest Consecutive Sequence

## Problem Description
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.

A consecutive sequence is a sequence of numbers where each number is exactly one more than the previous number. For example, [1, 2, 3, 4] is a consecutive sequence, but [1, 3, 4] is not.

## Examples

### Example 1:
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

### Example 2:
```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Length = 9.
```

## Solution Approach

The solution uses a hash set approach to achieve O(n) time complexity:

1. Convert the input array to a set for O(1) lookups
2. For each number in the set:
   - Only start checking sequences from the smallest number in the sequence
   - This is done by checking if the previous number (num - 1) exists in the set
   - If it doesn't exist, this number could be the start of a new sequence
3. For each potential sequence start:
   - Count how many consecutive numbers exist
   - Update the maximum length if this sequence is longer

The key insight is that we only need to check sequences starting from their smallest number. This ensures we don't check the same sequence multiple times and maintains O(n) time complexity.

## Time and Space Complexity

- **Time Complexity**: O(n)
  - Converting array to set: O(n)
  - Each number is visited at most twice:
    - Once when we check if it's a sequence start
    - Once when we count it as part of a sequence
  - Therefore, the total time is O(n)

- **Space Complexity**: O(n)
  - We need to store all numbers in a set
  - In the worst case, we store all n numbers

## Edge Cases

1. Empty array
2. Single element array
3. Array with no consecutive numbers
4. Array with duplicate numbers
5. Array with negative numbers
6. Array with all same numbers

## Implementation Notes

- The solution uses Python's built-in `set` data structure for O(1) lookups
- We don't need to store the actual sequence, only its length
- The solution handles duplicate numbers automatically by using a set
- The solution works with both positive and negative numbers
- The order of numbers in the input array doesn't matter

## Alternative Approaches

1. **Sorting Approach**:
   - Sort the array and find consecutive sequences
   - Time Complexity: O(n log n)
   - Space Complexity: O(1) if sorting in-place
   - Simpler to implement but doesn't meet the O(n) requirement

2. **Union-Find Approach**:
   - Use Union-Find data structure to group consecutive numbers
   - Time Complexity: O(n) with path compression
   - Space Complexity: O(n)
   - More complex to implement but could be useful for related problems
