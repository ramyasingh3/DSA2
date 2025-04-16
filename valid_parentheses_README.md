# Valid Parentheses

## Problem Description
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order
3. Every close bracket has a corresponding open bracket of the same type

### Examples
```
Input: "()"
Output: true

Input: "()[]{}"
Output: true

Input: "(]"
Output: false

Input: "([)]"
Output: false

Input: "{[]}"
Output: true
```

## Approach
1. Use a stack to keep track of opening brackets
2. For each character in the string:
   - If it's an opening bracket, push it onto the stack
   - If it's a closing bracket:
     - Check if stack is empty (invalid)
     - Check if top of stack matches the closing bracket
     - Pop the matching opening bracket
3. After processing all characters, check if stack is empty

### Key Points
- Stack-based solution
- O(n) time complexity
- Handles nested brackets
- Checks for proper ordering

## Time Complexity
- O(n) where n is the length of the string
  - We process each character exactly once

## Space Complexity
- O(n) in the worst case
  - When all characters are opening brackets
  - Average case is less than n

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