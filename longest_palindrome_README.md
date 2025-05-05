# Longest Palindromic Substring

## Problem Description
Given a string `s`, return the longest palindromic substring in `s`. A palindrome is a string that reads the same backward as forward.

## Examples
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"

Input: s = "a"
Output: "a"

Input: s = "racecar"
Output: "racecar"
```

## Constraints
- 1 <= s.length <= 1000
- s consists only of lowercase English letters

## Approach 1: Expand Around Center
1. For each character in the string, expand outward to find palindromes
2. Handle both odd and even length palindromes
3. Keep track of the longest palindrome found
4. Time Complexity: O(n²)
5. Space Complexity: O(1)

## Approach 2: Dynamic Programming
1. Create a 2D boolean array dp[i][j] to store if substring s[i:j+1] is a palindrome
2. Base cases: All single characters are palindromes
3. For length 2: Check if adjacent characters are equal
4. For length > 2: Check if first and last characters match and middle substring is palindrome
5. Time Complexity: O(n²)
6. Space Complexity: O(n²)

## Approach 3: Manacher's Algorithm
1. Preprocess string to handle even length palindromes
2. Use a center and right boundary to track the current palindrome
3. Use previously computed palindromes to avoid redundant checks
4. Time Complexity: O(n)
5. Space Complexity: O(n)

## Time and Space Complexity Comparison
| Approach              | Time Complexity | Space Complexity | Notes                    |
|----------------------|-----------------|------------------|--------------------------|
| Expand Around Center | O(n²)          | O(1)            | Simple and efficient     |
| Dynamic Programming  | O(n²)          | O(n²)           | Uses more space          |
| Manacher's Algorithm | O(n)           | O(n)            | Most efficient           |

## Key Points
- This is a classic string manipulation problem
- Multiple valid approaches exist
- Edge cases to consider:
  - Empty string
  - Single character
  - All same characters
  - Full string palindrome
- The solution is not unique if multiple palindromes have the same length

## Common Applications
- DNA sequence analysis
- Text processing
- Pattern matching
- String manipulation
- Algorithm optimization
- Interview questions
- Real-world problems

## Example Walkthrough
For s = "babad":

### Expand Around Center Approach:
1. Start at 'b':
   - Expand: "b" (length 1)
2. Start at 'a':
   - Expand: "aba" (length 3)
3. Start at 'b':
   - Expand: "b" (length 1)
4. Start at 'a':
   - Expand: "a" (length 1)
5. Start at 'd':
   - Expand: "d" (length 1)
Result: "aba" or "bab"

## Follow-up Questions
1. What if we need to find all palindromic substrings?
2. What if we need to find the number of palindromic substrings?
3. What if we need to find the shortest palindromic substring?
4. What if we need to find palindromic subsequences?
5. What if we need to find palindromes in a stream of characters?

## Optimization Tips
1. Use Manacher's algorithm for optimal time complexity
2. Consider using expand around center for space efficiency
3. Handle edge cases early
4. Use early returns when possible
5. Consider using a set for unique palindromes
6. Implement parallel processing for large strings
7. Use bit manipulation for character comparison 