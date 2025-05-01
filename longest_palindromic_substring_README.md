# Longest Palindromic Substring

## Problem Description
Given a string `s`, return the longest palindromic substring in `s`. A palindrome is a string that reads the same backward as forward, e.g., "madam" or "racecar".

## Examples
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

Input: s = "racecar"
Output: "racecar"
Explanation: The entire string is a palindrome.
```

## Solution Approach
The solution uses the "Expand Around Center" technique. Here's how it works:

1. For each character in the string, we treat it as the center of a potential palindrome
2. We expand outward in both directions to find the longest palindrome
3. We need to check both odd-length and even-length palindromes:
   - Odd-length: center is a single character (e.g., "aba")
   - Even-length: center is between two characters (e.g., "abba")

## Time and Space Complexity
- Time Complexity: O(n²), where n is the length of the input string
  - For each character, we expand outward which can take O(n) time
  - We do this for each of the n characters
- Space Complexity: O(1)
  - We only use a constant amount of extra space

## Implementation Details
The solution is implemented in `longest_palindromic_substring.py` with:
- Type hints for better code clarity
- Comprehensive test cases covering:
  - Basic palindrome cases
  - Edge cases (empty string, single character)
  - Special cases (full string palindrome, no long palindromes)
- Clear documentation and comments
- Helper function for expanding around center

## Alternative Approaches
1. Dynamic Programming (O(n²) time, O(n²) space):
   - Build a table to store palindrome information
   - More complex but can be useful for related problems

2. Manacher's Algorithm (O(n) time, O(n) space):
   - More complex but optimal solution
   - Uses preprocessing to handle even/odd length palindromes

## Common Applications
- DNA sequence analysis
- Text processing
- Pattern matching
- Natural language processing
- Data compression
- Security (palindrome-based encryption)
- Game development (word games) 