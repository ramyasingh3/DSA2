def search(nums: list[int], target: int) -> int:
    """
    Search for a target value in a rotated sorted array.
    
    Args:
        nums (list[int]): Rotated sorted array
        target (int): Value to search for
        
    Returns:
        int: Index of target if found, -1 otherwise
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
            
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            # Check if target is in the left half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            # Check if target is in the right half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [4,5,6,7,0,1,2]
    target1 = 0
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {search(nums1, target1)}")  # Expected: 4
    
    # Test case 2
    nums2 = [4,5,6,7,0,1,2]
    target2 = 3
    print(f"\nInput: nums = {nums2}, target = {target2}")
    print(f"Output: {search(nums2, target2)}")  # Expected: -1
    
    # Test case 3
    nums3 = [1]
    target3 = 0
    print(f"\nInput: nums = {nums3}, target = {target3}")
    print(f"Output: {search(nums3, target3)}")  # Expected: -1
    
    # Test case 4
    nums4 = [4,5,6,7,8,1,2,3]
    target4 = 8
    print(f"\nInput: nums = {nums4}, target = {target4}")
    print(f"Output: {search(nums4, target4)}")  # Expected: 4 