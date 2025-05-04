def word_break_dp(s: str, word_dict: list[str]) -> bool:
    """
    Check if a string can be segmented into a space-separated sequence of dictionary words using dynamic programming.
    Time Complexity: O(n * m * k) where n is string length, m is number of words, k is max word length
    Space Complexity: O(n)
    """
    n = len(s)
    dp = [False] * (n + 1)  # dp[i] represents if s[0...i-1] can be segmented
    dp[0] = True  # Empty string is always valid
    
    for i in range(1, n + 1):
        for word in word_dict:
            word_len = len(word)
            if i >= word_len and dp[i - word_len]:
                if s[i - word_len:i] == word:
                    dp[i] = True
                    break
    
    return dp[n]

def word_break_recursive(s: str, word_dict: list[str]) -> bool:
    """
    Check if a string can be segmented using recursion with memoization.
    Time Complexity: O(n * m * k) where n is string length, m is number of words, k is max word length
    Space Complexity: O(n) for memoization
    """
    memo = {}
    
    def can_break(start: int) -> bool:
        if start == len(s):
            return True
        if start in memo:
            return memo[start]
        
        for word in word_dict:
            word_len = len(word)
            if start + word_len <= len(s) and s[start:start + word_len] == word:
                if can_break(start + word_len):
                    memo[start] = True
                    return True
        
        memo[start] = False
        return False
    
    return can_break(0)

def get_word_break(s: str, word_dict: list[str]) -> list[str]:
    """
    Find all possible word break combinations.
    Returns a list of valid word break combinations.
    Time Complexity: O(n * m * k) where n is string length, m is number of words, k is max word length
    Space Complexity: O(n * m) for storing all combinations
    """
    n = len(s)
    dp = [[] for _ in range(n + 1)]  # dp[i] stores all valid combinations for s[0...i-1]
    dp[0] = [""]  # Empty string has one empty combination
    
    for i in range(1, n + 1):
        for word in word_dict:
            word_len = len(word)
            if i >= word_len and dp[i - word_len]:
                if s[i - word_len:i] == word:
                    for prev in dp[i - word_len]:
                        if prev:
                            dp[i].append(prev + " " + word)
                        else:
                            dp[i].append(word)
    
    return dp[n]

def main():
    # Test cases
    test_cases = [
        ("leetcode", ["leet", "code"]),  # Expected: True
        ("applepenapple", ["apple", "pen"]),  # Expected: True
        ("catsandog", ["cats", "dog", "sand", "and", "cat"]),  # Expected: False
        ("", ["a", "b", "c"]),  # Expected: True
        ("a", ["a"]),  # Expected: True
        ("a", ["b"]),  # Expected: False
        ("aaaaaaaa", ["aa", "aaa", "aaaa"]),  # Expected: True
        ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
         ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]),  # Expected: False
        ("catsanddog", ["cat", "cats", "and", "sand", "dog"]),  # Expected: True
        ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]),  # Expected: True
    ]
    
    print("Testing Dynamic Programming solution:")
    for s, word_dict in test_cases:
        result = word_break_dp(s, word_dict)
        print(f"String: '{s}'")
        print(f"Dictionary: {word_dict}")
        print(f"Can be segmented: {result}")
        if result:
            combinations = get_word_break(s, word_dict)
            print("Valid combinations:")
            for combo in combinations:
                print(f"  {combo}")
        print()
    
    print("\nTesting Recursive solution:")
    for s, word_dict in test_cases:
        result = word_break_recursive(s, word_dict)
        print(f"String: '{s}'")
        print(f"Dictionary: {word_dict}")
        print(f"Can be segmented: {result}")
        print()

if __name__ == "__main__":
    main() 