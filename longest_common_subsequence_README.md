# Longest Common Subsequence

## Problem Description
Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

## Examples
```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no common subsequence, so the result is 0.
```

## Constraints
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters

## Approach 1: Dynamic Programming
1. Create a 2D array `dp` where `dp[i][j]` represents the length of LCS of text1[0...i-1] and text2[0...j-1]
2. Base case: dp[0][j] = dp[i][0] = 0 (empty string has no common subsequence)
3. For each position (i, j):
   - If text1[i-1] == text2[j-1]:
     - dp[i][j] = dp[i-1][j-1] + 1
   - Else:
     - dp[i][j] = max(dp[i-1][j], dp[i][j-1])
4. Return dp[m][n] where m and n are lengths of text1 and text2

## Approach 2: Recursion with Memoization
1. Define a recursive function that takes indices i and j
2. Base cases:
   - If i == 0 or j == 0: return 0
   - If (i, j) is memoized: return memoized value
3. If text1[i-1] == text2[j-1]:
   - Return 1 + recursive call for (i-1, j-1)
4. Else:
   - Return max of recursive calls for (i-1, j) and (i, j-1)
5. Use memoization to avoid redundant calculations

## Time and Space Complexity
### Approach 1 (Dynamic Programming)
- Time Complexity: O(m * n)
  - We need to fill the dp table
  - Each cell takes O(1) time to compute
- Space Complexity: O(m * n)
  - We need to store the dp table

### Approach 2 (Recursion with Memoization)
- Time Complexity: O(m * n)
  - Each state is computed only once
  - We have m * n possible states
- Space Complexity: O(m * n)
  - Space for memoization
  - O(m + n) for recursion stack

## Key Points
- This is a classic dynamic programming problem
- The DP approach is more efficient than naive recursion
- The solution can be extended to find the actual subsequence
- We need to handle edge cases (empty strings)
- The order of characters matters
- Characters can be skipped in either string

## Common Applications
- DNA sequence alignment
- File difference detection
- Spell checking
- Plagiarism detection
- Version control systems
- Text comparison
- Bioinformatics

## Example Walkthrough
For text1 = "abcde" and text2 = "ace":

### Dynamic Programming Approach:
1. Initialize dp table:
   ```
   [0, 0, 0, 0]
   [0, 0, 0, 0]
   [0, 0, 0, 0]
   [0, 0, 0, 0]
   [0, 0, 0, 0]
   [0, 0, 0, 0]
   ```
2. Fill the table:
   ```
   [0, 0, 0, 0]
   [0, 1, 1, 1]
   [0, 1, 1, 1]
   [0, 1, 2, 2]
   [0, 1, 2, 2]
   [0, 1, 2, 3]
   ```
3. Result: 3

### Recursive Approach:
1. Compare 'e' with 'e': match
   - Add 1 to result
   - Move to 'd' and 'c'
2. Compare 'd' with 'c': no match
   - Take max of ('d' with 'c') and ('e' with 'c')
3. Compare 'c' with 'c': match
   - Add 1 to result
   - Move to 'b' and 'a'
4. Compare 'b' with 'a': no match
   - Take max of ('b' with 'a') and ('c' with 'a')
5. Compare 'a' with 'a': match
   - Add 1 to result
6. Result: 3

## Finding the Actual Subsequence
To find the actual longest common subsequence:
1. Use the dp table to reconstruct the subsequence
2. Start from dp[m][n]
3. If characters match:
   - Add character to result
   - Move diagonally
4. Else:
   - Move in direction of larger value
5. Reverse the result to get the subsequence 