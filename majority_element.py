"""
Problem: Majority Element

Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

from typing import List

def majority_element(nums: List[int]) -> int:
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

# Test cases
def test_majority_element():
    assert majority_element([3,2,3]) == 3
    assert majority_element([2,2,1,1,1,2,2]) == 2
    assert majority_element([1]) == 1
    assert majority_element([1,1,2]) == 1
    print("All test cases passed!")

if __name__ == "__main__":
    test_majority_element() 