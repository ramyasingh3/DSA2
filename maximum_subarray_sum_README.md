# Maximum Subarray Sum

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

### Example 1:
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.
```

### Example 2:
```
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum = 1.
```

### Example 3:
```
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum = 23.
```

## Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## Solution Approach
The solution uses Kadane's Algorithm to solve this problem efficiently:

1. Initialize two variables:
   - `max_so_far`: keeps track of the maximum sum found so far
   - `max_ending_here`: keeps track of the maximum sum ending at the current position

2. For each element in the array:
   - Update `max_ending_here` to be the maximum of:
     - The current element
     - The sum of current element and `max_ending_here`
   - Update `max_so_far` to be the maximum of `max_so_far` and `max_ending_here`

3. Return `max_so_far` as the result

## Time and Space Complexity
- Time Complexity: O(n), where n is the length of the input array
- Space Complexity: O(1), as we only use two variables regardless of input size

## Implementation
The solution is implemented in Python using Kadane's Algorithm. The code includes test cases to verify the implementation. 