# Search a 2D Matrix

## Problem Statement
Write an efficient algorithm that searches for a value `target` in an `m x n` matrix. This matrix has the following properties:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

### Example 1:
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

### Example 2:
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

### Example 3:
```
Input: matrix = [[1]], target = 1
Output: true
```

## Approach
The solution uses a modified binary search:
1. Treat the 2D matrix as a 1D array
2. Calculate the total number of elements (m * n)
3. Perform binary search on the virtual 1D array:
   - Convert 1D index to 2D coordinates:
     - row = index // n
     - col = index % n
   - Compare the target with the element at the calculated position
   - Adjust the search space based on the comparison

## Time Complexity
- O(log(m*n)), where m is the number of rows and n is the number of columns
- We perform binary search once on the virtual 1D array
- The conversion between 1D and 2D indices is O(1)

## Space Complexity
- O(1)
- We only use constant extra space for the pointers and variables
- The search is done in-place 