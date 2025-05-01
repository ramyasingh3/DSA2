def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Given two strings text1 and text2, return the length of their longest common subsequence.
    A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
    
    Args:
        text1 (str): First input string
        text2 (str): Second input string
        
    Returns:
        int: Length of the longest common subsequence
    """
    m, n = len(text1), len(text2)
    
    # Create a 2D DP table initialized with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def get_lcs_string(text1: str, text2: str) -> str:
    """
    Get the actual longest common subsequence string.
    
    Args:
        text1 (str): First input string
        text2 (str): Second input string
        
    Returns:
        str: The longest common subsequence string
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the LCS string
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

def test_lcs():
    """Test cases for longest common subsequence implementation"""
    test_cases = [
        # Basic cases
        ("abcde", "ace", 3),           # "ace" is the LCS
        ("abc", "abc", 3),             # Same strings
        ("abc", "def", 0),             # No common subsequence
        
        # Edge cases
        ("", "", 0),                   # Empty strings
        ("a", "a", 1),                 # Single character
        ("a", "b", 0),                 # Different single characters
        
        # Special cases
        ("ABCDGH", "AEDFHR", 3),       # "ADH" is the LCS
        ("AGGTAB", "GXTXAYB", 4),      # "GTAB" is the LCS
        ("HELLO", "WORLD", 1),         # "L" is the LCS
    ]
    
    for text1, text2, expected_length in test_cases:
        result = longest_common_subsequence(text1, text2)
        assert result == expected_length, f"Test failed for '{text1}' and '{text2}'. Expected {expected_length}, got {result}"
        
        # Test the actual LCS string
        lcs_string = get_lcs_string(text1, text2)
        assert len(lcs_string) == expected_length, f"LCS string length mismatch for '{text1}' and '{text2}'"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_lcs()
    
    # Example usage
    example_pairs = [
        ("abcde", "ace"),
        ("ABCDGH", "AEDFHR"),
        ("AGGTAB", "GXTXAYB"),
        ("HELLO", "WORLD"),
    ]
    
    for text1, text2 in example_pairs:
        length = longest_common_subsequence(text1, text2)
        lcs_string = get_lcs_string(text1, text2)
        print(f"Input: text1 = '{text1}', text2 = '{text2}'")
        print(f"Output: {length}")
        print(f"Explanation: The longest common subsequence is '{lcs_string}' with length {length}\n") 