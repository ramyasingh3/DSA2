def longest_common_subsequence(text1, text2):
    """
    Find the length of the longest common subsequence between two strings.
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    m, n = len(text1), len(text2)
    
    # Create a 2D dp array where dp[i][j] represents the length of LCS
    # of text1[0...i-1] and text2[0...j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))

def main():
    # Test cases
    test_cases = [
        ("abcde", "ace"),      # Expected: "ace"
        ("abc", "abc"),        # Expected: "abc"
        ("abc", "def"),        # Expected: ""
        ("", ""),              # Expected: ""
        ("abc", ""),           # Expected: ""
        ("", "abc"),           # Expected: ""
        ("ABCDGH", "AEDFHR"),  # Expected: "ADH"
        ("AGGTAB", "GXTXAYB"), # Expected: "GTAB"
    ]
    
    for text1, text2 in test_cases:
        result = longest_common_subsequence(text1, text2)
        print(f"Input: text1 = '{text1}', text2 = '{text2}'")
        print(f"Output: '{result}'")
        print(f"Length of LCS: {len(result)}\n")

if __name__ == "__main__":
    main() 