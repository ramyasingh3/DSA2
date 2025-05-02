# Longest Palindromic Substring

## Problem Description
Given a string `s`, return the longest palindromic substring in `s`. A palindrome is a string that reads the same backward as forward.

## Examples
```
Input: s = "babad"
Output: "bab" or "aba"
Explanation: Both "bab" and "aba" are valid answers.

Input: s = "cbbd"
Output: "bb"
Explanation: The longest palindromic substring is "bb".

Input: s = "a"
Output: "a"
Explanation: The string itself is a palindrome.
```

## Constraints
- 1 <= s.length <= 1000
- s consists only of lowercase English letters

## Approach
1. Use dynamic programming to solve the problem
2. Create a 2D boolean array dp[i][j] where:
   - dp[i][j] is true if s[i:j+1] is a palindrome
   - dp[i][j] is false otherwise
3. Base cases:
   - Every single character is a palindrome (dp[i][i] = true)
   - Two same characters form a palindrome (dp[i][i+1] = true if s[i] == s[i+1])
4. For substrings of length > 2:
   - If first and last characters match and substring between them is palindrome
   - Then the whole substring is a palindrome

## Time and Space Complexity
- Time Complexity: O(n²) where n is the length of the string
- Space Complexity: O(n²) for the dp array

## Solution
The solution uses dynamic programming with the following key insights:
1. We can build up the solution for longer substrings using solutions for shorter substrings
2. A substring is a palindrome if:
   - First and last characters match
   - Substring between them is a palindrome
3. We need to handle base cases properly
4. We need to keep track of the longest palindrome found

## Key Points
- A palindrome reads the same forward and backward
- We need to handle both odd and even length palindromes
- The solution must be efficient (O(n²) time complexity)
- We need to handle edge cases (empty string, single character)
- There might be multiple valid answers of the same length

## Common Applications
- DNA sequence analysis
- Text processing
- Pattern matching
- String manipulation
- Bioinformatics

## Example Walkthrough
For s = "babad":
1. Initialize dp array with all False
2. Set dp[i][i] = True for all i (single characters)
3. Check for length 2:
   - "ba": False
   - "ab": False
   - "ba": False
   - "ad": False
4. Check for length 3:
   - "bab": True (first and last match, middle is palindrome)
   - "aba": True (first and last match, middle is palindrome)
   - "bad": False
5. Check for length 4:
   - "baba": False
   - "abad": False
6. Check for length 5:
   - "babad": False
7. Return "bab" or "aba" (both are valid answers) 