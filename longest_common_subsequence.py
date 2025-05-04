def longest_common_subsequence_dp(text1: str, text2: str) -> int:
    """
    Find the length of the longest common subsequence using dynamic programming.
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def longest_common_subsequence_recursive(text1: str, text2: str) -> int:
    """
    Find the length of the longest common subsequence using recursion with memoization.
    Time Complexity: O(m * n)
    Space Complexity: O(m * n) for memoization
    """
    memo = {}
    
    def lcs(i: int, j: int) -> int:
        if i == 0 or j == 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        
        if text1[i - 1] == text2[j - 1]:
            memo[(i, j)] = lcs(i - 1, j - 1) + 1
        else:
            memo[(i, j)] = max(lcs(i - 1, j), lcs(i, j - 1))
        
        return memo[(i, j)]
    
    return lcs(len(text1), len(text2))

def get_longest_common_subsequence(text1: str, text2: str) -> str:
    """
    Find the actual longest common subsequence.
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the subsequence
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))

def main():
    # Test cases
    test_cases = [
        ("abcde", "ace"),           # Expected: 3 ("ace")
        ("abc", "abc"),             # Expected: 3 ("abc")
        ("abc", "def"),             # Expected: 0 ("")
        ("", ""),                   # Expected: 0 ("")
        ("a", "a"),                 # Expected: 1 ("a")
        ("abcde", "ace"),           # Expected: 3 ("ace")
        ("abcde", "ace"),           # Expected: 3 ("ace")
        ("oxcpqrsvwf", "shmtulqrypy"),  # Expected: 2
        ("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"),  # Expected: 4
        ("ezupkr", "ubmrapg"),      # Expected: 2
    ]
    
    print("Testing Dynamic Programming solution:")
    for text1, text2 in test_cases:
        length = longest_common_subsequence_dp(text1, text2)
        subsequence = get_longest_common_subsequence(text1, text2)
        print(f"Text1: '{text1}'")
        print(f"Text2: '{text2}'")
        print(f"Length of LCS: {length}")
        print(f"LCS: '{subsequence}'")
        print()
    
    print("\nTesting Recursive solution:")
    for text1, text2 in test_cases:
        length = longest_common_subsequence_recursive(text1, text2)
        print(f"Text1: '{text1}'")
        print(f"Text2: '{text2}'")
        print(f"Length of LCS: {length}")
        print()

if __name__ == "__main__":
    main() 