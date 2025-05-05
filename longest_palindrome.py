"""
Longest Palindromic Substring Implementation

This file contains multiple implementations to find the longest palindromic substring in a given string.

Problem Statement:
Given a string s, return the longest palindromic substring in s.
A palindrome is a string that reads the same backward as forward.

Time Complexity: O(n²) for optimal solution
Space Complexity: O(1) for optimal solution
"""

def longest_palindrome_expand(s: str) -> str:
    """
    Find longest palindrome using expand around center approach.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    if not s:
        return ""
    
    start = 0
    max_length = 1
    
    def expand_around_center(left: int, right: int) -> tuple:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
    
    for i in range(len(s)):
        # Check for odd length palindromes
        left, right = expand_around_center(i, i)
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start = left
        
        # Check for even length palindromes
        left, right = expand_around_center(i, i + 1)
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start = left
    
    return s[start:start + max_length]

def longest_palindrome_dp(s: str) -> str:
    """
    Find longest palindrome using dynamic programming.
    Time Complexity: O(n²)
    Space Complexity: O(n²)
    """
    if not s:
        return ""
    
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_length = 1
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for lengths greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start + max_length]

def longest_palindrome_manacher(s: str) -> str:
    """
    Find longest palindrome using Manacher's algorithm.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not s:
        return ""
    
    # Preprocess string to handle even length palindromes
    t = '#'.join('^{}$'.format(s))
    n = len(t)
    p = [0] * n
    center = right = 0
    
    for i in range(1, n - 1):
        if i < right:
            p[i] = min(right - i, p[2 * center - i])
        
        # Expand palindrome centered at i
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1
        
        # Update center and right if palindrome expands beyond right
        if i + p[i] > right:
            center, right = i, i + p[i]
    
    # Find the maximum element in p
    max_len, center_index = max((n, i) for i, n in enumerate(p))
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

def test_longest_palindrome():
    """Test cases for longest palindromic substring implementations"""
    test_cases = [
        ("babad", "bab"),       # Multiple palindromes
        ("cbbd", "bb"),         # Even length palindrome
        ("a", "a"),             # Single character
        ("", ""),               # Empty string
        ("racecar", "racecar"), # Full string palindrome
        ("abcde", "a"),         # No palindrome longer than 1
        ("aaa", "aaa"),         # Same characters
        ("abba", "abba"),       # Even length full palindrome
        ("abcba", "abcba"),     # Odd length full palindrome
        ("aacabdkacaa", "aca"), # Complex case
    ]
    
    for s, expected in test_cases:
        # Test expand around center approach
        result = longest_palindrome_expand(s)
        assert result == expected, f"Expand test failed for '{s}'"
        
        # Test dynamic programming approach
        result = longest_palindrome_dp(s)
        assert result == expected, f"DP test failed for '{s}'"
        
        # Test Manacher's algorithm
        result = longest_palindrome_manacher(s)
        assert result == expected, f"Manacher test failed for '{s}'"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_longest_palindrome()
    
    # Example usage
    test_strings = [
        "babad",
        "cbbd",
        "a",
        "",
        "racecar",
        "abcde",
        "aaa",
        "abba",
        "abcba",
        "aacabdkacaa"
    ]
    
    print("\nTesting various strings:")
    for s in test_strings:
        print(f"\nString: '{s}'")
        print(f"Using expand around center: {longest_palindrome_expand(s)}")
        print(f"Using dynamic programming: {longest_palindrome_dp(s)}")
        print(f"Using Manacher's algorithm: {longest_palindrome_manacher(s)}") 