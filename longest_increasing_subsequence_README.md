# Longest Increasing Subsequence (LIS)

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
- -10^4 <= nums[i] <= 10^4

## Approach 1: Dynamic Programming
1. Create an array `dp` where `dp[i]` represents the length of LIS ending at index i
2. Initialize all elements in dp to 1 (each element is a subsequence of length 1)
3. For each position i:
   - Check all previous positions j
   - If nums[i] > nums[j], update dp[i] = max(dp[i], dp[j] + 1)
4. Return the maximum value in dp

## Approach 2: Binary Search
1. Create an array `sub` to store the smallest possible tail value for all increasing subsequences
2. For each number in nums:
   - Use binary search to find the first element in sub that is greater than or equal to the number
   - If the number is greater than all elements in sub, append it
   - Otherwise, replace the first element that is greater than or equal to the number
3. Return the length of sub

## Time and Space Complexity
### Approach 1 (Dynamic Programming)
- Time Complexity: O(n²)
  - We need to check all previous elements for each position
- Space Complexity: O(n)
  - We need to store the dp array

### Approach 2 (Binary Search)
- Time Complexity: O(n log n)
  - For each element, we perform binary search
- Space Complexity: O(n)
  - We need to store the sub array

## Key Points
- This is a classic dynamic programming problem
- The binary search approach is more efficient
- The solution can be extended to find the actual subsequence
- The order of elements matters
- We need to handle edge cases (empty array, single element)

## Common Applications
- Sequence analysis
- Pattern recognition
- Data compression
- Bioinformatics
- Stock market analysis
- Route planning
- Game theory

## Example Walkthrough
For nums = [10, 9, 2, 5, 3, 7, 101, 18]:

### Dynamic Programming Approach:
1. Initialize dp array:
   ```
   [1, 1, 1, 1, 1, 1, 1, 1]
   ```
2. Fill the array:
   ```
   [1, 1, 1, 2, 2, 3, 4, 4]
   ```
3. Result: 4

### Binary Search Approach:
1. Process each number:
   - 10: [10]
   - 9: [9]
   - 2: [2]
   - 5: [2, 5]
   - 3: [2, 3]
   - 7: [2, 3, 7]
   - 101: [2, 3, 7, 101]
   - 18: [2, 3, 7, 18]
2. Result: 4

## Finding the Actual Subsequence
To find the actual LIS:
1. Use dynamic programming with an additional array to store previous indices
2. For each position:
   - Update dp[i] and store the previous index that led to this length
3. Find the index with maximum length
4. Reconstruct the subsequence by following the previous indices
5. Return the reversed subsequence 