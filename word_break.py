def word_break_dp(s: str, word_dict: list) -> bool:
    """
    Check if a string can be segmented into a space-separated sequence of dictionary words using dynamic programming.
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(s)
    # dp[i] represents whether s[0:i] can be segmented
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always valid
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    
    return dp[n]

def word_break_recursive(s: str, word_dict: list) -> bool:
    """
    Check if a string can be segmented into a space-separated sequence of dictionary words using recursion with memoization.
    Time Complexity: O(n^2)
    Space Complexity: O(n) for memoization
    """
    memo = {}
    
    def can_break(start: int) -> bool:
        if start == len(s):
            return True
        
        if start in memo:
            return memo[start]
        
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_dict and can_break(end):
                memo[start] = True
                return True
        
        memo[start] = False
        return False
    
    return can_break(0)

def get_word_break(s: str, word_dict: list) -> list:
    """
    Find all possible word breaks for the given string.
    Returns a list of all possible space-separated sequences of dictionary words.
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    # First, find all valid break points
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    
    if not dp[n]:
        return []
    
    # Then, find all possible word breaks
    result = []
    
    def find_breaks(start: int, current: list):
        if start == n:
            result.append(' '.join(current))
            return
        
        for end in range(start + 1, n + 1):
            word = s[start:end]
            if word in word_dict and dp[end]:
                current.append(word)
                find_breaks(end, current)
                current.pop()
    
    find_breaks(0, [])
    return result

def main():
    # Test cases
    test_cases = [
        ("leetcode", ["leet", "code"]),  # Expected: True
        ("applepenapple", ["apple", "pen"]),  # Expected: True
        ("catsandog", ["cats", "dog", "sand", "and", "cat"]),  # Expected: False
        ("", ["a", "b"]),  # Expected: True
        ("a", ["a"]),  # Expected: True
        ("aaaaaaa", ["aaaa", "aaa"]),  # Expected: True
        ("catsanddog", ["cat", "cats", "and", "sand", "dog"]),  # Expected: True
        ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]),  # Expected: True
    ]
    
    print("Testing Dynamic Programming solution:")
    for s, word_dict in test_cases:
        result = word_break_dp(s, word_dict)
        print(f"String: {s}")
        print(f"Dictionary: {word_dict}")
        print(f"Can be segmented: {result}")
        if result:
            breaks = get_word_break(s, word_dict)
            print("Possible word breaks:")
            for break_sequence in breaks:
                print(f"  {break_sequence}")
        print()
    
    print("\nTesting Recursive solution:")
    for s, word_dict in test_cases:
        result = word_break_recursive(s, word_dict)
        print(f"String: {s}")
        print(f"Dictionary: {word_dict}")
        print(f"Can be segmented: {result}")
        print()

if __name__ == "__main__":
    main() 