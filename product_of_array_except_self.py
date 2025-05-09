"""
Product of Array Except Self

Problem:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: 
- answer[0] = 2 * 3 * 4 = 24
- answer[1] = 1 * 3 * 4 = 12
- answer[2] = 1 * 2 * 4 = 8
- answer[3] = 1 * 2 * 3 = 6

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Time Complexity: O(n) where n is the length of the input array
Space Complexity: O(1) if we don't count the output array
"""

from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n
    
    # Calculate prefix products
    # For each position i, answer[i] will contain product of all numbers before i
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    
    # Calculate suffix products and combine with prefix products
    # For each position i, multiply answer[i] with product of all numbers after i
    suffix = 1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    
    return answer

# Test cases
def test_product_except_self():
    # Test case 1: Basic case with positive numbers
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    
    # Test case 2: Array with zero
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    
    # Test case 3: Array with two zeros
    assert product_except_self([0, 0]) == [0, 0]
    
    # Test case 4: Array with negative numbers
    assert product_except_self([-1, -2, -3, -4]) == [-24, -12, -8, -6]
    
    # Test case 5: Single element array
    assert product_except_self([1]) == [1]
    
    # Test case 6: Array with one zero
    assert product_except_self([1, 0, 3, 4]) == [0, 12, 0, 0]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_product_except_self() 