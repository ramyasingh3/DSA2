# Longest Increasing Subsequence

## Problem Description
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

## Examples
```
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: The longest increasing subsequence is [2, 5, 7, 101], therefore the length is 4.

Input: nums = [0, 1, 0, 3, 2, 3]
Output: 4
Explanation: The longest increasing subsequence is [0, 1, 2, 3], therefore the length is 4.

Input: nums = [7, 7, 7, 7, 7, 7, 7]
Output: 1
Explanation: The longest increasing subsequence is [7], therefore the length is 1.
```

## Constraints
- 1 <= nums.length <= 2500
- -10⁴ <= nums[i] <= 10⁴

## Approach 1: Dynamic Programming
1. Create an array `dp` where `dp[i]` represents the length of LIS ending at index i
2. Initialize dp[i] = 1 for all i (each element is a subsequence of length 1)
3. For each index i:
   - For each index j < i:
     - If nums[i] > nums[j]:
       - dp[i] = max(dp[i], dp[j] + 1)
4. Return the maximum value in dp array

## Approach 2: Binary Search
1. Create an array `dp` where `dp[i]` represents the smallest tail of all increasing subsequences of length i+1
2. For each number in nums:
   - Use binary search to find the first index in dp where dp[index] >= num
   - If num is larger than all elements in dp:
     - Append num to dp
   - Else:
     - Replace dp[index] with num
3. Return the length of dp array

## Time and Space Complexity
### Approach 1 (Dynamic Programming)
- Time Complexity: O(n²)
  - For each element, we check all previous elements
  - Each comparison takes O(1) time
- Space Complexity: O(n)
  - We need to store the dp array

### Approach 2 (Binary Search)
- Time Complexity: O(n log n)
  - For each element, we perform binary search
  - Binary search takes O(log n) time
- Space Complexity: O(n)
  - We need to store the dp array

## Key Points
- This is a classic dynamic programming problem
- The binary search approach is more efficient
- The solution can be extended to find the actual subsequence
- We need to handle edge cases (empty array, single element)
- The order of elements matters
- Elements can be skipped in the subsequence

## Common Applications
- Stock price analysis
- DNA sequence analysis
- Pattern recognition
- Data compression
- Network routing
- Game theory
- Bioinformatics

## Example Walkthrough
For nums = [10, 9, 2, 5, 3, 7, 101, 18]:

### Dynamic Programming Approach:
1. Initialize dp array:
   ```
   [1, 1, 1, 1, 1, 1, 1, 1]
   ```
2. Fill the dp array:
   ```
   [1, 1, 1, 2, 2, 3, 4, 4]
   ```
3. Result: 4

### Binary Search Approach:
1. Initialize dp array: []
2. Process each number:
   - 10: [10]
   - 9: [9]
   - 2: [2]
   - 5: [2, 5]
   - 3: [2, 3]
   - 7: [2, 3, 7]
   - 101: [2, 3, 7, 101]
   - 18: [2, 3, 7, 18]
3. Result: 4

## Finding the Actual Subsequence
To find the actual longest increasing subsequence:
1. Use the dp array to track the length of LIS ending at each index
2. Use a prev array to store the previous index for each element
3. Find the index of the maximum value in dp
4. Reconstruct the subsequence by following the prev pointers
5. Reverse the result to get the subsequence in correct order 