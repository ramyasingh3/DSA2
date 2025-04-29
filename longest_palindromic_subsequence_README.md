# Longest Palindromic Subsequence

## Problem Statement
Given a string `s`, find the length of the longest palindromic subsequence in `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

### Example 1:
```
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
```

### Example 2:
```
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
```

### Example 3:
```
Input: s = "racecar"
Output: 7
Explanation: The entire string is a palindrome, so the longest palindromic subsequence is "racecar".
```

## Constraints:
- 1 <= s.length <= 1000
- s consists only of lowercase English letters.

## Solution Approach
The solution uses dynamic programming to solve this problem efficiently:

1. Create a 2D DP table where dp[i][j] represents the length of the longest palindromic subsequence in the substring s[i:j+1].

2. Base cases:
   - Every single character is a palindrome of length 1 (dp[i][i] = 1)
   - For substrings of length 2, check if both characters are the same

3. For substrings of length > 2:
   - If s[i] == s[j], then dp[i][j] = dp[i+1][j-1] + 2
   - Otherwise, dp[i][j] = max(dp[i+1][j], dp[i][j-1])

4. Return dp[0][n-1] as the result

## Time and Space Complexity
- Time Complexity: O(n²), where n is the length of the input string
- Space Complexity: O(n²) for the DP table

## Implementation
The solution is implemented in Python using dynamic programming. The code includes test cases to verify the implementation. 