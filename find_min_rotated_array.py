def findMin(nums: list[int]) -> int:
    """
    Find the minimum element in a rotated sorted array.
    
    Args:
        nums (list[int]): Rotated sorted array
        
    Returns:
        int: Minimum element in the array
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If mid element is greater than right element,
        # minimum is in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        # Otherwise, minimum is in the left half (including mid)
        else:
            right = mid
    
    # When left == right, we've found the minimum
    return nums[left]

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [3,4,5,1,2]
    print(f"Input: nums = {nums1}")
    print(f"Output: {findMin(nums1)}")  # Expected: 1
    
    # Test case 2
    nums2 = [4,5,6,7,0,1,2]
    print(f"\nInput: nums = {nums2}")
    print(f"Output: {findMin(nums2)}")  # Expected: 0
    
    # Test case 3
    nums3 = [11,13,15,17]
    print(f"\nInput: nums = {nums3}")
    print(f"Output: {findMin(nums3)}")  # Expected: 11
    
    # Test case 4
    nums4 = [2,1]
    print(f"\nInput: nums = {nums4}")
    print(f"Output: {findMin(nums4)}")  # Expected: 1 