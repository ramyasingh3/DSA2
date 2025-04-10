from typing import List

class Solution:
    def remove_duplicates_two_pointers(self, nums: List[int]) -> int:
        """
        Two pointers approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
            
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                
        return i + 1
        
    def remove_duplicates_set(self, nums: List[int]) -> int:
        """
        Set-based approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        unique_nums = list(set(nums))
        unique_nums.sort()
        nums[:len(unique_nums)] = unique_nums
        return len(unique_nums)
        
    def remove_duplicates_groupby(self, nums: List[int]) -> int:
        """
        Groupby approach
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        from itertools import groupby
        unique_nums = [k for k, _ in groupby(nums)]
        nums[:len(unique_nums)] = unique_nums
        return len(unique_nums)

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    print("Test Case 1: Basic case")
    nums = [1, 1, 2]
    result = solution.remove_duplicates_two_pointers(nums.copy())
    print(f"Input: {nums}")
    print(f"Output: {result}, nums = {nums[:result]}")
    print()
    
    # Test Case 2: All duplicates
    print("Test Case 2: All duplicates")
    nums = [1, 1, 1, 1]
    result = solution.remove_duplicates_two_pointers(nums.copy())
    print(f"Input: {nums}")
    print(f"Output: {result}, nums = {nums[:result]}")
    print()
    
    # Test Case 3: No duplicates
    print("Test Case 3: No duplicates")
    nums = [1, 2, 3, 4]
    result = solution.remove_duplicates_two_pointers(nums.copy())
    print(f"Input: {nums}")
    print(f"Output: {result}, nums = {nums[:result]}")
    print()
    
    # Test Case 4: Empty array
    print("Test Case 4: Empty array")
    nums = []
    result = solution.remove_duplicates_two_pointers(nums.copy())
    print(f"Input: {nums}")
    print(f"Output: {result}, nums = {nums[:result]}")
    print()
    
    # Test Case 5: Large array
    print("Test Case 5: Large array")
    nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    result = solution.remove_duplicates_two_pointers(nums.copy())
    print(f"Input: {nums}")
    print(f"Output: {result}, nums = {nums[:result]}")
    print()
    
    # Test all methods
    print("Testing all methods:")
    nums = [1, 1, 2, 2, 3]
    
    print("Two Pointers:")
    result = solution.remove_duplicates_two_pointers(nums.copy())
    print(f"Result: {result}, nums = {nums[:result]}")
    
    print("Set-based:")
    result = solution.remove_duplicates_set(nums.copy())
    print(f"Result: {result}, nums = {nums[:result]}")
    
    print("Groupby:")
    result = solution.remove_duplicates_groupby(nums.copy())
    print(f"Result: {result}, nums = {nums[:result]}")

if __name__ == "__main__":
    test_solution() 