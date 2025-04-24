# Search in Rotated Sorted Array

## Problem Statement
There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (1 <= k < nums.length) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`.

Given the array `nums` after the rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with O(log n) runtime complexity.

### Example 1:
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

### Example 2:
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

### Example 3:
```
Input: nums = [1], target = 0
Output: -1
```

## Approach
The solution uses a modified binary search:
1. Find the pivot point where the array is rotated
2. Determine which half of the array is sorted
3. Check if the target is in the sorted half
4. If yes, perform regular binary search in that half
5. If no, search in the other half
6. Repeat until target is found or search space is exhausted

## Time Complexity
- O(log n), where n is the length of the array
- We perform binary search twice:
  - Once to find the pivot
  - Once to find the target
- Each binary search takes O(log n) time

## Space Complexity
- O(1)
- We only use constant extra space for the pointers and variables
- The search is done in-place 