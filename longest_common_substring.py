def longest_common_substring(str1: str, str2: str) -> str:
    """
    Find the longest common substring between two strings.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
        
    Returns:
        str: Longest common substring
    """
    if not str1 or not str2:
        return ""
        
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_index = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
    
    return str1[end_index - max_length:end_index]

def main():
    # Test cases
    test_cases = [
        ("ABCDGH", "ACDGHR"),          # Expected: "CDGH"
        ("ABC", "DEF"),                # Expected: ""
        ("GeeksforGeeks", "GeeksQuiz"), # Expected: "Geeks"
        ("", "ABC"),                   # Expected: ""
        ("ABC", ""),                   # Expected: ""
        ("", ""),                      # Expected: ""
    ]
    
    for str1, str2 in test_cases:
        result = longest_common_substring(str1, str2)
        print(f"Input: str1 = '{str1}', str2 = '{str2}'")
        print(f"Output: '{result}'\n")

if __name__ == "__main__":
    main() 