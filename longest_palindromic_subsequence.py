def longest_palindromic_subsequence(s: str) -> int:
    """
    Find the length of the longest palindromic subsequence in a string.
    
    Args:
        s (str): Input string
        
    Returns:
        int: Length of the longest palindromic subsequence
    """
    if not s:
        return 0
        
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Check for subsequences of length 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 2
        else:
            dp[i][i+1] = 1
    
    # Check for subsequences of length > 2
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]

def main():
    # Test cases
    test_cases = [
        "bbbab",    # Expected: 4 (subsequence: "bbbb")
        "cbbd",     # Expected: 2 (subsequence: "bb")
        "a",        # Expected: 1 (subsequence: "a")
        "",         # Expected: 0
        "racecar",  # Expected: 7 (subsequence: "racecar")
    ]
    
    for s in test_cases:
        result = longest_palindromic_subsequence(s)
        print(f"Input: s = '{s}'")
        print(f"Output: {result}\n")

if __name__ == "__main__":
    main() 