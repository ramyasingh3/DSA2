def word_break_dp(s: str, word_dict: list) -> bool:
    """
    Check if the string can be segmented into a space-separated sequence of dictionary words using DP.
    Time Complexity: O(n * m * k) where n is string length, m is dict size, k is max word length
    Space Complexity: O(n)
    """
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always valid
    
    for i in range(1, n + 1):
        for word in word_dict:
            word_len = len(word)
            if i >= word_len and s[i - word_len:i] == word:
                dp[i] = dp[i] or dp[i - word_len]
    
    return dp[n]

def word_break_recursive(s: str, word_dict: list) -> bool:
    """
    Check if the string can be segmented using recursion with memoization.
    Time Complexity: O(n * m * k) where n is string length, m is dict size, k is max word length
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

def get_word_break(s: str, word_dict: list) -> list:
    """
    Return all possible word break combinations if possible.
    Returns empty list if no valid break exists.
    Time Complexity: O(n * m * k) where n is string length, m is dict size, k is max word length
    Space Complexity: O(n)
    """
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    prev = [[] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for word in word_dict:
            word_len = len(word)
            if i >= word_len and s[i - word_len:i] == word and dp[i - word_len]:
                dp[i] = True
                prev[i].append(i - word_len)
    
    if not dp[n]:
        return []
    
    # Reconstruct all possible combinations
    result = []
    def reconstruct(pos: int, current: list):
        if pos == 0:
            result.append(' '.join(current[::-1]))
            return
        for prev_pos in prev[pos]:
            word = s[prev_pos:pos]
            reconstruct(prev_pos, current + [word])
    
    reconstruct(n, [])
    return result

def main():
    # Test cases
    test_cases = [
        ("leetcode", ["leet", "code"]),                    # Expected: True
        ("applepenapple", ["apple", "pen"]),              # Expected: True
        ("catsandog", ["cats", "dog", "sand", "and"]),    # Expected: False
        ("", ["a", "b"]),                                 # Expected: True
        ("a", ["a"]),                                     # Expected: True
        ("aaaaaaa", ["aaaa", "aaa"]),                     # Expected: True
        ("catsanddog", ["cat", "cats", "and", "sand", "dog"]),  # Expected: True
        ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]),  # Expected: True
        ("aaaaaaaa", ["aaaa", "aa", "a"]),                # Expected: True
        ("aaaaaaaa", ["aaaa", "aaa"]),                    # Expected: True
    ]
    
    print("Testing Dynamic Programming solution:")
    for s, word_dict in test_cases:
        result = word_break_dp(s, word_dict)
        print(f"String: '{s}'")
        print(f"Dictionary: {word_dict}")
        print(f"Can be broken: {result}")
        if result:
            combinations = get_word_break(s, word_dict)
            print(f"Possible combinations: {combinations}")
        print()
    
    print("\nTesting Recursive solution:")
    for s, word_dict in test_cases:
        result = word_break_recursive(s, word_dict)
        print(f"String: '{s}'")
        print(f"Dictionary: {word_dict}")
        print(f"Can be broken: {result}")
        print()

if __name__ == "__main__":
    main() 