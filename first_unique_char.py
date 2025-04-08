from collections import Counter, OrderedDict
from typing import Dict

class Solution:
    def first_unique_char_counter(self, s: str) -> int:
        """
        Counter solution with O(n) time complexity.
        Uses Counter to count character frequencies.
        """
        # Count character frequencies
        counts = Counter(s)
        
        # Find first character with count 1
        for i, char in enumerate(s):
            if counts[char] == 1:
                return i
        return -1

    def first_unique_char_dict(self, s: str) -> int:
        """
        Dictionary solution with O(n) time complexity.
        Uses a dictionary to track both count and first index.
        """
        char_count: Dict[str, tuple[int, int]] = {}  # char -> (count, first_index)
        
        # Count characters and store first index
        for i, char in enumerate(s):
            count, index = char_count.get(char, (0, i))
            char_count[char] = (count + 1, index)
        
        # Find first character with count 1
        min_index = float('inf')
        for char, (count, index) in char_count.items():
            if count == 1:
                min_index = min(min_index, index)
        
        return min_index if min_index != float('inf') else -1

    def first_unique_char_ordered_dict(self, s: str) -> int:
        """
        OrderedDict solution with O(n) time complexity.
        Uses OrderedDict to maintain character order.
        """
        char_count = OrderedDict()
        
        # Count characters
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Find first character with count 1
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        return -1

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    s1 = "leetcode"
    print("Test Case 1:")
    print(f"Input: {s1}")
    print(f"Counter: {solution.first_unique_char_counter(s1)}")
    print(f"Dictionary: {solution.first_unique_char_dict(s1)}")
    print(f"OrderedDict: {solution.first_unique_char_ordered_dict(s1)}")
    print()
    
    # Test Case 2: No unique character
    s2 = "aabb"
    print("Test Case 2:")
    print(f"Input: {s2}")
    print(f"Counter: {solution.first_unique_char_counter(s2)}")
    print(f"Dictionary: {solution.first_unique_char_dict(s2)}")
    print(f"OrderedDict: {solution.first_unique_char_ordered_dict(s2)}")
    print()
    
    # Test Case 3: All unique characters
    s3 = "abcde"
    print("Test Case 3:")
    print(f"Input: {s3}")
    print(f"Counter: {solution.first_unique_char_counter(s3)}")
    print(f"Dictionary: {solution.first_unique_char_dict(s3)}")
    print(f"OrderedDict: {solution.first_unique_char_ordered_dict(s3)}")
    print()
    
    # Test Case 4: Empty string
    s4 = ""
    print("Test Case 4:")
    print(f"Input: {s4}")
    print(f"Counter: {solution.first_unique_char_counter(s4)}")
    print(f"Dictionary: {solution.first_unique_char_dict(s4)}")
    print(f"OrderedDict: {solution.first_unique_char_ordered_dict(s4)}")
    print()
    
    # Test Case 5: Single character
    s5 = "z"
    print("Test Case 5:")
    print(f"Input: {s5}")
    print(f"Counter: {solution.first_unique_char_counter(s5)}")
    print(f"Dictionary: {solution.first_unique_char_dict(s5)}")
    print(f"OrderedDict: {solution.first_unique_char_ordered_dict(s5)}")

if __name__ == "__main__":
    test_solution() 