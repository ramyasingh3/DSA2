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
Explanation: "bb" is the only palindrome in the string.

Input: s = "a"
Output: "a"
Explanation: Single character is always a palindrome.
```

## Constraints
- 1 <= s.length <= 1000
- s consist only of lowercase English letters

## Approach 1: Dynamic Programming
1. Create a 2D boolean array `dp` where `dp[i][j]` represents if s[i...j] is a palindrome
2. Base cases:
   - Single characters are palindromes: dp[i][i] = true
   - Two same characters are palindromes: dp[i][i+1] = true if s[i] == s[i+1]
3. For substrings of length > 2:
   - dp[i][j] = true if s[i] == s[j] and dp[i+1][j-1] is true
4. Keep track of the longest palindrome found

## Approach 2: Center Expansion
1. For each character in the string:
   - Expand around the character for odd-length palindromes
   - Expand around the character and next character for even-length palindromes
2. Keep track of the longest palindrome found
3. Return the longest palindrome

## Approach 3: Manacher's Algorithm
1. Preprocess the string to handle even-length palindromes
2. Use an array to store the length of palindrome centered at each position
3. Use the concept of mirroring to avoid redundant calculations
4. Keep track of the center and right boundary of the current palindrome
5. Return the longest palindrome found

## Time and Space Complexity
### Approach 1 (Dynamic Programming)
- Time Complexity: O(n²)
  - We need to fill the dp table
  - Each cell takes O(1) time to compute
- Space Complexity: O(n²)
  - We need to store the dp table

### Approach 2 (Center Expansion)
- Time Complexity: O(n²)
  - We check each character as center
  - For each center, we expand up to n/2 times
- Space Complexity: O(1)
  - We only use a few variables

### Approach 3 (Manacher's Algorithm)
- Time Complexity: O(n)
  - Each character is processed at most twice
- Space Complexity: O(n)
  - We need to store the palindrome lengths

## Key Points
- This is a classic string manipulation problem
- Multiple approaches with different trade-offs
- Manacher's algorithm is the most efficient but complex
- Center expansion is simple and efficient for most cases
- Dynamic programming is intuitive but less efficient
- We need to handle both odd and even length palindromes
- Edge cases: empty string, single character, no palindrome

## Common Applications
- DNA sequence analysis
- Text processing
- Pattern matching
- Data compression
- Cryptography
- Natural language processing
- Game development

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
2. Check length 2:
   ```
   [T, F, F, F, F]
   [F, T, F, T, F]
   [F, F, T, F, F]
   [F, F, F, T, F]
   [F, F, F, F, T]
   ```
3. Check length 3:
   ```
   [T, F, T, F, F]
   [F, T, F, T, F]
   [F, F, T, F, F]
   [F, F, F, T, F]
   [F, F, F, F, T]
   ```
4. Result: "bab" or "aba"

### Center Expansion Approach:
1. Start with 'b':
   - Expand: "b" (length 1)
2. Start with 'a':
   - Expand: "aba" (length 3)
3. Start with 'b':
   - Expand: "bab" (length 3)
4. Result: "bab" or "aba"

### Manacher's Algorithm:
1. Preprocessed string: "^#b#a#b#a#d#$"
2. Calculate palindrome lengths:
   ```
   [0, 0, 1, 0, 3, 0, 3, 0, 1, 0, 1, 0, 0]
   ```
3. Result: "bab" or "aba"

## Optimization Tips
1. Use early termination if a palindrome of length n is found
2. Skip unnecessary expansions in center expansion
3. Use rolling array for space optimization in DP
4. Implement pruning in recursive solutions
5. Use bit manipulation for small character sets
6. Cache frequently accessed values
7. Use string interning for repeated substrings

## Counting Palindromic Substrings
To count all palindromic substrings:
1. Use dynamic programming to mark all palindromic substrings
2. Count the number of true values in the dp table
3. Return the total count

This can be done in O(n²) time and O(n²) space using the same dp approach. 