# Coin Change

## Problem Description
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the minimum number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

## Examples
```
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
Explanation: It's impossible to make amount 3 with only coin of denomination 2.

Input: coins = [1], amount = 0
Output: 0
Explanation: No coins needed for amount 0.
```

## Constraints
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

## Approach 1: Dynamic Programming
1. Create an array `dp` where `dp[i]` represents the minimum number of coins needed to make amount i
2. Initialize dp[0] = 0 (base case: 0 coins needed for amount 0)
3. For each amount from 1 to target:
   - Try each coin denomination
   - If the coin can be used (amount >= coin value):
     - Update dp[i] = min(dp[i], dp[i - coin] + 1)
4. Return dp[amount] if it's not infinity, else -1

## Approach 2: Recursion with Memoization
1. Define a recursive function that takes remaining amount
2. Base cases:
   - If remaining = 0: return 0
   - If remaining < 0: return infinity
3. For each coin:
   - Recursively find minimum coins for (remaining - coin)
   - Take minimum of all possibilities
4. Use memoization to avoid redundant calculations

## Time and Space Complexity
### Approach 1 (Dynamic Programming)
- Time Complexity: O(amount * len(coins))
  - We need to check each amount and each coin
- Space Complexity: O(amount)
  - We need to store the dp array

### Approach 2 (Recursion with Memoization)
- Time Complexity: O(amount * len(coins))
  - Each amount is computed only once
  - For each amount, we try all coins
- Space Complexity: O(amount)
  - Space for memoization
  - O(amount) for recursion stack

## Key Points
- This is a classic dynamic programming problem
- The DP approach is more efficient than naive recursion
- The solution can be extended to find the actual coin combination
- We need to handle edge cases (amount = 0, impossible amounts)
- The order of coins doesn't matter

## Common Applications
- Vending machines
- Cash registers
- Banking systems
- Payment processing
- Currency conversion
- Budget planning
- Resource allocation

## Example Walkthrough
For coins = [1, 2, 5] and amount = 11:

### Dynamic Programming Approach:
1. Initialize dp array:
   ```
   [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
   ```
2. Fill the array:
   ```
   [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
   ```
3. Result: 3

### Recursive Approach:
1. Try coin 5:
   - Remaining: 6
   - Try coin 5 again: remaining 1
   - Try coin 1: remaining 0
   - Total: 3 coins
2. Try other combinations:
   - 5 + 2 + 2 + 2: 4 coins
   - 2 + 2 + 2 + 2 + 2 + 1: 6 coins
3. Result: 3

## Finding the Coin Combination
To find the actual coin combination:
1. Use dynamic programming with an additional array to store the last coin used
2. For each amount:
   - Update dp[i] and store the coin that led to this minimum
3. Reconstruct the combination by following the stored coins
4. Return the list of coins used 