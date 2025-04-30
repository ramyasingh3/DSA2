"""
Best Time to Buy and Sell Stock Implementation

This file contains multiple implementations to find the maximum profit from buying and selling stocks.

Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.

Time Complexity: O(n) where n is the length of the prices array
Space Complexity: O(1) for optimal solution
"""

def max_profit_brute_force(prices: list[int]) -> int:
    """
    Find maximum profit using brute force approach.
    Try all possible buy and sell combinations.
    
    Args:
        prices (list[int]): List of stock prices
        
    Returns:
        int: Maximum profit possible
    """
    max_profit = 0
    n = len(prices)
    
    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    
    return max_profit

def max_profit_optimal(prices: list[int]) -> int:
    """
    Find maximum profit using optimal approach.
    Keep track of minimum price and maximum profit.
    
    Args:
        prices (list[int]): List of stock prices
        
    Returns:
        int: Maximum profit possible
    """
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        # Update minimum price if current price is lower
        min_price = min(min_price, price)
        # Update maximum profit if current profit is higher
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

def max_profit_dp(prices: list[int]) -> int:
    """
    Find maximum profit using dynamic programming approach.
    This approach is useful when extending to more complex problems.
    
    Args:
        prices (list[int]): List of stock prices
        
    Returns:
        int: Maximum profit possible
    """
    if not prices:
        return 0
    
    n = len(prices)
    # dp[i] represents the maximum profit possible up to day i
    dp = [0] * n
    min_price = prices[0]
    
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        dp[i] = max(dp[i - 1], prices[i] - min_price)
    
    return dp[-1]

def test_max_profit():
    """Test cases for maximum profit implementations"""
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),     # Buy on day 2, sell on day 5
        ([7, 6, 4, 3, 1], 0),        # No profit possible
        ([1, 2, 3, 4, 5], 4),        # Buy on day 1, sell on day 5
        ([5, 4, 3, 2, 1], 0),        # No profit possible
        ([1], 0),                    # Single day
        ([1, 1, 1, 1], 0),          # Same price
        ([2, 4, 1], 2),             # Buy on day 1, sell on day 2
        ([3, 2, 6, 5, 0, 3], 4),    # Buy on day 2, sell on day 3
    ]
    
    for prices, expected in test_cases:
        # Test brute force approach
        assert max_profit_brute_force(prices) == expected, \
            f"Brute force test failed for {prices}"
        
        # Test optimal approach
        assert max_profit_optimal(prices) == expected, \
            f"Optimal test failed for {prices}"
        
        # Test DP approach
        assert max_profit_dp(prices) == expected, \
            f"DP test failed for {prices}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_max_profit()
    
    # Example usage
    test_prices = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [1, 2, 3, 4, 5],
        [3, 2, 6, 5, 0, 3]
    ]
    
    print("\nTesting various price arrays:")
    for prices in test_prices:
        print(f"\nPrices: {prices}")
        print(f"Using brute force: {max_profit_brute_force(prices)}")
        print(f"Using optimal: {max_profit_optimal(prices)}")
        print(f"Using DP: {max_profit_dp(prices)}") 