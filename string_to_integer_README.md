# String to Integer (atoi)

## Problem Description
Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).

The algorithm for `myAtoi(string s)` is as follows:
1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'.
3. Read in next the characters until the next non-digit character or the end of the input is reached.
4. Convert these digits into an integer.
5. If the integer is out of the 32-bit signed integer range [-2³¹, 2³¹ - 1], clamp the integer so that it remains in the range.

## Examples
1. Basic conversion:
   ```
   Input: "42"
   Output: 42
   ```

2. Negative number:
   ```
   Input: "   -42"
   Output: -42
   ```

3. With words:
   ```
   Input: "4193 with words"
   Output: 4193
   ```

4. Overflow case:
   ```
   Input: "91283472332"
   Output: 2147483647
   ```

5. Empty string:
   ```
   Input: ""
   Output: 0
   ```

## Solution Approaches

### 1. Naive Solution (O(n))
- Strip leading whitespace
- Handle sign
- Convert digits until non-digit character
- Clamp result to 32-bit range

### 2. Optimized Solution (O(n))
- Strip leading whitespace
- Handle sign
- Convert digits with overflow check
- Return clamped result

## Time Complexity
- Both solutions: O(n)

## Space Complexity
- Both solutions: O(1)

## Usage
```python
from string_to_integer import Solution

solution = Solution()
s = "42"

# Using naive solution
result = solution.my_atoi_naive(s)
print(result)  # Output: 42

# Using optimized solution (recommended)
result = solution.my_atoi_optimized(s)
print(result)  # Output: 42
```

## Common Applications
- String parsing
- Data validation
- Input processing
- File parsing
- Configuration reading 