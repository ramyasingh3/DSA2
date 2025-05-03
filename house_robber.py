def rob(nums):
    """
    Find the maximum amount of money you can rob tonight without alerting the police.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # Initialize variables for the two previous states
    prev2 = 0  # max money for houses[0...i-2]
    prev1 = nums[0]  # max money for houses[0...i-1]
    
    # For each house, decide whether to rob it or not
    for i in range(1, len(nums)):
        # Current max is max of:
        # 1. Robbing current house + max from two houses back
        # 2. Not robbing current house (keeping max from previous house)
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current
    
    return prev1

def rob_recursive(nums):
    """
    Recursive solution with memoization for the house robber problem.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def helper(i, memo):
        # Base cases
        if i < 0:
            return 0
        if i in memo:
            return memo[i]
        
        # For each house, we have two choices:
        # 1. Rob current house and skip next house
        # 2. Skip current house and move to next house
        memo[i] = max(helper(i - 1, memo),  # Skip current house
                     helper(i - 2, memo) + nums[i])  # Rob current house
        return memo[i]
    
    return helper(len(nums) - 1, {})

def main():
    # Test cases
    test_cases = [
        [1, 2, 3, 1],  # Expected: 4 (rob house 1 and 3)
        [2, 7, 9, 3, 1],  # Expected: 12 (rob house 1, 3, and 5)
        [1, 2],  # Expected: 2 (rob house 2)
        [1],  # Expected: 1 (rob house 1)
        [],  # Expected: 0 (no houses)
        [2, 1, 1, 2],  # Expected: 4 (rob house 1 and 4)
        [1, 3, 1, 3, 100],  # Expected: 103 (rob house 2 and 5)
    ]
    
    print("Testing Iterative solution:")
    for nums in test_cases:
        result = rob(nums)
        print(f"Houses: {nums}")
        print(f"Maximum amount that can be robbed: {result}")
        print()
    
    print("\nTesting Recursive solution with memoization:")
    for nums in test_cases:
        result = rob_recursive(nums)
        print(f"Houses: {nums}")
        print(f"Maximum amount that can be robbed: {result}")
        print()

if __name__ == "__main__":
    main() 