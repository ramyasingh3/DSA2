def word_break(s, word_dict):
    """
    Determine if s can be segmented into a space-separated sequence of one or more dictionary words.
    Time Complexity: O(n^3) where n is the length of string s
    Space Complexity: O(n)
    """
    n = len(s)
    # dp[i] represents if s[0...i-1] can be segmented into dictionary words
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always valid
    
    # Convert word_dict to set for O(1) lookups
    word_set = set(word_dict)
    
    # Check each position in the string
    for i in range(1, n + 1):
        # Check all possible substrings ending at position i
        for j in range(i):
            # If substring s[j...i-1] is in dictionary and dp[j] is True
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[n]

def main():
    # Test cases
    test_cases = [
        ("leetcode", ["leet", "code"]),  # Expected: True
        ("applepenapple", ["apple", "pen"]),  # Expected: True
        ("catsandog", ["cats", "dog", "sand", "and", "cat"]),  # Expected: False
        ("", ["a", "b"]),  # Expected: True
        ("a", []),  # Expected: False
        ("a", ["a"]),  # Expected: True
        ("aaaaaaa", ["aaaa", "aaa"]),  # Expected: True
        ("goalspecial", ["go", "goal", "goals", "special"]),  # Expected: True
    ]
    
    for s, word_dict in test_cases:
        result = word_break(s, word_dict)
        print(f"Input: s = '{s}', wordDict = {word_dict}")
        print(f"Output: {result}")
        if result:
            print("The string can be segmented into dictionary words.")
        else:
            print("The string cannot be segmented into dictionary words.")
        print()

if __name__ == "__main__":
    main() 