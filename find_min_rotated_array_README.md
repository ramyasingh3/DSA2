# Find Minimum in Rotated Sorted Array

## Problem Statement
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:
- `[4,5,6,7,0,1,2]` if it was rotated 4 times.
- `[0,1,2,4,5,6,7]` if it was rotated 7 times.

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

### Example 1:
```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

### Example 2:
```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

### Example 3:
```
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
```

## Approach
The solution uses a modified binary search:
1. Initialize two pointers, left and right
2. While left < right:
   - Calculate mid point
   - Compare nums[mid] with nums[right]
   - If nums[mid] > nums[right], the minimum is in the right half
   - Otherwise, the minimum is in the left half (including mid)
3. When left == right, we've found the minimum element

## Time Complexity
- O(log n), where n is the length of the array
- We perform binary search once, halving the search space each time

## Space Complexity
- O(1)
- We only use constant extra space for the pointers and variables
- The search is done in-place 