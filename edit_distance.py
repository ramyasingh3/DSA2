def edit_distance_dp(word1: str, word2: str) -> int:
    """
    Find the minimum number of operations required to convert word1 to word2 using dynamic programming.
    Operations: insert, delete, replace
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j - 1] + 1,  # replace
                    dp[i - 1][j] + 1,      # delete
                    dp[i][j - 1] + 1       # insert
                )
    
    return dp[m][n]

def edit_distance_recursive(word1: str, word2: str) -> int:
    """
    Find the minimum number of operations required using recursion with memoization.
    Time Complexity: O(m * n)
    Space Complexity: O(m * n) for memoization
    """
    memo = {}
    
    def min_distance(i: int, j: int) -> int:
        if i == 0:
            return j
        if j == 0:
            return i
        if (i, j) in memo:
            return memo[(i, j)]
        
        if word1[i - 1] == word2[j - 1]:
            memo[(i, j)] = min_distance(i - 1, j - 1)
        else:
            memo[(i, j)] = min(
                min_distance(i - 1, j - 1) + 1,  # replace
                min_distance(i - 1, j) + 1,      # delete
                min_distance(i, j - 1) + 1       # insert
            )
        
        return memo[(i, j)]
    
    return min_distance(len(word1), len(word2))

def get_edit_operations(word1: str, word2: str) -> list:
    """
    Find the sequence of operations required to convert word1 to word2.
    Returns a list of operations: ('replace', i, char), ('delete', i), ('insert', i, char)
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j - 1] + 1,  # replace
                    dp[i - 1][j] + 1,      # delete
                    dp[i][j - 1] + 1       # insert
                )
    
    # Reconstruct the operations
    operations = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i - 1] == word2[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            operations.append(('replace', i - 1, word2[j - 1]))
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(('delete', i - 1))
            i -= 1
        else:
            operations.append(('insert', i, word2[j - 1]))
            j -= 1
    
    return operations[::-1]

def main():
    # Test cases
    test_cases = [
        ("horse", "ros"),           # Expected: 3
        ("intention", "execution"), # Expected: 5
        ("", ""),                   # Expected: 0
        ("a", "a"),                 # Expected: 0
        ("a", "b"),                 # Expected: 1
        ("ab", "bc"),               # Expected: 2
        ("pneumonoultramicroscopicsilicovolcanoconiosis", "pneumonoultramicroscopicsilicovolcanoconiosis"),  # Expected: 0
        ("kitten", "sitting"),      # Expected: 3
        ("sunday", "saturday"),     # Expected: 3
        ("algorithm", "altruistic"), # Expected: 6
    ]
    
    print("Testing Dynamic Programming solution:")
    for word1, word2 in test_cases:
        distance = edit_distance_dp(word1, word2)
        operations = get_edit_operations(word1, word2)
        print(f"Word1: '{word1}'")
        print(f"Word2: '{word2}'")
        print(f"Edit distance: {distance}")
        print("Operations:")
        for op in operations:
            if op[0] == 'replace':
                print(f"  Replace '{word1[op[1]]}' with '{op[2]}' at position {op[1]}")
            elif op[0] == 'delete':
                print(f"  Delete '{word1[op[1]]}' at position {op[1]}")
            else:  # insert
                print(f"  Insert '{op[2]}' at position {op[1]}")
        print()
    
    print("\nTesting Recursive solution:")
    for word1, word2 in test_cases:
        distance = edit_distance_recursive(word1, word2)
        print(f"Word1: '{word1}'")
        print(f"Word2: '{word2}'")
        print(f"Edit distance: {distance}")
        print()

if __name__ == "__main__":
    main() 