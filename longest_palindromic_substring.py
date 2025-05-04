def longest_palindrome_dp(s: str) -> str:
    """
    Find the longest palindromic substring using dynamic programming.
    Time Complexity: O(n²)
    Space Complexity: O(n²)
    """
    n = len(s)
    if n < 2:
        return s
    
    # dp[i][j] represents if s[i...j] is a palindrome
    dp = [[False] * n for _ in range(n)]
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
    
    start = 0  # Start index of longest palindrome
    max_len = 1  # Length of longest palindrome
    
    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    
    # Check for substrings of length > 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1  # End index of substring
            
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length
    
    return s[start:start + max_len]

def longest_palindrome_expand(s: str) -> str:
    """
    Find the longest palindromic substring using center expansion.
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(s)
    if n < 2:
        return s
    
    def expand_around_center(left: int, right: int) -> tuple[int, int]:
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
    
    start = 0
    max_len = 1
    
    for i in range(n):
        # Check for odd length palindromes
        left, right = expand_around_center(i, i)
        if right - left + 1 > max_len:
            start = left
            max_len = right - left + 1
        
        # Check for even length palindromes
        left, right = expand_around_center(i, i + 1)
        if right - left + 1 > max_len:
            start = left
            max_len = right - left + 1
    
    return s[start:start + max_len]

def longest_palindrome_manacher(s: str) -> str:
    """
    Find the longest palindromic substring using Manacher's algorithm.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Preprocess string to handle even length palindromes
    t = '#'.join('^{}$'.format(s))
    n = len(t)
    p = [0] * n  # p[i] is the length of the palindrome centered at i
    center = right = 0
    
    for i in range(1, n - 1):
        # Mirror index
        mirror = 2 * center - i
        
        # If i is within the right boundary
        if i < right:
            p[i] = min(right - i, p[mirror])
        
        # Expand palindrome centered at i
        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1
        
        # Update center and right boundary if needed
        if i + p[i] > right:
            center = i
            right = i + p[i]
    
    # Find the maximum palindrome
    max_len = max(p)
    center_index = p.index(max_len)
    start = (center_index - max_len) // 2
    
    return s[start:start + max_len]

def count_palindromic_substrings(s: str) -> int:
    """
    Count all palindromic substrings in the given string.
    Time Complexity: O(n²)
    Space Complexity: O(n²)
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
        count += 1
    
    # Check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            count += 1
    
    # Check for substrings of length > 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                count += 1
    
    return count

def main():
    # Test cases
    test_cases = [
        "babad",           # Expected: "bab" or "aba"
        "cbbd",           # Expected: "bb"
        "a",              # Expected: "a"
        "ac",             # Expected: "a"
        "racecar",        # Expected: "racecar"
        "abba",           # Expected: "abba"
        "abcba",          # Expected: "abcba"
        "aaaa",           # Expected: "aaaa"
        "aacabdkacaa",    # Expected: "aca"
        "babadada",       # Expected: "adada"
        "",               # Expected: ""
        "a" * 1000,       # Expected: "a" * 1000
    ]
    
    print("Testing Dynamic Programming solution:")
    for s in test_cases:
        result = longest_palindrome_dp(s)
        print(f"String: '{s}'")
        print(f"Longest palindromic substring: '{result}'")
        print(f"Length: {len(result)}")
        print()
    
    print("\nTesting Center Expansion solution:")
    for s in test_cases:
        result = longest_palindrome_expand(s)
        print(f"String: '{s}'")
        print(f"Longest palindromic substring: '{result}'")
        print(f"Length: {len(result)}")
        print()
    
    print("\nTesting Manacher's algorithm:")
    for s in test_cases:
        result = longest_palindrome_manacher(s)
        print(f"String: '{s}'")
        print(f"Longest palindromic substring: '{result}'")
        print(f"Length: {len(result)}")
        print()
    
    print("\nTesting Palindromic Substring Count:")
    for s in test_cases:
        count = count_palindromic_substrings(s)
        print(f"String: '{s}'")
        print(f"Number of palindromic substrings: {count}")
        print()

if __name__ == "__main__":
    main() 