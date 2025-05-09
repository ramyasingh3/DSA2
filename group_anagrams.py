"""
Group Anagrams

Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Time Complexity: O(n * k * log k) where n is the number of strings and k is the maximum length of a string
Space Complexity: O(n * k) to store the grouped anagrams
"""

from collections import defaultdict
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    # Create a defaultdict to store groups of anagrams
    # Key: sorted string, Value: list of original strings
    anagram_groups = defaultdict(list)
    
    # Iterate through each string in the input list
    for s in strs:
        # Sort the string to create a key
        # All anagrams will have the same sorted string
        sorted_s = ''.join(sorted(s))
        # Add the original string to the group
        anagram_groups[sorted_s].append(s)
    
    # Return all groups as a list of lists
    return list(anagram_groups.values())

# Test cases
def test_group_anagrams():
    # Test case 1: Multiple groups
    input1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = group_anagrams(input1)
    # Sort each group and the overall result for consistent comparison
    result1 = [sorted(group) for group in result1]
    result1.sort()
    expected1 = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    expected1 = [sorted(group) for group in expected1]
    expected1.sort()
    assert result1 == expected1
    
    # Test case 2: Empty string
    input2 = [""]
    assert group_anagrams(input2) == [[""]]
    
    # Test case 3: Single character
    input3 = ["a"]
    assert group_anagrams(input3) == [["a"]]
    
    # Test case 4: Empty input
    input4 = []
    assert group_anagrams(input4) == []
    
    # Test case 5: All same strings
    input5 = ["abc", "abc", "abc"]
    result5 = group_anagrams(input5)
    assert len(result5) == 1 and len(result5[0]) == 3
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_group_anagrams() 