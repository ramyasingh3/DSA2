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
1. Create a boolean array `dp` where `dp[i]` represents if s[0...i-1] can be segmented
2. Base case: dp[0] = true (empty string is always valid)
3. For each position i:
   - For each word in wordDict:
     - If the word matches s[i-word_len:i] and dp[i-word_len] is true:
       - Set dp[i] = true
       - Break the inner loop
4. Return dp[n] where n is the length of s

## Approach 2: Recursion with Memoization
1. Define a recursive function that takes a starting index
2. Base cases:
   - If start == len(s): return true (reached end of string)
   - If start is memoized: return memoized value
3. For each word in wordDict:
   - If the word matches s[start:start+word_len]:
     - Recursively check if the rest of the string can be segmented
     - If true, memoize and return true
4. Memoize and return false

## Time and Space Complexity
### Approach 1 (Dynamic Programming)
- Time Complexity: O(n * m * k)
  - n is the length of string s
  - m is the number of words in wordDict
  - k is the maximum word length
- Space Complexity: O(n)
  - We need to store the dp array

### Approach 2 (Recursion with Memoization)
- Time Complexity: O(n * m * k)
  - Each position is computed only once
  - For each position, we check all words
- Space Complexity: O(n)
  - Space for memoization
  - O(n) for recursion stack

## Key Points
- This is a classic dynamic programming problem
- The DP approach is more efficient than naive recursion
- The solution can be extended to find all valid segmentations
- We need to handle edge cases (empty string, single character)
- Words can be reused multiple times
- The order of words matters

## Common Applications
- Text segmentation
- Natural language processing
- Spell checking
- Machine translation
- Document analysis
- Search engines
- Compiler design

## Example Walkthrough
For s = "leetcode" and wordDict = ["leet", "code"]:

### Dynamic Programming Approach:
1. Initialize dp array:
   ```
   [True, False, False, False, False, False, False, False]
   ```
2. Fill the dp array:
   ```
   [True, False, False, False, True, False, False, False, True]
   ```
3. Result: True

### Recursive Approach:
1. Start with index 0
2. Check "leet":
   - Matches s[0:4]
   - Recursively check s[4:]
3. Check "code":
   - Matches s[4:8]
   - Reached end of string
4. Result: True

## Finding All Valid Segmentations
To find all valid word break combinations:
1. Use a 2D array to store all valid combinations at each position
2. For each position i:
   - For each word in wordDict:
     - If the word matches and previous position has valid combinations:
       - Add new combinations by appending the word
3. Return all combinations at the last position 