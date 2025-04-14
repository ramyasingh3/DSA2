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

def max_subarray(nums):
    if not nums:
        return 0
    
    current_sum = max_sum = nums[0]
    start_idx = end_idx = max_start_idx = max_end_idx = 0
    
    for i in range(1, len(nums)):
        # If current_sum becomes negative, start fresh from current element
        if current_sum < 0:
            current_sum = nums[i]
            start_idx = i
        else:
            current_sum += nums[i]
        
        # Update end index
        end_idx = i
        
        # Update maximum sum and indices if we find a better sum
        if current_sum > max_sum:
            max_sum = current_sum
            max_start_idx = start_idx
            max_end_idx = end_idx
    
    return max_sum, nums[max_start_idx:max_end_idx + 1]

def test_max_subarray():
    test_cases = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6, [4,-1,2,1]),
        ([1], 1, [1]),
        ([5,4,-1,7,8], 23, [5,4,-1,7,8]),
        ([-1], -1, [-1]),
        ([-2,-1], -1, [-1]),
        ([1,-1,1], 1, [1]),
        ([-2,1,-3,4,-1,2,1,-5,4], 6, [4,-1,2,1]),
    ]
    
    for i, (nums, expected_sum, expected_subarray) in enumerate(test_cases, 1):
        max_sum, subarray = max_subarray(nums)
        print(f"\nTest Case {i}:")
        print(f"Input array: {nums}")
        print(f"Expected sum: {expected_sum}, Got: {max_sum}")
        print(f"Expected subarray: {expected_subarray}")
        print(f"Got subarray: {subarray}")
        print("Result: ", "✓ Passed" if max_sum == expected_sum and subarray == expected_subarray 
              else "✗ Failed")
        print("-" * 50)

if __name__ == "__main__":
    test_max_subarray()
