"""
Problem: Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive 
elements sequence. The sequence must be strictly consecutive (numbers increasing by 1).

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Length = 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Explanation: The longest consecutive elements sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]. Length = 9.

Time Complexity: O(n) where n is the length of the input array
Space Complexity: O(n) to store the numbers in a set
"""

from typing import List

def longest_consecutive(nums: List[int]) -> int:
    if not nums:
        return 0
    
    # Convert to set for O(1) lookup
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start checking sequences from the smallest number in the sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            # Update max_length if current sequence is longer
            max_length = max(max_length, current_length)
    
    return max_length

def test_longest_consecutive():
    test_cases = [
        ([100,4,200,1,3,2], 4),
        ([0,3,7,2,5,8,4,6,0,1], 9),
        ([], 0),
        ([1], 1),
        ([1,2,3,5,7,8,9], 3),
        ([1,1,1,1], 1),
        ([5,4,3,2,1], 5),
    ]
    
    for i, (nums, expected_length) in enumerate(test_cases, 1):
        length = longest_consecutive(nums)
        print(f"\nTest Case {i}:")
        print(f"Input array: {nums}")
        print(f"Expected length: {expected_length}, Got: {length}")
        
        # Check if the result is correct
        # Note: For cases with multiple possible sequences of same length,
        # we only check the length
        result = "✓ Passed" if length == expected_length else "✗ Failed"
        print(f"Result: {result}")
        print("-" * 50)

if __name__ == "__main__":
    test_longest_consecutive()
