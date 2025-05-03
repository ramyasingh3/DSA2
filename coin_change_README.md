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
Explanation: It's impossible to make amount 3 with only coin of denomination 2.

Input: coins = [1], amount = 0
Output: 0
Explanation: No coins needed for amount 0.
```

## Constraints
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

## Approach 1: Dynamic Programming (Bottom-up)
1. Create a dp array where dp[i] represents the minimum number of coins needed for amount i
2. Initialize dp[0] = 0 (base case)
3. Initialize all other dp values to amount + 1 (which is greater than any possible answer)
4. For each amount from 1 to target amount:
   - Try each coin denomination
   - If the coin can be used (coin <= current amount), update dp[i] = min(dp[i], dp[i - coin] + 1)
5. Return dp[amount] if it's not amount + 1, otherwise return -1

## Approach 2: Recursive with Memoization (Top-down)
1. Create a recursive function that takes remaining amount and memo dictionary
2. Base cases:
   - If remaining < 0, return infinity (invalid)
   - If remaining == 0, return 0 (valid)
   - If remaining in memo, return memoized value
3. For each coin:
   - Recursively calculate minimum coins needed for (remaining - coin)
   - Update minimum if a valid solution is found
4. Memoize and return the result

## Time and Space Complexity
### Both Approaches
- Time Complexity: O(amount * len(coins))
- Space Complexity: O(amount)

## Key Points
- This is a classic dynamic programming problem
- The order of coins doesn't matter
- We can use each coin multiple times
- We need to handle the case where no solution exists
- The recursive approach with memoization can be more intuitive but has the same complexity

## Common Applications
- Vending machines
- Cash register systems
- Financial calculations
- Currency conversion
- Payment processing
- Budget planning

## Example Walkthrough
For coins = [1,2,5], amount = 11:

### Dynamic Programming Approach:
1. Initialize dp = [0,12,12,12,12,12,12,12,12,12,12,12]
2. For amount 1: dp = [0,1,12,12,12,12,12,12,12,12,12,12]
3. For amount 2: dp = [0,1,1,12,12,12,12,12,12,12,12,12]
4. For amount 3: dp = [0,1,1,2,12,12,12,12,12,12,12,12]
5. For amount 4: dp = [0,1,1,2,2,12,12,12,12,12,12,12]
6. For amount 5: dp = [0,1,1,2,2,1,12,12,12,12,12,12]
7. For amount 6: dp = [0,1,1,2,2,1,2,12,12,12,12,12]
8. For amount 7: dp = [0,1,1,2,2,1,2,2,12,12,12,12]
9. For amount 8: dp = [0,1,1,2,2,1,2,2,3,12,12,12]
10. For amount 9: dp = [0,1,1,2,2,1,2,2,3,3,12,12]
11. For amount 10: dp = [0,1,1,2,2,1,2,2,3,3,2,12]
12. For amount 11: dp = [0,1,1,2,2,1,2,2,3,3,2,3]
13. Return dp[11] = 3

### Recursive Approach with Memoization:
1. Start with amount = 11
2. Try coin 5: helper(6, {})
3. Try coin 2: helper(9, {})
4. Try coin 1: helper(10, {})
5. Build up solution using memoization
6. Return 3 (minimum coins needed) 