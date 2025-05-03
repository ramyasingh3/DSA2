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
1. Create a 2D boolean array `dp` where `dp[i][j]` represents whether `s[i:j+1]` is a palindrome
2. Initialize the diagonal elements (single characters) as true
3. Check for substrings of length 2
4. For substrings of length > 2:
   - If first and last characters match and substring between them is palindrome, mark as true
5. Keep track of the longest palindrome found

## Approach 2: Expand Around Center
1. For each character in the string:
   - Expand around it as center for odd length palindromes
   - Expand around it and next character for even length palindromes
2. Keep track of the longest palindrome found
3. Return the substring with maximum length

## Time and Space Complexity
### Approach 1 (Dynamic Programming)
- Time Complexity: O(n²)
  - We need to fill the n×n DP table
- Space Complexity: O(n²)
  - We need to store the n×n DP table

### Approach 2 (Expand Around Center)
- Time Complexity: O(n²)
  - For each center, we expand up to n/2 times
- Space Complexity: O(1)
  - We only use constant extra space

## Key Points
- This is a classic dynamic programming problem
- The expand around center approach is more space efficient
- We need to handle both odd and even length palindromes
- The solution can be extended to count all palindromic substrings
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
     b a b a d
   b 1 0 0 0 0
   a 0 1 0 0 0
   b 0 0 1 0 0
   a 0 0 0 1 0
   d 0 0 0 0 1
   ```
2. Check length 2:
   ```
     b a b a d
   b 1 0 0 0 0
   a 0 1 0 0 0
   b 0 0 1 0 0
   a 0 0 0 1 0
   d 0 0 0 0 1
   ```
3. Check length > 2:
   ```
     b a b a d
   b 1 0 1 0 0
   a 0 1 0 1 0
   b 0 0 1 0 0
   a 0 0 0 1 0
   d 0 0 0 0 1
   ```
4. Result: "bab" or "aba"

### Expand Around Center Approach:
1. Center at 'b':
   - Odd: "b"
   - Even: "ba"
2. Center at 'a':
   - Odd: "aba"
   - Even: "ab"
3. Center at 'b':
   - Odd: "bab"
   - Even: "ba"
4. Center at 'a':
   - Odd: "a"
   - Even: "ad"
5. Center at 'd':
   - Odd: "d"
   - Even: N/A
6. Result: "bab" or "aba"

## Counting Palindromic Substrings
To count all palindromic substrings:
1. Use the expand around center approach
2. For each center:
   - Count odd length palindromes
   - Count even length palindromes
3. Sum up all counts
4. Return the total number of palindromic substrings 