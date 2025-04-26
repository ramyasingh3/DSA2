"""
Problem: Find All Duplicates in an Array

Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []
"""

from typing import List

def find_duplicates(nums: List[int]) -> List[int]:
    res = []
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            res.append(abs(num))
        else:
            nums[idx] = -nums[idx]
    return res

# Test cases
def test_find_duplicates():
    assert sorted(find_duplicates([4,3,2,7,8,2,3,1])) == [2,3]
    assert find_duplicates([1,1,2]) == [1]
    assert find_duplicates([1]) == []
    assert sorted(find_duplicates([2,2,3,3,4,4])) == [2,3,4]
    print("All test cases passed!")

if __name__ == "__main__":
    test_find_duplicates() 