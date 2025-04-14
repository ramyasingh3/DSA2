# Longest Substring Without Repeating Characters

## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

## Examples

### Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Approach
The solution uses a sliding window technique with a hash set to track characters in the current window. Here's how it works:

1. Initialize a set to store unique characters in the current window
2. Use two pointers, `left` and `right`, to represent the current window
3. Move the `right` pointer to expand the window:
   - If the current character is not in the set, add it and update the maximum length
   - If the current character is in the set, move the `left` pointer to remove characters until the current character is no longer in the set
4. Keep track of the maximum length found during the process

## Time Complexity
- O(n), where n is the length of the input string
- Each character is visited at most twice (once by the right pointer and once by the left pointer)

## Space Complexity
- O(min(m, n)), where m is the size of the character set
- The size of the set is bounded by the size of the character set and the length of the string

## Solution Code
The solution is implemented in `longest_substring_without_repeating_characters.py`. 