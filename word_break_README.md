# Word Break

## Problem Description
Given a string `s` and a dictionary of strings `wordDict`, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Examples
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: "applepenapple" can be segmented as "apple pen apple".

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and"]
Output: false
Explanation: "catsandog" cannot be segmented into dictionary words.
```

## Constraints
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters
- All the strings of wordDict are unique

## Approach 1: Dynamic Programming
1. Create a boolean array `dp` where `dp[i]` represents whether the substring s[0...i-1] can be segmented
2. Initialize dp[0] = true (empty string is always valid)
3. For each position i in the string:
   - Check each word in the dictionary
   - If the word matches the substring ending at i:
     - Update dp[i] = dp[i] or dp[i - word.length]
4. Return dp[n] where n is the length of the string

## Approach 2: Recursion with Memoization
1. Define a recursive function that takes a starting position
2. Base cases:
   - If start == len(s): return true
   - If start is already memoized: return memoized value
3. For each word in the dictionary:
   - If the word matches the substring starting at current position:
     - Recursively check if the rest of the string can be segmented
4. Use memoization to avoid redundant calculations

## Time and Space Complexity
### Approach 1 (Dynamic Programming)
- Time Complexity: O(n * m * k)
  - n: length of string
  - m: number of words in dictionary
  - k: maximum word length
- Space Complexity: O(n)
  - Space for dp array

### Approach 2 (Recursion with Memoization)
- Time Complexity: O(n * m * k)
  - Each position is computed only once
  - For each position, we try all words
- Space Complexity: O(n)
  - Space for memoization
  - O(n) for recursion stack

## Key Points
- This is a classic dynamic programming problem
- The DP approach is more efficient than naive recursion
- The solution can be extended to find all possible word breaks
- We need to handle edge cases (empty string, single character)
- The order of words in the dictionary doesn't matter
- Words can be reused multiple times

## Common Applications
- Text segmentation
- Natural language processing
- Spell checking
- Autocomplete systems
- Search engines
- Document processing
- Machine translation

## Example Walkthrough
For s = "leetcode" and wordDict = ["leet", "code"]:

### Dynamic Programming Approach:
1. Initialize dp array:
   ```
   [true, false, false, false, false, false, false, false]
   ```
2. Fill the array:
   ```
   [true, false, false, false, true, false, false, true]
   ```
3. Result: true

### Recursive Approach:
1. Try "leet":
   - Remaining: "code"
   - Try "code": remaining ""
   - Result: true
2. Try other combinations:
   - No other valid combinations
3. Result: true

## Finding All Word Breaks
To find all possible word break combinations:
1. Use dynamic programming with an additional array to store valid break points
2. For each position:
   - Store all previous positions that lead to valid breaks
3. Reconstruct all possible combinations by following the stored break points
4. Return the list of all possible word break combinations 