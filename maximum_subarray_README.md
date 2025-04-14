# Maximum Subarray Sum

## Problem Description
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## Example
```python
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6
```

## Solution Approach: Kadane's Algorithm
The solution uses Kadane's Algorithm, which is an efficient way to solve the maximum subarray problem with the following steps:

1. Initialize variables:
   - `current_sum`: tracks the current subarray sum
   - `max_sum`: tracks the maximum sum found so far
   - Track indices to return the actual subarray

2. Iterate through the array:
   - If `current_sum` becomes negative, reset it (start fresh from current element)
   - Otherwise, add the current element to `current_sum`
   - Update `max_sum` if `current_sum` becomes larger

3. Return both the maximum sum and the subarray that produces it

## Time Complexity
- O(n) where n is the length of the input array
- We only need one pass through the array

## Space Complexity
- O(1) for computing just the sum
- O(k) for storing the result subarray, where k is the length of the maximum subarray

## Edge Cases Handled
- Empty array
- Array with all negative numbers
- Single element array
- Array with all positive numbers
- Array with mixed positive and negative numbers
