# Minimum Window Substring

## Problem Description
Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is unique.

## Examples

### Example 1:
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

### Example 2:
```
Input: s = "a", t = "a"
Output: "a"
```

### Example 3:
```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.
```

## Approach
The solution uses a sliding window technique with two pointers. Here's how it works:

1. Create a frequency map for characters in `t`
2. Initialize two pointers, `left` and `right`, both starting at 0
3. Move the `right` pointer to expand the window until we find all required characters
4. Once we have all required characters, move the `left` pointer to contract the window while maintaining the required characters
5. Keep track of the minimum window size and its starting position
6. Return the minimum window substring if found, otherwise return an empty string

## Time Complexity
- O(n + m), where n is the length of `s` and m is the length of `t`
- We traverse both strings once

## Space Complexity
- O(1) or O(128) for the character frequency maps
- We use constant space for the frequency maps since the number of possible characters is fixed

## Solution Code
The solution is implemented in `minimum_window_substring.py`. 