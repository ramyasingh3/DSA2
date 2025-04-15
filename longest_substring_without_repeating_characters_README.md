# Longest Substring Without Repeating Characters

## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

### Examples
1. Input: s = "abcabcbb"
   Output: 3
   Explanation: The answer is "abc", with the length of 3.

2. Input: s = "bbbbb"
   Output: 1
   Explanation: The answer is "b", with the length of 1.

3. Input: s = "pwwkew"
   Output: 3
   Explanation: The answer is "wke", with the length of 3.

## Approach
The solution uses a sliding window technique with a hash set:
1. Use two pointers to represent the window boundaries (left and right).
2. Use a hash set to keep track of unique characters in the current window.
3. Move the right pointer to expand the window until we encounter a duplicate character.
4. When a duplicate is found, move the left pointer to remove the duplicate character.
5. Keep track of the maximum window size during the process.

## Time Complexity
- O(n) where n is the length of the string
- Each character is visited at most twice (once by each pointer)
- Hash set operations are O(1) on average

## Space Complexity
- O(min(m, n)) where m is the size of the character set
- In the worst case, we need to store all unique characters
- For ASCII strings, this is O(1) since there are only 128 possible characters

## Solution Code
The solution is implemented in `longest_substring_without_repeating_characters.py`. 