# Coin Change

## Problem Description
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the minimum number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

## Examples
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
Explanation: It's impossible to make up amount 3 with only coin of denomination 2.

Input: coins = [1], amount = 0
Output: 0
Explanation: No coins needed for amount 0.
```

## Constraints
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

## Approach 1: Dynamic Programming
1. Create a dp array where dp[i] represents the minimum number of coins needed for amount i
2. Initialize dp[0] = 0 (base case: 0 coins needed for amount 0)
3. For each amount from 1 to target:
   - For each coin denomination:
     - If the coin can be used (amount >= coin):
       - Update dp[amount] = min(dp[amount], dp[amount - coin] + 1)
4. Return dp[amount] if it's possible, -1 otherwise

## Approach 2: Recursion with Memoization
1. Define a recursive function that takes remaining amount
2. Base cases:
   - If remaining = 0: return 0
   - If remaining < 0: return infinity
   - If remaining is memoized: return memoized value
3. For each coin:
   - Recursively calculate minimum coins needed for (remaining - coin)
   - Update minimum if a better solution is found
4. Memoize and return the minimum

## Time and Space Complexity
### Approach 1 (Dynamic Programming)
- Time Complexity: O(amount * len(coins))
  - We process each amount once
  - For each amount, we check all coins
- Space Complexity: O(amount)
  - We need to store the dp array

### Approach 2 (Recursion with Memoization)
- Time Complexity: O(amount * len(coins))
  - Each amount is computed only once
  - For each amount, we check all coins
- Space Complexity: O(amount)
  - Space for memoization
  - O(amount) for recursion stack

## Key Points
- This is a classic dynamic programming problem
- The DP approach is more efficient than naive recursion
- We need to handle edge cases (amount = 0, impossible amounts)
- Coins can be reused multiple times
- The order of coins doesn't matter
- We can extend the solution to find all possible combinations

## Common Applications
- Vending machines
- Cash register systems
- Financial calculations
- Currency conversion
- Budget planning
- Investment strategies
- Game theory

## Example Walkthrough
For coins = [1, 2, 5] and amount = 11:

### Dynamic Programming Approach:
1. Initialize dp array:
   ```
   [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
   ```
2. Fill dp array:
   ```
   [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
   ```
3. Result: 3 (5 + 5 + 1)

### Recursive Approach:
1. Start with amount = 11
2. Try coin = 5:
   - Recursively solve for amount = 6
   - Minimum coins = 2
3. Try coin = 2:
   - Recursively solve for amount = 9
   - Minimum coins = 3
4. Try coin = 1:
   - Recursively solve for amount = 10
   - Minimum coins = 2
5. Result: 3 (minimum of all possibilities)

## Finding All Combinations
To find all possible coin combinations:
1. Use a 2D array to store all valid combinations at each amount
2. For each amount i:
   - For each coin:
     - If the coin can be used:
       - Add new combinations by appending the coin to previous combinations
3. Return all combinations at the target amount

## Optimization Tips
1. Sort coins in descending order to try larger denominations first
2. Use early termination if a solution is found
3. Skip coins larger than the remaining amount
4. Use bit manipulation for small coin sets
5. Implement pruning in recursive solution
6. Use rolling array for space optimization 