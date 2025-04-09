from typing import List, List[List[int]]

class Solution:
    def three_sum_brute_force(self, nums: List[int]) -> List[List[int]]:
        """
        Brute force approach checking all possible triplets.
        Time Complexity: O(n³)
        Space Complexity: O(1)
        """
        result = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in result:
                            result.append(triplet)
        return result

    def three_sum_two_pointers(self, nums: List[int]) -> List[List[int]]:
        """
        Using sorting and two pointers.
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        result = []
        nums.sort()
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                    
        return result

    def three_sum_hash(self, nums: List[int]) -> List[List[int]]:
        """
        Using hash set to store complements.
        Time Complexity: O(n²)
        Space Complexity: O(n)
        """
        result = []
        nums.sort()
        n = len(nums)
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            seen = set()
            target = -nums[i]
            
            for j in range(i + 1, n):
                complement = target - nums[j]
                if complement in seen:
                    triplet = [nums[i], complement, nums[j]]
                    if triplet not in result:
                        result.append(triplet)
                seen.add(nums[j])
                
        return result

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    nums = [-1, 0, 1, 2, -1, -4]
    print("Test Case 1:")
    print(f"Input: {nums}")
    print("Brute Force:", solution.three_sum_brute_force(nums))
    print("Two Pointers:", solution.three_sum_two_pointers(nums))
    print("Hash Method:", solution.three_sum_hash(nums))
    print()
    
    # Test Case 2: No solution
    nums = [1, 2, 3, 4, 5]
    print("Test Case 2:")
    print(f"Input: {nums}")
    print("Brute Force:", solution.three_sum_brute_force(nums))
    print("Two Pointers:", solution.three_sum_two_pointers(nums))
    print("Hash Method:", solution.three_sum_hash(nums))
    print()
    
    # Test Case 3: All zeros
    nums = [0, 0, 0, 0]
    print("Test Case 3:")
    print(f"Input: {nums}")
    print("Brute Force:", solution.three_sum_brute_force(nums))
    print("Two Pointers:", solution.three_sum_two_pointers(nums))
    print("Hash Method:", solution.three_sum_hash(nums))
    print()
    
    # Test Case 4: Large numbers
    nums = [-100, -50, -25, 0, 25, 50, 100]
    print("Test Case 4:")
    print(f"Input: {nums}")
    print("Brute Force:", solution.three_sum_brute_force(nums))
    print("Two Pointers:", solution.three_sum_two_pointers(nums))
    print("Hash Method:", solution.three_sum_hash(nums))
    print()
    
    # Test Case 5: Empty array
    nums = []
    print("Test Case 5:")
    print(f"Input: {nums}")
    print("Brute Force:", solution.three_sum_brute_force(nums))
    print("Two Pointers:", solution.three_sum_two_pointers(nums))
    print("Hash Method:", solution.three_sum_hash(nums))

if __name__ == "__main__":
    test_solution() 