# Word Break

## Problem Description
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words. The same word in the dictionary may be reused multiple times in the segmentation.

## Examples
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: "applepenapple" can be segmented as "apple pen apple".

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
Explanation: "catsandog" cannot be segmented into dictionary words.
```

## Constraints
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters
- All the strings of wordDict are unique

## Approach
1. Use dynamic programming to solve the problem
2. Create a dp array where:
   - dp[i] represents if s[0...i-1] can be segmented into dictionary words
3. Base case:
   - dp[0] = true (empty string is always valid)
4. For each position i in the string:
   - Check all possible substrings ending at position i
   - If a substring is in the dictionary and the prefix can be segmented, mark dp[i] as true

## Time and Space Complexity
- Time Complexity: O(n³) where n is the length of string s
  - O(n) for each position
  - O(n) for checking each substring
  - O(n) for string comparison
- Space Complexity: O(n) for the dp array

## Solution
The solution uses dynamic programming with the following key insights:
1. We can build up the solution for longer substrings using solutions for shorter substrings
2. For each position, we check all possible substrings ending at that position
3. We use a set for O(1) dictionary lookups
4. We need to handle edge cases (empty string, empty dictionary)

## Key Points
- The same word can be used multiple times
- We need to check all possible segmentations
- The solution must be efficient (O(n³) time complexity)
- We need to handle edge cases properly
- The order of words matters

## Common Applications
- Text segmentation
- Natural language processing
- Spell checking
- Word prediction
- Machine translation
- Text analysis

## Example Walkthrough
For s = "leetcode", wordDict = ["leet", "code"]:
1. Initialize dp array: [True, False, False, False, False, False, False, False, False]
2. Check each position:
   - i=1: "l" not in dict
   - i=2: "le" not in dict
   - i=3: "lee" not in dict
   - i=4: "leet" in dict, dp[4] = True
   - i=5: "leetc" not in dict
   - i=6: "leetco" not in dict
   - i=7: "leetcod" not in dict
   - i=8: "code" in dict and dp[4] is True, dp[8] = True
3. Return dp[8] = True 