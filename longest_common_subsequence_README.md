# Longest Common Subsequence

## Problem Description
Given two strings `text1` and `text2`, return the longest common subsequence (LCS) between them. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

## Examples
```
Input: text1 = "abcde", text2 = "ace"
Output: "ace"
Explanation: The longest common subsequence is "ace".

Input: text1 = "abc", text2 = "abc"
Output: "abc"
Explanation: The longest common subsequence is "abc".

Input: text1 = "abc", text2 = "def"
Output: ""
Explanation: There is no common subsequence.
```

## Constraints
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist only of lowercase English letters

## Approach
1. Use dynamic programming to solve the problem
2. Create a 2D dp array where:
   - dp[i][j] represents the length of LCS of text1[0...i-1] and text2[0...j-1]
3. Fill the dp table using the following rules:
   - If characters match: dp[i][j] = dp[i-1][j-1] + 1
   - If characters don't match: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
4. Reconstruct the LCS by backtracking through the dp table

## Time and Space Complexity
- Time Complexity: O(m*n) where m and n are the lengths of the input strings
- Space Complexity: O(m*n) for the dp array

## Solution
The solution uses dynamic programming with the following key insights:
1. We can build up the solution for longer substrings using solutions for shorter substrings
2. If characters match, we can extend the previous LCS
3. If characters don't match, we take the maximum of:
   - LCS of text1[0...i-2] and text2[0...j-1]
   - LCS of text1[0...i-1] and text2[0...j-2]
4. We need to handle edge cases (empty strings)

## Key Points
- A subsequence maintains the relative order of characters
- Characters don't need to be contiguous
- The solution must be efficient (O(m*n) time complexity)
- We need to handle edge cases properly
- There might be multiple valid answers of the same length

## Common Applications
- DNA sequence alignment
- File difference detection
- Plagiarism detection
- Version control systems
- Bioinformatics

## Example Walkthrough
For text1 = "abcde", text2 = "ace":
1. Initialize dp array with zeros
2. Fill dp table:
   - For "a" in both: dp[1][1] = 1
   - For "b" and "c": dp[2][2] = 1
   - For "c" in both: dp[3][2] = 2
   - For "d" and "e": dp[4][3] = 2
   - For "e" in both: dp[5][3] = 3
3. Backtrack to reconstruct LCS:
   - Start at dp[5][3]
   - Move diagonally when characters match
   - Move up or left when characters don't match
4. Result: "ace" 