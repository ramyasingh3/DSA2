def coin_change_dp(coins: list[int], amount: int) -> int:
    """
    Find the minimum number of coins needed to make up the amount using dynamic programming.
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    # Initialize dp array with amount + 1 (representing infinity)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    # Fill dp array
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return -1 if amount cannot be made up
    return dp[amount] if dp[amount] <= amount else -1

def coin_change_recursive(coins: list[int], amount: int) -> int:
    """
    Find the minimum number of coins needed using recursion with memoization.
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

def get_coin_combinations(coins: list[int], amount: int) -> list[list[int]]:
    """
    Find all possible combinations of coins that sum up to the amount.
    Returns a list of coin combinations, where each combination is a list of coin values.
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount * len(coins))
    """
    dp = [[] for _ in range(amount + 1)]
    dp[0] = [[]]  # Base case: empty combination for amount 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                for prev_combination in dp[i - coin]:
                    new_combination = prev_combination + [coin]
                    # Sort to avoid duplicates
                    new_combination.sort()
                    if new_combination not in dp[i]:
                        dp[i].append(new_combination)
    
    return dp[amount]

def main():
    # Test cases
    test_cases = [
        ([1, 2, 5], 11),           # Expected: 3 (5 + 5 + 1)
        ([2], 3),                  # Expected: -1 (impossible)
        ([1], 0),                  # Expected: 0 (no coins needed)
        ([1], 1),                  # Expected: 1 (one coin)
        ([1], 2),                  # Expected: 2 (two coins)
        ([1, 2, 5], 6),           # Expected: 2 (5 + 1)
        ([1, 2, 5], 7),           # Expected: 2 (5 + 2)
        ([1, 2, 5], 8),           # Expected: 3 (5 + 2 + 1)
        ([1, 2, 5], 9),           # Expected: 3 (5 + 2 + 2)
        ([1, 2, 5], 10),          # Expected: 2 (5 + 5)
        ([186, 419, 83, 408], 6249),  # Expected: 20
    ]
    
    print("Testing Dynamic Programming solution:")
    for coins, amount in test_cases:
        min_coins = coin_change_dp(coins, amount)
        combinations = get_coin_combinations(coins, amount)
        print(f"Coins: {coins}")
        print(f"Amount: {amount}")
        print(f"Minimum coins needed: {min_coins}")
        if min_coins != -1:
            print("Possible combinations:")
            for combo in combinations:
                print(f"  {combo}")
        print()
    
    print("\nTesting Recursive solution:")
    for coins, amount in test_cases:
        min_coins = coin_change_recursive(coins, amount)
        print(f"Coins: {coins}")
        print(f"Amount: {amount}")
        print(f"Minimum coins needed: {min_coins}")
        print()

if __name__ == "__main__":
    main() 