# Maximum Subarray

## Problem Description
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

### Examples
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23
```

## Approach
1. Kadane's Algorithm:
   - Keep track of current sum and maximum sum
   - For each number:
     - Add it to current sum
     - Update maximum sum if current sum is greater
     - Reset current sum to 0 if it becomes negative

### Key Points
- O(n) time complexity
- O(1) space complexity
- Handles negative numbers
- Single pass solution

## Time Complexity
- O(n) where n is the length of the array
  - We process each element exactly once

## Space Complexity
- O(1) constant space
  - We only store current and maximum sums

## Edge Cases Handled
- Empty array
- Array with all negative numbers
- Single element array
- Array with all positive numbers
- Array with mixed positive and negative numbers
