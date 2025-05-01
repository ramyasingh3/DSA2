# Longest Common Subsequence (LCS)

## Problem Description
Given two strings `text1` and `text2`, return the length of their longest common subsequence. A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.

## Examples
```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" with length 3.

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" with length 3.

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no common subsequence.
```

## Solution Approach
The solution uses dynamic programming with a 2D table. Here's how it works:

1. Create a DP table of size (m+1) × (n+1), where m and n are the lengths of text1 and text2
2. Initialize all cells with 0
3. For each character pair:
   - If characters match: dp[i][j] = dp[i-1][j-1] + 1
   - If characters don't match: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
4. The bottom-right cell contains the length of LCS

## Time and Space Complexity
- Time Complexity: O(m × n), where m and n are the lengths of the input strings
  - We fill the entire DP table once
- Space Complexity: O(m × n)
  - We need to store the entire DP table

## Implementation Details
The solution is implemented in `longest_common_subsequence.py` with:
- Two main functions:
  1. `longest_common_subsequence`: Returns the length of LCS
  2. `get_lcs_string`: Returns the actual LCS string
- Type hints for better code clarity
- Comprehensive test cases covering:
  - Basic cases
  - Edge cases (empty strings, single characters)
  - Special cases (same strings, no common subsequence)
- Clear documentation and comments

## Alternative Approaches
1. Recursive Solution (O(2^n) time):
   - Simple but inefficient
   - Good for understanding the problem
   - Can be optimized with memoization

2. Space-Optimized DP (O(n) space):
   - Uses only two rows of the DP table
   - Same time complexity but better space efficiency

## Common Applications
- DNA sequence alignment
- File difference detection
- Plagiarism detection
- Spell checking
- Natural language processing
- Version control systems
- Bioinformatics
- Machine translation 