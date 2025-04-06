# Valid Parentheses

## Problem Description
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Examples
1. Valid parentheses:
   ```
   Input: "()"
   Output: True
   ```

2. Valid nested parentheses:
   ```
   Input: "({[]})"
   Output: True
   ```

3. Invalid parentheses:
   ```
   Input: "(]"
   Output: False
   ```

4. Empty string:
   ```
   Input: ""
   Output: True
   ```

5. Unmatched parentheses:
   ```
   Input: "([)]"
   Output: False
   ```

## Solution Approaches

### 1. Stack-based Solution (O(n))
- Use a stack to keep track of opening brackets
- For each closing bracket, check if it matches the top of the stack
- If stack is empty at the end, the string is valid

### 2. String Replacement Solution (O(n²))
- Repeatedly remove valid pairs of parentheses
- If the string becomes empty, it's valid
- If no more pairs can be removed and string is not empty, it's invalid

## Time Complexity
- Stack Solution: O(n)
- Replace Solution: O(n²)

## Space Complexity
- Stack Solution: O(n)
- Replace Solution: O(1)

## Usage
```python
from valid_parentheses import Solution

solution = Solution()
s = "({[]})"

# Using stack solution (recommended)
result = solution.is_valid_stack(s)
print(result)  # Output: True

# Using replace solution
result = solution.is_valid_replace(s)
print(result)  # Output: True
```

## Common Applications
- Syntax checking in compilers
- HTML/XML validation
- Expression evaluation
- Code editors
- Configuration file validation 