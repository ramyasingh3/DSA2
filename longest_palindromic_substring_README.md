# Longest Palindromic Substring

## Problem Description
Given a string `s`, return the longest palindromic substring in `s`.

A palindrome is a string that reads the same backward as forward, e.g., "madam" or "racecar".

## Examples
```
Input: s = "babad"
Output: "bab" or "aba"
Explanation: Both "bab" and "aba" are valid answers.

Input: s = "cbbd"
Output: "bb"
Explanation: "bb" is the longest palindromic substring.

Input: s = "a"
Output: "a"
Explanation: Single character is always a palindrome.
```

## Constraints
- 1 <= s.length <= 1000
- s consist only of lowercase English letters

## Approach 1: Dynamic Programming
1. Create a 2D boolean array `dp` where `dp[i][j]` represents whether s[i:j+1] is a palindrome
2. Base cases:
   - Every single character is a palindrome (dp[i][i] = true)
   - Two characters are palindrome if they are equal (dp[i][i+1] = true if s[i] == s[i+1])
3. For substrings of length > 2:
   - dp[i][j] = true if s[i] == s[j] and dp[i+1][j-1] is true
4. Keep track of the longest palindrome found

## Approach 2: Center Expansion
1. For each character in the string, expand around it to find palindromes
2. Consider both odd and even length palindromes:
   - Odd length: expand from single character
   - Even length: expand from two adjacent characters
3. Keep track of the longest palindrome found

## Time and Space Complexity
### Approach 1 (Dynamic Programming)
- Time Complexity: O(n²)
  - We need to fill the dp table
  - Each cell takes O(1) time to compute
- Space Complexity: O(n²)
  - We need to store the dp table

### Approach 2 (Center Expansion)
- Time Complexity: O(n²)
  - For each character, we expand up to n/2 times
- Space Complexity: O(1)
  - We only use a constant amount of extra space

## Key Points
- This is a classic dynamic programming problem
- The center expansion approach is more space-efficient
- We need to handle both odd and even length palindromes
- The solution can be extended to count all palindromic substrings
- We need to handle edge cases (empty string, single character)
- The order of characters matters

## Common Applications
- DNA sequence analysis
- Text processing
- Pattern matching
- String manipulation
- Natural language processing
- Data compression
- Cryptography

## Example Walkthrough
For s = "babad":

### Dynamic Programming Approach:
1. Initialize dp table:
   ```
   [T, F, F, F, F]
   [F, T, F, F, F]
   [F, F, T, F, F]
   [F, F, F, T, F]
   [F, F, F, F, T]
   ```
2. Fill the table:
   ```
   [T, F, T, F, F]
   [F, T, F, T, F]
   [F, F, T, F, T]
   [F, F, F, T, F]
   [F, F, F, F, T]
   ```
3. Result: "bab" or "aba"

### Center Expansion Approach:
1. Try center at 'b':
   - Expand: "b" (length 1)
2. Try center at 'a':
   - Expand: "aba" (length 3)
3. Try center at 'b':
   - Expand: "bab" (length 3)
4. Try center at 'a':
   - Expand: "a" (length 1)
5. Try center at 'd':
   - Expand: "d" (length 1)
6. Result: "bab" or "aba"

## Counting Palindromic Substrings
To count all palindromic substrings:
1. Use dynamic programming to mark all palindromic substrings
2. Count the number of true values in the dp table
3. Return the total count

This can be done in O(n²) time and O(n²) space using the same dp approach. 