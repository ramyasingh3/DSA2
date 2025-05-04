def length_of_lis_dp(nums: list[int]) -> int:
    """
    Find the length of the longest strictly increasing subsequence using dynamic programming.
    Time Complexity: O(n²)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  # dp[i] represents the length of LIS ending at index i
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def length_of_lis_binary_search(nums: list[int]) -> int:
    """
    Find the length of the longest strictly increasing subsequence using binary search.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    
    # dp[i] represents the smallest tail of all increasing subsequences of length i+1
    dp = []
    
    for num in nums:
        # Find the first index in dp where dp[index] >= num
        left, right = 0, len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        # If num is larger than all elements in dp, append it
        if left == len(dp):
            dp.append(num)
        # Otherwise, replace the first element that is >= num
        else:
            dp[left] = num
    
    return len(dp)

def get_lis(nums: list[int]) -> list[int]:
    """
    Find the actual longest increasing subsequence.
    Time Complexity: O(n²)
    Space Complexity: O(n)
    """
    if not nums:
        return []
    
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n  # To store the previous index for reconstruction
    
    # Fill dp and prev arrays
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    # Find the index of the maximum value in dp
    max_len = max(dp)
    max_index = dp.index(max_len)
    
    # Reconstruct the subsequence
    lis = []
    while max_index != -1:
        lis.append(nums[max_index])
        max_index = prev[max_index]
    
    return lis[::-1]

def main():
    # Test cases
    test_cases = [
        [10, 9, 2, 5, 3, 7, 101, 18],  # Expected: 4 ([2, 5, 7, 101])
        [0, 1, 0, 3, 2, 3],            # Expected: 4 ([0, 1, 2, 3])
        [7, 7, 7, 7, 7, 7, 7],         # Expected: 1 ([7])
        [],                             # Expected: 0 ([])
        [1],                            # Expected: 1 ([1])
        [1, 2, 3, 4, 5],               # Expected: 5 ([1, 2, 3, 4, 5])
        [5, 4, 3, 2, 1],               # Expected: 1 ([5])
        [1, 3, 6, 7, 9, 4, 10, 5, 6],  # Expected: 6 ([1, 3, 6, 7, 9, 10])
        [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12],  # Expected: 6 ([3, 5, 6, 7, 12])
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Expected: 10
    ]
    
    print("Testing Dynamic Programming solution:")
    for nums in test_cases:
        length = length_of_lis_dp(nums)
        subsequence = get_lis(nums)
        print(f"Input: {nums}")
        print(f"Length of LIS: {length}")
        print(f"LIS: {subsequence}")
        print()
    
    print("\nTesting Binary Search solution:")
    for nums in test_cases:
        length = length_of_lis_binary_search(nums)
        print(f"Input: {nums}")
        print(f"Length of LIS: {length}")
        print()

if __name__ == "__main__":
    main() 