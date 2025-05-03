def coin_change(coins, amount):
    """
    Find the minimum number of coins needed to make up the given amount.
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    # Initialize dp array with amount + 1 (which is greater than any possible answer)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    # For each amount from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[amount] is still amount + 1, it means no solution exists
    return dp[amount] if dp[amount] != amount + 1 else -1

def coin_change_recursive(coins, amount):
    """
    Recursive solution with memoization for the coin change problem.
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    def helper(remaining, memo):
        # Base cases
        if remaining < 0:
            return float('inf')
        if remaining == 0:
            return 0
        if remaining in memo:
            return memo[remaining]
        
        # Try each coin
        min_coins = float('inf')
        for coin in coins:
            result = helper(remaining - coin, memo)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)
        
        memo[remaining] = min_coins
        return min_coins
    
    result = helper(amount, {})
    return result if result != float('inf') else -1

def main():
    # Test cases
    test_cases = [
        ([1, 2, 5], 11),  # Expected: 3 (5 + 5 + 1)
        ([2], 3),  # Expected: -1 (impossible)
        ([1], 0),  # Expected: 0
        ([1], 1),  # Expected: 1
        ([1], 2),  # Expected: 2
        ([186, 419, 83, 408], 6249),  # Expected: 20
        ([1, 2, 5, 10, 20, 50, 100, 200], 520),  # Expected: 4 (200 + 200 + 100 + 20)
    ]
    
    print("Testing Dynamic Programming solution:")
    for coins, amount in test_cases:
        result = coin_change(coins, amount)
        print(f"Coins: {coins}, Amount: {amount}")
        print(f"Minimum coins needed: {result}")
        print()
    
    print("\nTesting Recursive solution with memoization:")
    for coins, amount in test_cases:
        result = coin_change_recursive(coins, amount)
        print(f"Coins: {coins}, Amount: {amount}")
        print(f"Minimum coins needed: {result}")
        print()

if __name__ == "__main__":
    main() 