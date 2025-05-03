# Longest Increasing Subsequence (LIS)

## Problem Description
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

## Examples
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,5,7,101], therefore the length is 4.

Input: nums = [0,1,0,3,2,3]
Output: 4
Explanation: The longest increasing subsequence is [0,1,2,3], therefore the length is 4.

Input: nums = [7,7,7,7,7,7,7]
Output: 1
Explanation: The longest increasing subsequence is [7], therefore the length is 1.
```

## Constraints
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4

## Approach 1: Dynamic Programming (O(n²))
1. Create a dp array where dp[i] represents the length of LIS ending at index i
2. Initialize all dp values to 1 (each element is a subsequence of length 1)
3. For each position i:
   - Check all previous positions j
   - If nums[i] > nums[j], update dp[i] = max(dp[i], dp[j] + 1)
4. Return the maximum value in dp array

## Approach 2: Binary Search (O(n log n))
1. Create a dp array where dp[i] represents the smallest possible tail value for all increasing subsequences of length i+1
2. For each number in nums:
   - Use binary search to find the first element in dp that is greater than or equal to the current number
   - If found, replace it with the current number
   - If not found, append the current number to dp
3. The length of dp array is the answer

## Time and Space Complexity
### Approach 1 (Dynamic Programming)
- Time Complexity: O(n²)
- Space Complexity: O(n)

### Approach 2 (Binary Search)
- Time Complexity: O(n log n)
- Space Complexity: O(n)

## Key Points
- A subsequence doesn't need to be contiguous
- The order of elements must be preserved
- The solution must be strictly increasing
- The binary search approach is more efficient for large inputs
- Both approaches handle edge cases (empty array, single element)

## Common Applications
- Pattern recognition
- Bioinformatics
- Data compression
- Network routing
- Stock market analysis
- Machine learning

## Example Walkthrough
For nums = [10,9,2,5,3,7,101,18]:

### Dynamic Programming Approach:
1. Initialize dp = [1,1,1,1,1,1,1,1]
2. For i=1: dp = [1,1,1,1,1,1,1,1]
3. For i=2: dp = [1,1,1,1,1,1,1,1]
4. For i=3: dp = [1,1,1,2,1,1,1,1]
5. For i=4: dp = [1,1,1,2,2,1,1,1]
6. For i=5: dp = [1,1,1,2,2,3,1,1]
7. For i=6: dp = [1,1,1,2,2,3,4,1]
8. For i=7: dp = [1,1,1,2,2,3,4,4]
9. Return max(dp) = 4

### Binary Search Approach:
1. dp = [10]
2. dp = [9]
3. dp = [2]
4. dp = [2,5]
5. dp = [2,3]
6. dp = [2,3,7]
7. dp = [2,3,7,101]
8. dp = [2,3,7,18]
9. Return len(dp) = 4 