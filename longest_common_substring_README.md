# Longest Common Substring

## Problem Statement
Given two strings `str1` and `str2`, find the longest common substring between them. A substring is a contiguous sequence of characters within a string.

### Example 1:
```
Input: str1 = "ABCDGH", str2 = "ACDGHR"
Output: "CDGH"
Explanation: The longest common substring is "CDGH".
```

### Example 2:
```
Input: str1 = "ABC", str2 = "DEF"
Output: ""
Explanation: There is no common substring between the two strings.
```

### Example 3:
```
Input: str1 = "GeeksforGeeks", str2 = "GeeksQuiz"
Output: "Geeks"
Explanation: The longest common substring is "Geeks".
```

## Constraints:
- 1 <= str1.length, str2.length <= 1000
- str1 and str2 consist of only uppercase and lowercase English letters.

## Solution Approach
The solution uses dynamic programming to solve this problem efficiently:

1. Create a 2D DP table where dp[i][j] represents the length of the longest common substring ending at str1[i-1] and str2[j-1].

2. For each character pair:
   - If str1[i-1] == str2[j-1], then dp[i][j] = dp[i-1][j-1] + 1
   - Keep track of the maximum length and its ending index

3. Return the substring using the maximum length and ending index

## Time and Space Complexity
- Time Complexity: O(m*n), where m and n are the lengths of the input strings
- Space Complexity: O(m*n) for the DP table

## Implementation
The solution is implemented in Python using dynamic programming. The code includes test cases to verify the implementation. 