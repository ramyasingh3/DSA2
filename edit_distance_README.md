# Edit Distance (Levenshtein Distance)

## Problem Description
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:
1. Insert a character
2. Delete a character
3. Replace a character

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

## Approach 1: Dynamic Programming
1. Create a 2D array `dp` where `dp[i][j]` represents the minimum number of operations required to convert word1[0...i-1] to word2[0...j-1]
2. Base cases:
   - dp[i][0] = i (delete all characters from word1)
   - dp[0][j] = j (insert all characters from word2)
3. For each position (i, j):
   - If word1[i-1] == word2[j-1]:
     - dp[i][j] = dp[i-1][j-1] (no operation needed)
   - Else:
     - dp[i][j] = min(
         dp[i-1][j-1] + 1,  # replace
         dp[i-1][j] + 1,    # delete
         dp[i][j-1] + 1     # insert
       )
4. Return dp[m][n] where m and n are lengths of word1 and word2

## Approach 2: Recursion with Memoization
1. Define a recursive function that takes indices i and j
2. Base cases:
   - If i == 0: return j (insert all remaining characters)
   - If j == 0: return i (delete all remaining characters)
3. If word1[i-1] == word2[j-1]:
   - Return recursive call for (i-1, j-1)
4. Else:
   - Return min of:
     - Replace: recursive call for (i-1, j-1) + 1
     - Delete: recursive call for (i-1, j) + 1
     - Insert: recursive call for (i, j-1) + 1
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
- The solution can be extended to find the actual sequence of operations
- We need to handle edge cases (empty strings)
- The order of operations matters
- Each operation has a cost of 1

## Common Applications
- Spell checking
- DNA sequence alignment
- Plagiarism detection
- Natural language processing
- Speech recognition
- File difference detection
- Version control systems

## Example Walkthrough
For word1 = "horse" and word2 = "ros":

### Dynamic Programming Approach:
1. Initialize dp table:
   ```
   [0, 1, 2, 3]
   [1, 0, 0, 0]
   [2, 0, 0, 0]
   [3, 0, 0, 0]
   [4, 0, 0, 0]
   [5, 0, 0, 0]
   ```
2. Fill the table:
   ```
   [0, 1, 2, 3]
   [1, 1, 2, 3]
   [2, 2, 1, 2]
   [3, 2, 2, 2]
   [4, 3, 3, 2]
   [5, 4, 4, 3]
   ```
3. Result: 3

### Recursive Approach:
1. Compare 'e' with 's': no match
   - Take min of:
     - Replace: recursive call for (4, 2) + 1
     - Delete: recursive call for (4, 3) + 1
     - Insert: recursive call for (5, 2) + 1
2. Continue recursion until base cases
3. Result: 3

## Finding the Actual Operations
To find the sequence of operations:
1. Use the dp table to reconstruct the operations
2. Start from dp[m][n]
3. If characters match:
   - Move diagonally
4. Else:
   - Choose the operation that led to the minimum value
   - Move accordingly
5. Reverse the operations to get the sequence 