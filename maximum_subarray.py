"""
Maximum Subarray Implementation

This file contains multiple implementations to find the contiguous subarray with the largest sum.

Problem Statement:
Given an integer array nums, find the subarray with the largest sum, and return its sum.
A subarray is a contiguous non-empty sequence of elements within an array.

Time Complexity: O(n) for optimal solution
Space Complexity: O(1) for optimal solution
"""

def max_subarray_kadane(nums: list[int]) -> int:
    """
    Find maximum subarray sum using Kadane's Algorithm.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def max_subarray_with_indices(nums: list[int]) -> tuple[int, int, int]:
    """
    Find maximum subarray sum and its start/end indices using Kadane's Algorithm.
    Returns (max_sum, start_index, end_index)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0, -1, -1
    
    max_sum = current_sum = nums[0]
    start = end = max_start = 0
    
    for i, num in enumerate(nums[1:], 1):
        if num > current_sum + num:
            current_sum = num
            start = i
        else:
            current_sum += num
            
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = start
            end = i
    
    return max_sum, max_start, end

def max_subarray_divide_conquer(nums: list[int]) -> int:
    """
    Find maximum subarray sum using divide and conquer approach.
    Time Complexity: O(n log n)
    Space Complexity: O(log n) due to recursion stack
    """
    def find_max_crossing(nums: list[int], left: int, mid: int, right: int) -> int:
        # Find maximum sum for left side
        left_sum = float('-inf')
        current_sum = 0
        for i in range(mid, left - 1, -1):
            current_sum += nums[i]
            left_sum = max(left_sum, current_sum)
        
        # Find maximum sum for right side
        right_sum = float('-inf')
        current_sum = 0
        for i in range(mid + 1, right + 1):
            current_sum += nums[i]
            right_sum = max(right_sum, current_sum)
        
        return left_sum + right_sum
    
    def find_max_subarray(nums: list[int], left: int, right: int) -> int:
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        
        # Find maximum sum in left and right halves
        left_sum = find_max_subarray(nums, left, mid)
        right_sum = find_max_subarray(nums, mid + 1, right)
        
        # Find maximum sum crossing the middle
        cross_sum = find_max_crossing(nums, left, mid, right)
        
        return max(left_sum, right_sum, cross_sum)
    
    if not nums:
        return 0
    
    return find_max_subarray(nums, 0, len(nums) - 1)

def max_subarray_dp(nums: list[int]) -> int:
    """
    Find maximum subarray sum using dynamic programming.
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [0] * n  # dp[i] represents max sum ending at index i
    dp[0] = nums[0]
    max_sum = dp[0]
    
    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
        max_sum = max(max_sum, dp[i])
    
    return max_sum

def test_max_subarray():
    """Test cases for maximum subarray implementations"""
    test_cases = [
        ([1], 1),                              # Single element
        ([-2,1,-3,4,-1,2,1,-5,4], 6),         # Classic case
        ([-1], -1),                            # Single negative
        ([-2,-1], -1),                         # All negative
        ([5,4,-1,7,8], 23),                    # All positive sum
        [1,2,-1,-2,2,1,-2,1,4,-5,4], 6),      # Complex case
        ([-2,-3,-1], -1),                      # All negative
        ([0,0,0,0], 0),                        # All zeros
        ([1,-1,1,-1], 1),                      # Alternating
        ([-1,-1,2,3,-2,4,-1,-2,3,-1], 7),     # Multiple peaks
    ]
    
    for nums, expected in test_cases:
        # Test Kadane's Algorithm
        result = max_subarray_kadane(nums)
        assert result == expected, f"Kadane test failed for {nums}"
        
        # Test Divide and Conquer
        result = max_subarray_divide_conquer(nums)
        assert result == expected, f"Divide and Conquer test failed for {nums}"
        
        # Test Dynamic Programming
        result = max_subarray_dp(nums)
        assert result == expected, f"DP test failed for {nums}"
        
        # Test with indices (only check sum)
        max_sum, _, _ = max_subarray_with_indices(nums)
        assert max_sum == expected, f"With indices test failed for {nums}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_max_subarray()
    
    # Example usage
    test_arrays = [
        [1],
        [-2,1,-3,4,-1,2,1,-5,4],
        [-1],
        [-2,-1],
        [5,4,-1,7,8],
        [1,2,-1,-2,2,1,-2,1,4,-5,4],
        [-2,-3,-1],
        [0,0,0,0],
        [1,-1,1,-1],
        [-1,-1,2,3,-2,4,-1,-2,3,-1]
    ]
    
    print("\nTesting various arrays:")
    for nums in test_arrays:
        print(f"\nArray: {nums}")
        print(f"Using Kadane's Algorithm: {max_subarray_kadane(nums)}")
        max_sum, start, end = max_subarray_with_indices(nums)
        print(f"With indices (sum={max_sum}, subarray={nums[start:end+1]})")
        print(f"Using Divide and Conquer: {max_subarray_divide_conquer(nums)}")
        print(f"Using Dynamic Programming: {max_subarray_dp(nums)}")
