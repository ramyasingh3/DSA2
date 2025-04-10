# Remove Duplicates from Sorted Array

## Problem Description
Given a sorted array `nums`, remove the duplicates in-place such that each element appears only once and returns the new length.

## Examples
1. Basic case:
   ```
   Input: nums = [1, 1, 2]
   Output: 2, nums = [1, 2]
   ```

2. All duplicates:
   ```
   Input: nums = [1, 1, 1, 1]
   Output: 1, nums = [1]
   ```

3. No duplicates:
   ```
   Input: nums = [1, 2, 3, 4]
   Output: 4, nums = [1, 2, 3, 4]
   ```

## Solution Approaches

### 1. Two Pointers (O(n))
- Uses two pointers to track positions
- Time Complexity: O(n)
- Space Complexity: O(1)
- Best for most cases

### 2. Set-based (O(n))
- Uses set to remove duplicates
- Time Complexity: O(n)
- Space Complexity: O(n)
- Best for readability

### 3. Groupby (O(n))
- Uses itertools.groupby
- Time Complexity: O(n)
- Space Complexity: O(n)
- Best for Python-specific solutions

## Time Complexity
- All approaches: O(n)
- n is the length of the array

## Space Complexity
- Two Pointers: O(1)
- Set-based: O(n)
- Groupby: O(n)

## Usage
```python
from remove_duplicates_sorted_array import Solution

solution = Solution()
nums = [1, 1, 2]

# Using two pointers
length = solution.remove_duplicates_two_pointers(nums)
print(f"New length: {length}")
print(f"Modified array: {nums[:length]}")

# Using set-based
length = solution.remove_duplicates_set(nums)
print(f"New length: {length}")
print(f"Modified array: {nums[:length]}")

# Using groupby
length = solution.remove_duplicates_groupby(nums)
print(f"New length: {length}")
print(f"Modified array: {nums[:length]}")
```

## Common Applications
- Data cleaning
- Array manipulation
- Memory optimization
- In-place algorithms
- Interview preparation
- System design 