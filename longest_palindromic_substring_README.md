# Longest Palindromic Substring

## Problem Description
Given a string `s`, return the longest palindromic substring in `s`. A palindrome is a string that reads the same backward as forward.

## Examples
1. Basic case:
   ```
   Input: s = "babad"
   Output: "bab" or "aba"
   ```

2. Single character:
   ```
   Input: s = "a"
   Output: "a"
   ```

3. All same characters:
   ```
   Input: s = "aaaa"
   Output: "aaaa"
   ```

## Solution Approaches

### 1. Brute Force Solution (O(n³))
- Checks all possible substrings
- Time Complexity: O(n³)
- Space Complexity: O(1)
- Simple but inefficient
- Good for understanding the problem

### 2. Dynamic Programming Solution (O(n²))
- Uses a 2D table to store palindrome information
- Time Complexity: O(n²)
- Space Complexity: O(n²)
- More efficient than brute force
- Good for learning dynamic programming

### 3. Expand Around Center Solution (O(n²))
- Expands around each character as center
- Time Complexity: O(n²)
- Space Complexity: O(1)
- Most efficient
- Good for learning string manipulation

## Time Complexity
- Brute Force: O(n³)
- Dynamic Programming: O(n²)
- Expand Around Center: O(n²)

## Space Complexity
- Brute Force: O(1)
- Dynamic Programming: O(n²)
- Expand Around Center: O(1)

## Usage
```python
from longest_palindromic_substring import Solution

solution = Solution()
s = "babad"

# Using brute force solution
result = solution.longest_palindrome_brute(s)
print(f"Longest palindromic substring: {result}")

# Using dynamic programming solution
result = solution.longest_palindrome_dp(s)
print(f"Longest palindromic substring: {result}")

# Using expand around center solution
result = solution.longest_palindrome_expand(s)
print(f"Longest palindromic substring: {result}")
```

## Common Applications
- Text processing
- Pattern matching
- Data validation
- String manipulation
- Bioinformatics 