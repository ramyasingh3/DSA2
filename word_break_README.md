# Word Break

## Problem Description
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Examples
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

## Constraints
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters
- All the strings of wordDict are unique

## Approach 1: Dynamic Programming
1. Create a boolean array `dp` where `dp[i]` represents whether the substring `s[0:i]` can be segmented
2. Initialize `dp[0] = true` (empty string is always valid)
3. For each position i in the string:
   - Check all possible substrings ending at i
   - If a substring is in the dictionary and the prefix can be segmented, mark dp[i] as true
4. Return dp[n] where n is the length of the string

## Approach 2: Recursion with Memoization
1. Define a recursive function that takes a starting index
2. Base case: if start == len(s), return true
3. For each possible end position:
   - If the substring is in the dictionary and the rest can be segmented, return true
4. Use memoization to avoid redundant calculations

## Time and Space Complexity
### Approach 1 (Dynamic Programming)
- Time Complexity: O(n^2)
  - We check each possible substring
  - Dictionary lookup is O(1) with a set
- Space Complexity: O(n)
  - We need to store the dp array

### Approach 2 (Recursion with Memoization)
- Time Complexity: O(n^2)
  - Each state is computed only once
  - We check each possible substring
- Space Complexity: O(n)
  - Space for memoization
  - O(n) for recursion stack

## Key Points
- This is a classic dynamic programming problem
- The DP approach is more efficient than naive recursion
- The solution can be extended to find all possible word breaks
- Dictionary words can be reused multiple times
- The order of words matters

## Common Applications
- Text segmentation
- Natural language processing
- Spell checking
- Word prediction
- Text analysis
- Machine translation
- Search engines

## Example Walkthrough
For s = "leetcode" and wordDict = ["leet", "code"]:

### Dynamic Programming Approach:
1. Initialize dp array:
   ```
   [True, False, False, False, False, False, False, False, False]
   ```
2. Fill the array:
   ```
   [True, False, False, False, True, False, False, False, True]
   ```
3. Result: True

### Recursive Approach:
1. Check "leet":
   - "leet" is in dictionary
   - Recursively check "code"
2. Check "code":
   - "code" is in dictionary
   - Reached end of string
3. Result: True

## Finding All Possible Word Breaks
To find all possible word breaks:
1. First, find all valid break points using DP
2. Then, use backtracking to find all possible combinations
3. For each valid break point:
   - Add the word to current sequence
   - Recursively find breaks for remaining string
   - Backtrack and try other possibilities
4. Return all valid sequences 