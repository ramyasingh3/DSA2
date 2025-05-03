def longest_palindrome_dp(s: str) -> str:
    """
    Find the longest palindromic substring using dynamic programming.
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    """
    n = len(s)
    if n < 2:
        return s
    
    # dp[i][j] represents whether s[i:j+1] is a palindrome
    dp = [[False] * n for _ in range(n)]
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
    
    start = 0
    max_length = 1
    
    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for substrings of length > 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start + max_length]

def longest_palindrome_expand(s: str) -> str:
    """
    Find the longest palindromic substring using expand around center approach.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    if not s:
        return ""
    
    def expand_around_center(left: int, right: int) -> tuple:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
    
    start = 0
    max_length = 1
    
    for i in range(len(s)):
        # Check for odd length palindromes
        left, right = expand_around_center(i, i)
        if right - left + 1 > max_length:
            start = left
            max_length = right - left + 1
        
        # Check for even length palindromes
        left, right = expand_around_center(i, i + 1)
        if right - left + 1 > max_length:
            start = left
            max_length = right - left + 1
    
    return s[start:start + max_length]

def count_palindromic_substrings(s: str) -> int:
    """
    Count the number of palindromic substrings in a string.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    def expand_around_center(left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    total = 0
    for i in range(len(s)):
        # Count odd length palindromes
        total += expand_around_center(i, i)
        # Count even length palindromes
        total += expand_around_center(i, i + 1)
    
    return total

def main():
    # Test cases
    test_cases = [
        "babad",  # Expected: "bab" or "aba"
        "cbbd",   # Expected: "bb"
        "a",      # Expected: "a"
        "ac",     # Expected: "a"
        "racecar", # Expected: "racecar"
        "abba",   # Expected: "abba"
        "abcde",  # Expected: "a"
        "",       # Expected: ""
    ]
    
    print("Testing Dynamic Programming solution:")
    for s in test_cases:
        result = longest_palindrome_dp(s)
        print(f"Input: {s}")
        print(f"Longest palindromic substring: {result}")
        print()
    
    print("\nTesting Expand Around Center solution:")
    for s in test_cases:
        result = longest_palindrome_expand(s)
        print(f"Input: {s}")
        print(f"Longest palindromic substring: {result}")
        print()
    
    print("\nTesting Count Palindromic Substrings:")
    for s in test_cases:
        count = count_palindromic_substrings(s)
        print(f"Input: {s}")
        print(f"Number of palindromic substrings: {count}")
        print()

if __name__ == "__main__":
    main() 