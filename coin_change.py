def coin_change_dp(coins: list, amount: int) -> int:
    """
    Find the minimum number of coins needed to make up the amount using dynamic programming.
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    # dp[i] represents the minimum number of coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_recursive(coins: list, amount: int) -> int:
    """
    Find the minimum number of coins needed to make up the amount using recursion with memoization.
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount) for memoization
    """
    memo = {}
    
    def min_coins(remaining: int) -> int:
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')
        if remaining in memo:
            return memo[remaining]
        
        min_count = float('inf')
        for coin in coins:
            count = min_coins(remaining - coin)
            if count != float('inf'):
                min_count = min(min_count, count + 1)
        
        memo[remaining] = min_count
        return min_count
    
    result = min_coins(amount)
    return result if result != float('inf') else -1

def get_coin_combination(coins: list, amount: int) -> list:
    """
    Find the combination of coins that makes up the amount with minimum number of coins.
    Returns a list of coins used, or empty list if no solution exists.
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    prev_coin = [-1] * (amount + 1)  # To store the last coin used for each amount
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev_coin[i] = coin
    
    if dp[amount] == float('inf'):
        return []
    
    # Reconstruct the combination
    combination = []
    remaining = amount
    while remaining > 0:
        coin = prev_coin[remaining]
        combination.append(coin)
        remaining -= coin
    
    return combination

def main():
    # Test cases
    test_cases = [
        ([1, 2, 5], 11),      # Expected: 3 (5 + 5 + 1)
        ([2], 3),             # Expected: -1 (impossible)
        ([1], 0),             # Expected: 0
        ([1], 1),             # Expected: 1
        ([1], 2),             # Expected: 2
        ([1, 2, 5], 6),       # Expected: 2 (5 + 1)
        ([1, 2, 5], 7),       # Expected: 2 (5 + 2)
        ([1, 2, 5], 8),       # Expected: 3 (5 + 2 + 1)
        ([1, 2, 5], 9),       # Expected: 3 (5 + 2 + 2)
        ([1, 2, 5], 10),      # Expected: 2 (5 + 5)
    ]
    
    print("Testing Dynamic Programming solution:")
    for coins, amount in test_cases:
        result = coin_change_dp(coins, amount)
        print(f"Coins: {coins}, Amount: {amount}")
        print(f"Minimum number of coins: {result}")
        if result != -1:
            combination = get_coin_combination(coins, amount)
            print(f"Coin combination: {combination}")
        print()
    
    print("\nTesting Recursive solution:")
    for coins, amount in test_cases:
        result = coin_change_recursive(coins, amount)
        print(f"Coins: {coins}, Amount: {amount}")
        print(f"Minimum number of coins: {result}")
        print()

if __name__ == "__main__":
    main() 