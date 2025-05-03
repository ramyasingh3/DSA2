def length_of_lis(nums):
    """
    Find the length of the longest strictly increasing subsequence.
    Time Complexity: O(n²)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    
    n = len(nums)
    # dp[i] represents the length of LIS ending at index i
    dp = [1] * n
    
    # For each position, check all previous positions
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def length_of_lis_binary_search(nums):
    """
    Find the length of the longest strictly increasing subsequence using binary search.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    
    # dp[i] represents the smallest possible tail value for all increasing subsequences of length i+1
    dp = []
    
    for num in nums:
        # Find the first element in dp that is greater than or equal to num
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        # If num is greater than all elements in dp, append it
        if left == len(dp):
            dp.append(num)
        # Otherwise, replace the first element that is greater than or equal to num
        else:
            dp[left] = num
    
    return len(dp)

def main():
    # Test cases
    test_cases = [
        [10, 9, 2, 5, 3, 7, 101, 18],  # Expected: 4
        [0, 1, 0, 3, 2, 3],  # Expected: 4
        [7, 7, 7, 7, 7, 7, 7],  # Expected: 1
        [],  # Expected: 0
        [1],  # Expected: 1
        [1, 2, 3, 4, 5],  # Expected: 5
        [5, 4, 3, 2, 1],  # Expected: 1
    ]
    
    print("Testing O(n²) solution:")
    for nums in test_cases:
        result = length_of_lis(nums)
        print(f"Input: {nums}")
        print(f"Length of LIS: {result}")
        print()
    
    print("\nTesting O(n log n) solution:")
    for nums in test_cases:
        result = length_of_lis_binary_search(nums)
        print(f"Input: {nums}")
        print(f"Length of LIS: {result}")
        print()

if __name__ == "__main__":
    main() 