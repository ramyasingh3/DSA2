# Longest Substring Without Repeating Characters

## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

## Examples
```
Input: s = "abcabcbb"
Output: 3
Explanation: The longest substring without repeating characters is "abc", with length 3.

Input: s = "bbbbb"
Output: 1
Explanation: The longest substring without repeating characters is "b", with length 1.

Input: s = "pwwkew"
Output: 3
Explanation: The longest substring without repeating characters is "wke", with length 3.
```

## Constraints
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols, and spaces

## Approach
1. Use sliding window technique with two pointers
2. Keep track of the last position of each character
3. When we find a repeating character:
   - Update the start position to the position after the last occurrence
   - Continue expanding the window
4. Update maximum length when we find a longer valid substring

## Time and Space Complexity
- Time Complexity: O(n) where n is the length of the string
- Space Complexity: O(min(m, n)) where m is the size of the character set

## Solution
The solution uses a sliding window approach with the following key insights:
1. We can use a dictionary to store the last position of each character
2. When we find a repeating character, we can skip all characters before its last occurrence
3. We only need to update the maximum length when we find a longer valid substring
4. We need to handle edge cases (empty string, single character)

## Key Points
- The substring must not contain any repeating characters
- We need to handle all possible characters (letters, digits, symbols, spaces)
- The solution must be efficient (O(n) time complexity)
- We need to handle edge cases properly
- The order of characters matters

## Common Applications
- Text analysis
- DNA sequence analysis
- Pattern matching
- String processing
- Data compression

## Example Walkthrough
For s = "abcabcbb":
1. Start with empty window
2. Add 'a': window = "a", length = 1
3. Add 'b': window = "ab", length = 2
4. Add 'c': window = "abc", length = 3
5. Add 'a': window = "bca", length = 3
6. Add 'b': window = "cab", length = 3
7. Add 'c': window = "abc", length = 3
8. Add 'b': window = "cb", length = 2
9. Add 'b': window = "b", length = 1
10. Return maximum length = 3 