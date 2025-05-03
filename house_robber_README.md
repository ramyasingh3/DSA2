# House Robber

## Problem Description
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Examples
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

## Constraints
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

## Approach 1: Dynamic Programming (Iterative)
1. For each house, we have two choices:
   - Rob the current house and skip the next house
   - Skip the current house and move to the next house
2. Keep track of maximum money for previous two states:
   - prev2: maximum money for houses[0...i-2]
   - prev1: maximum money for houses[0...i-1]
3. For each house i:
   - Current maximum = max(prev1, prev2 + nums[i])
   - Update prev2 = prev1
   - Update prev1 = current maximum
4. Return the final maximum

## Approach 2: Recursive with Memoization
1. Create a recursive function that takes current index and memo dictionary
2. Base cases:
   - If index < 0, return 0
   - If index in memo, return memoized value
3. For each house, we have two choices:
   - Rob current house and skip next house
   - Skip current house and move to next house
4. Memoize and return the maximum of these choices

## Time and Space Complexity
### Approach 1 (Iterative)
- Time Complexity: O(n)
- Space Complexity: O(1)

### Approach 2 (Recursive with Memoization)
- Time Complexity: O(n)
- Space Complexity: O(n)

## Key Points
- This is a classic dynamic programming problem
- We can't rob adjacent houses
- We need to consider all possible combinations
- The iterative approach is more space-efficient
- Both approaches handle edge cases (empty array, single house)

## Common Applications
- Resource allocation
- Scheduling problems
- Network optimization
- Game theory
- Decision making
- Risk assessment

## Example Walkthrough
For nums = [1,2,3,1]:

### Iterative Approach:
1. Initialize prev2 = 0, prev1 = 1
2. For house 2 (nums[1] = 2):
   - current = max(1, 0 + 2) = 2
   - prev2 = 1, prev1 = 2
3. For house 3 (nums[2] = 3):
   - current = max(2, 1 + 3) = 4
   - prev2 = 2, prev1 = 4
4. For house 4 (nums[3] = 1):
   - current = max(4, 2 + 1) = 4
   - prev2 = 4, prev1 = 4
5. Return prev1 = 4

### Recursive Approach with Memoization:
1. Start with index 3
2. Try robbing house 4: helper(1, {}) + 1
3. Try skipping house 4: helper(2, {})
4. Build up solution using memoization
5. Return 4 (maximum amount that can be robbed) 