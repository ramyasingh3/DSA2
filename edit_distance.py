def min_distance(word1, word2):
    """
    Find the minimum number of operations required to convert word1 to word2.
    Operations allowed: insert, delete, or replace a character.
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    m, n = len(word1), len(word2)
    
    # Create a 2D dp array where dp[i][j] represents the minimum number of operations
    # required to convert word1[0...i-1] to word2[0...j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters from word1
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters from word2
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No operation needed
            else:
                # Take minimum of three operations:
                # 1. Replace: dp[i-1][j-1] + 1
                # 2. Delete: dp[i-1][j] + 1
                # 3. Insert: dp[i][j-1] + 1
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    return dp[m][n]

def main():
    # Test cases
    test_cases = [
        ("horse", "ros"),      # Expected: 3 (horse -> rorse -> rose -> ros)
        ("intention", "execution"),  # Expected: 5
        ("", ""),              # Expected: 0
        ("", "a"),             # Expected: 1 (insert 'a')
        ("a", ""),             # Expected: 1 (delete 'a')
        ("a", "b"),            # Expected: 1 (replace 'a' with 'b')
        ("pneumonoultramicroscopicsilicovolcanoconiosis", "pneumonoultramicroscopicsilicovolcanoconiosis"),  # Expected: 0
        ("sunday", "saturday"), # Expected: 3
    ]
    
    for word1, word2 in test_cases:
        result = min_distance(word1, word2)
        print(f"Input: word1 = '{word1}', word2 = '{word2}'")
        print(f"Output: {result}")
        print(f"Minimum number of operations required: {result}\n")

if __name__ == "__main__":
    main() 