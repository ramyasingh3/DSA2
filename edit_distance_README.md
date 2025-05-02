# Edit Distance (Levenshtein Distance)

## Problem Description
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`. You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

## Examples
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

## Constraints
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters

## Approach
1. Use dynamic programming to solve the problem
2. Create a 2D dp array where:
   - dp[i][j] represents the minimum number of operations required to convert word1[0...i-1] to word2[0...j-1]
3. Base cases:
   - dp[i][0] = i (delete all characters from word1)
   - dp[0][j] = j (insert all characters from word2)
4. For each position (i,j):
   - If characters match: dp[i][j] = dp[i-1][j-1]
   - If characters don't match: dp[i][j] = min(replace, delete, insert) + 1

## Time and Space Complexity
- Time Complexity: O(m*n) where m and n are the lengths of the input strings
- Space Complexity: O(m*n) for the dp array

## Solution
The solution uses dynamic programming with the following key insights:
1. We can build up the solution for longer substrings using solutions for shorter substrings
2. For each position, we consider three operations:
   - Replace: dp[i-1][j-1] + 1
   - Delete: dp[i-1][j] + 1
   - Insert: dp[i][j-1] + 1
3. We take the minimum of these three operations
4. We need to handle edge cases (empty strings)

## Key Points
- The order of operations matters
- We need to consider all three operations at each step
- The solution must be efficient (O(m*n) time complexity)
- We need to handle edge cases properly
- The operations are symmetric (distance from A to B equals distance from B to A)

## Common Applications
- Spell checking
- DNA sequence alignment
- Natural language processing
- Plagiarism detection
- Speech recognition
- Machine translation

## Example Walkthrough
For word1 = "horse", word2 = "ros":
1. Initialize dp array:
   - First row: [0,1,2,3]
   - First column: [0,1,2,3,4,5]
2. Fill dp table:
   - For "h" and "r": dp[1][1] = 1 (replace)
   - For "ho" and "ro": dp[2][2] = 1 (replace)
   - For "hor" and "ros": dp[3][3] = 2 (replace 'h' and 'r')
   - For "hors" and "ros": dp[4][3] = 2 (delete 'h')
   - For "horse" and "ros": dp[5][3] = 3 (delete 'h' and 'e')
3. Return dp[5][3] = 3 