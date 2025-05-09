# Product of Array Except Self

## Problem Description
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

## Examples

### Example 1:
```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: 
- answer[0] = 2 * 3 * 4 = 24
- answer[1] = 1 * 3 * 4 = 12
- answer[2] = 1 * 2 * 4 = 8
- answer[3] = 1 * 2 * 3 = 6
```

### Example 2:
```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

## Solution Approach

The solution uses a two-pass approach with prefix and suffix products:

1. First Pass (Prefix Products):
   - Initialize an array `answer` with all 1's
   - For each position i, store the product of all numbers before i
   - This is done by maintaining a running prefix product

2. Second Pass (Suffix Products):
   - For each position i, multiply the existing answer with the product of all numbers after i
   - This is done by maintaining a running suffix product
   - The final answer at each position will be the product of prefix and suffix

The key insight is that we can break down the problem into two parts:
- Product of all numbers before the current position
- Product of all numbers after the current position

## Time and Space Complexity

- **Time Complexity**: O(n)
  - We make two passes through the array
  - Each pass takes O(n) time
  - Therefore, total time is O(n)

- **Space Complexity**: O(1) if we don't count the output array
  - We only use a constant amount of extra space for prefix and suffix variables
  - The output array is required by the problem, so it's not counted in the space complexity

## Edge Cases

1. Array with zero(s)
2. Array with negative numbers
3. Single element array
4. Array with all same numbers
5. Array with two or more zeros
6. Array with alternating positive and negative numbers

## Implementation Notes

- The solution avoids using division operation as required
- The solution handles zero values correctly
- The solution works with both positive and negative numbers
- The solution is space-efficient, using only the output array for storage
- The solution maintains the order of elements in the output array

## Alternative Approaches

1. **Using Division**:
   - Calculate total product and divide by each element
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   - Not allowed by problem constraints
   - Fails when array contains zeros

2. **Using Left and Right Arrays**:
   - Create separate arrays for left and right products
   - Time Complexity: O(n)
   - Space Complexity: O(n)
   - More intuitive but uses extra space
   - Easier to understand but less efficient

3. **Using Logarithm**:
   - Convert multiplication to addition using logarithms
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   - May have precision issues with floating-point numbers
   - Not recommended for production use 