"""
Problem: Maximum Subarray Sum (Kadane's Algorithm)

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6

Input: [1]
Output: 1

Input: [5,4,-1,7,8]
Output: 23
"""

from typing import List

def max_subarray(nums: List[int]) -> int:
    """
    Find the maximum sum of any contiguous subarray.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum sum of any contiguous subarray
    """
    if not nums:
        return 0
        
    current_sum = max_sum = nums[0]
    
    for num in nums[1:]:
        # Choose between starting new subarray or continuing current
        current_sum = max(num, current_sum + num)
        # Update max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def test_max_subarray():
    """Test cases for the maximum subarray solution."""
    
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1, -2, -3, -4], -1),
        ([1, 2, 3, 4, 5], 15),
        ([-2, -3, 4, -1, -2, 1, 5, -3], 7),
        ([2, -1, 2, 3, -9, 3], 6),
        ([-1, -2, -3, -4, -5], -1)
    ]
    
    print("Testing Maximum Subarray Solution...")
    for nums, expected in test_cases:
        result = max_subarray(nums)
        print(f"\nInput: nums = {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_max_subarray()
