# First Unique Character

## Problem Description
Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return -1.

## Examples
1. Basic case:
   ```
   Input: "leetcode"
   Output: 0
   Explanation: 'l' is the first non-repeating character
   ```

2. No unique character:
   ```
   Input: "aabb"
   Output: -1
   Explanation: All characters appear twice
   ```

3. All unique characters:
   ```
   Input: "abcde"
   Output: 0
   Explanation: All characters are unique, so return index of first character
   ```

## Solution Approaches

### 1. Counter Solution (O(n))
- Use Counter class to count character frequencies
- Iterate through string to find first character with count 1
- Time Complexity: O(n)
- Space Complexity: O(1) - limited by alphabet size
- Best for readability

### 2. Dictionary Solution (O(n))
- Use dictionary to track count and first index
- Find minimum index among characters with count 1
- Time Complexity: O(n)
- Space Complexity: O(1) - limited by alphabet size
- Best for memory efficiency

### 3. OrderedDict Solution (O(n))
- Use OrderedDict to maintain character order
- Track character frequencies while preserving order
- Time Complexity: O(n)
- Space Complexity: O(1) - limited by alphabet size
- Best for maintaining order

## Time Complexity
All solutions: O(n), where n is the length of the string

## Space Complexity
All solutions: O(1), as we only store at most 26 characters (English alphabet)

## Usage
```python
from first_unique_char import Solution

solution = Solution()
s = "leetcode"

# Using Counter
result = solution.first_unique_char_counter(s)
print(result)  # Output: 0

# Using Dictionary
result = solution.first_unique_char_dict(s)
print(result)  # Output: 0

# Using OrderedDict
result = solution.first_unique_char_ordered_dict(s)
print(result)  # Output: 0
```

## Common Applications
- Text processing
- Data deduplication
- Stream processing
- Error detection
- Natural language processing 