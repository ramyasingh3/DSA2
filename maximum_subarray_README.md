# Maximum Subarray

## Problem Description
Given an integer array `nums`, find the subarray with the largest sum, and return its sum. A subarray is a contiguous non-empty sequence of elements within an array.

## Examples
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum = 1.

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum = 23.
```

## Constraints
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

## Approach 1: Kadane's Algorithm
1. Initialize variables for current sum and maximum sum
2. For each number, decide whether to:
   - Start a new subarray (take current number)
   - Continue previous subarray (add to current sum)
3. Update maximum sum if current sum is larger
4. Time Complexity: O(n)
5. Space Complexity: O(1)

## Approach 2: Dynamic Programming
1. Create a DP array where dp[i] represents max sum ending at index i
2. For each number, decide whether to:
   - Start new subarray: dp[i] = nums[i]
   - Continue previous subarray: dp[i] = dp[i-1] + nums[i]
3. Track maximum sum seen so far
4. Time Complexity: O(n)
5. Space Complexity: O(n)

## Approach 3: Divide and Conquer
1. Divide array into two halves
2. Recursively find maximum subarray sum in:
   - Left half
   - Right half
   - Crossing the middle
3. Return maximum of the three sums
4. Time Complexity: O(n log n)
5. Space Complexity: O(log n)

## Time and Space Complexity Comparison
| Approach          | Time Complexity | Space Complexity | Notes                    |
|------------------|-----------------|------------------|--------------------------|
| Kadane's         | O(n)           | O(1)            | Most efficient           |
| Dynamic Programming| O(n)          | O(n)            | Uses extra space         |
| Divide & Conquer | O(n log n)     | O(log n)        | Due to recursion stack   |

## Key Points
- This is a fundamental dynamic programming problem
- Multiple valid approaches exist
- Edge cases to consider:
  - Empty array
  - Single element
  - All negative numbers
  - All positive numbers
  - Alternating numbers
- The solution is unique for each input

## Common Applications
- Stock market analysis
- Signal processing
- Data mining
- Pattern recognition
- Time series analysis
- Resource allocation
- Performance optimization

## Example Walkthrough
For nums = [-2,1,-3,4,-1,2,1,-5,4]:

### Kadane's Algorithm:
1. Start with nums[0] = -2:
   - current_sum = -2, max_sum = -2
2. Process 1:
   - current_sum = max(1, -2 + 1) = 1
   - max_sum = 1
3. Process -3:
   - current_sum = max(-3, 1 + -3) = -2
   - max_sum = 1
4. Process 4:
   - current_sum = max(4, -2 + 4) = 4
   - max_sum = 4
5. Continue until end...
Final result: 6 (subarray [4,-1,2,1])

## Follow-up Questions
1. What if we need to find the actual subarray?
2. What if we need to find all subarrays with sum greater than K?
3. What if we need to find the maximum product subarray?
4. What if we need to find the maximum sum circular subarray?
5. What if we need to find the maximum sum with at most K elements?

## Optimization Tips
1. Use Kadane's algorithm for optimal time complexity
2. Handle edge cases early
3. Use early returns when possible
4. Consider using bit manipulation for optimization
5. Implement parallel processing for large arrays
6. Use sliding window for variants
7. Consider space-time tradeoffs based on constraints
