def max_subarray_sum(nums: list[int]) -> int:
    """
    Find the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    Args:
        nums (list[int]): List of integers
        
    Returns:
        int: Maximum sum of a contiguous subarray
    """
    if not nums:
        return 0
        
    max_so_far = float('-inf')
    max_ending_here = 0
    
    for num in nums:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

def main():
    # Test cases
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],  # Expected: 6 (subarray [4,-1,2,1])
        [1],                              # Expected: 1
        [5, 4, -1, 7, 8],                # Expected: 23 (subarray [5,4,-1,7,8])
        [-1, -2, -3],                    # Expected: -1 (subarray [-1])
        [],                              # Expected: 0
    ]
    
    for nums in test_cases:
        result = max_subarray_sum(nums)
        print(f"Input: nums = {nums}")
        print(f"Output: {result}\n")

if __name__ == "__main__":
    main() 