# Valid Anagram

## Problem Description
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

### Example 1:
```
Input: s = "anagram", t = "nagaram"
Output: true
```

### Example 2:
```
Input: s = "rat", t = "car"
Output: false
```

## Solution Approach

The solution uses a character counting approach:

1. First, we check if the lengths of both strings are equal. If not, they cannot be anagrams.
2. We create a fixed-size array of size 26 (for lowercase English letters) to store character counts.
3. We iterate through the first string and increment the count for each character.
4. We then iterate through the second string and decrement the count for each character.
5. If at any point the count becomes negative, it means the second string has more of that character than the first string, so they cannot be anagrams.
6. If we complete the iteration without finding any negative counts, the strings are anagrams.

## Time and Space Complexity

- **Time Complexity**: O(n), where n is the length of the strings
  - We need to iterate through both strings once
  - The length check is O(1)

- **Space Complexity**: O(1)
  - We use a fixed-size array of size 26 regardless of input size
  - This is constant space as it doesn't grow with input size

## Edge Cases

1. Empty strings (both strings empty)
2. Single character strings
3. Strings of different lengths
4. Strings with repeated characters
5. Strings with all same characters

## Implementation Notes

- The solution assumes lowercase English letters (a-z)
- For a more general solution that handles all ASCII characters or Unicode, we would need to use a hash map instead of a fixed-size array
- The solution is case-sensitive; for case-insensitive comparison, we would need to convert strings to lowercase first 