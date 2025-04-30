"""
Merge Sorted Arrays Implementation

This file contains multiple implementations to merge two sorted arrays.

Problem Statement:
Given two sorted arrays nums1 and nums2, merge them into a single sorted array.
The first array nums1 has enough space at the end to hold all elements from nums2.

Time Complexity: O(m + n) where m and n are the lengths of the arrays
Space Complexity: O(1) for in-place solution
"""

def merge_sorted_arrays_extra_space(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merge two sorted arrays using extra space.
    This approach creates a new array to store the result.
    
    Args:
        nums1 (list[int]): First sorted array with extra space
        m (int): Number of elements in nums1
        nums2 (list[int]): Second sorted array
        n (int): Number of elements in nums2
    """
    # Create a new array to store the result
    result = []
    i, j = 0, 0
    
    # Compare elements from both arrays and merge
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    
    # Add remaining elements from nums1
    while i < m:
        result.append(nums1[i])
        i += 1
    
    # Add remaining elements from nums2
    while j < n:
        result.append(nums2[j])
        j += 1
    
    # Copy result back to nums1
    for k in range(len(result)):
        nums1[k] = result[k]

def merge_sorted_arrays_inplace(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merge two sorted arrays in-place.
    This is the optimal solution with O(1) space complexity.
    
    Args:
        nums1 (list[int]): First sorted array with extra space
        m (int): Number of elements in nums1
        nums2 (list[int]): Second sorted array
        n (int): Number of elements in nums2
    """
    # Start from the end of both arrays
    p1, p2 = m - 1, n - 1
    p = m + n - 1  # Position to place the next element
    
    # While there are elements to compare
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

def merge_sorted_arrays_simple(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Merge two sorted arrays using a simple approach.
    First copy nums2 to the end of nums1, then sort.
    
    Args:
        nums1 (list[int]): First sorted array with extra space
        m (int): Number of elements in nums1
        nums2 (list[int]): Second sorted array
        n (int): Number of elements in nums2
    """
    # Copy nums2 to the end of nums1
    for i in range(n):
        nums1[m + i] = nums2[i]
    
    # Sort the entire array
    nums1.sort()

def test_merge_sorted_arrays():
    """Test cases for merge sorted arrays implementations"""
    test_cases = [
        # (nums1, m, nums2, n, expected)
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([1, 2, 3, 0, 0], 3, [4, 5], 2, [1, 2, 3, 4, 5]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        ([1, 3, 5, 0, 0, 0], 3, [2, 4, 6], 3, [1, 2, 3, 4, 5, 6]),
    ]
    
    for nums1, m, nums2, n, expected in test_cases:
        # Test extra space approach
        nums1_copy = nums1.copy()
        merge_sorted_arrays_extra_space(nums1_copy, m, nums2, n)
        assert nums1_copy == expected, f"Extra space test failed for {nums1[:m]} and {nums2}"
        
        # Test in-place approach
        nums1_copy = nums1.copy()
        merge_sorted_arrays_inplace(nums1_copy, m, nums2, n)
        assert nums1_copy == expected, f"In-place test failed for {nums1[:m]} and {nums2}"
        
        # Test simple approach
        nums1_copy = nums1.copy()
        merge_sorted_arrays_simple(nums1_copy, m, nums2, n)
        assert nums1_copy == expected, f"Simple test failed for {nums1[:m]} and {nums2}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_merge_sorted_arrays()
    
    # Example usage
    test_cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
        ([1], 1, [], 0),
        ([0], 0, [1], 1),
        ([1, 2, 3, 0, 0], 3, [4, 5], 2),
    ]
    
    print("\nTesting various arrays:")
    for nums1, m, nums2, n in test_cases:
        print(f"\nArrays: {nums1[:m]} and {nums2}")
        
        # Test extra space approach
        nums1_copy = nums1.copy()
        merge_sorted_arrays_extra_space(nums1_copy, m, nums2, n)
        print(f"Using extra space: {nums1_copy}")
        
        # Test in-place approach
        nums1_copy = nums1.copy()
        merge_sorted_arrays_inplace(nums1_copy, m, nums2, n)
        print(f"Using in-place: {nums1_copy}")
        
        # Test simple approach
        nums1_copy = nums1.copy()
        merge_sorted_arrays_simple(nums1_copy, m, nums2, n)
        print(f"Using simple: {nums1_copy}") 