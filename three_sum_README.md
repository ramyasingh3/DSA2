# 3Sum

## Problem Description
Given an array of integers `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

## Examples
1. Basic case:
   ```
   Input: nums = [-1,0,1,2,-1,-4]
   Output: [[-1,-1,2],[-1,0,1]]
   ```

2. No solution:
   ```
   Input: nums = [1,2,3,4,5]
   Output: []
   ```

3. All zeros:
   ```
   Input: nums = [0,0,0,0]
   Output: [[0,0,0]]
   ```

## Solution Approaches

### 1. Brute Force (O(n³))
- Check all possible triplets
- Time Complexity: O(n³)
- Space Complexity: O(1)
- Best for understanding the problem

### 2. Two Pointers (O(n²))
- Sort the array
- Use three pointers (i, left, right)
- Skip duplicates
- Time Complexity: O(n²)
- Space Complexity: O(1)
- Best for most practical cases

### 3. Hash Set (O(n²))
- Sort the array
- Use hash set to store complements
- Skip duplicates
- Time Complexity: O(n²)
- Space Complexity: O(n)
- Best when memory is not a concern

## Time Complexity
- Brute Force: O(n³)
- Two Pointers: O(n²)
- Hash Set: O(n²)

## Space Complexity
- Brute Force: O(1)
- Two Pointers: O(1)
- Hash Set: O(n)

## Usage
```python
from three_sum import Solution

solution = Solution()

# Using brute force
print(solution.three_sum_brute_force([-1,0,1,2,-1,-4]))  # Output: [[-1,-1,2],[-1,0,1]]

# Using two pointers
print(solution.three_sum_two_pointers([-1,0,1,2,-1,-4]))  # Output: [[-1,-1,2],[-1,0,1]]

# Using hash set
print(solution.three_sum_hash([-1,0,1,2,-1,-4]))  # Output: [[-1,-1,2],[-1,0,1]]
```

## Common Applications
- Finding triplets in data analysis
- Financial calculations
- Resource allocation
- Scheduling problems
- Network routing
- Database queries 