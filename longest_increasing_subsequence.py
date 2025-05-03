def length_of_lis_dp(nums: list) -> int:
    """
    Find the length of the longest strictly increasing subsequence using dynamic programming.
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    
    n = len(nums)
    # dp[i] represents the length of LIS ending at index i
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

def length_of_lis_binary_search(nums: list) -> int:
    """
    Find the length of the longest strictly increasing subsequence using binary search.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    
    # sub[i] represents the smallest possible tail value for all increasing subsequences of length i+1
    sub = []
    
    for num in nums:
        # Find the first element in sub that is greater than or equal to num
        i = 0
        j = len(sub)
        while i < j:
            mid = (i + j) // 2
            if sub[mid] < num:
                i = mid + 1
            else:
                j = mid
        
        # If num is greater than all elements in sub, append it
        if i == len(sub):
            sub.append(num)
        # Otherwise, replace the first element that is greater than or equal to num
        else:
            sub[i] = num
    
    return len(sub)

def get_lis(nums: list) -> list:
    """
    Find the longest strictly increasing subsequence.
    Returns the actual subsequence, not just its length.
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    if not nums:
        return []
    
    n = len(nums)
    dp = [1] * n
    prev = [-1] * n  # To store the previous index for each element
    
    # Find the length of LIS ending at each index
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    # Find the index of the maximum value in dp
    max_len = max(dp)
    max_index = dp.index(max_len)
    
    # Reconstruct the LIS
    lis = []
    while max_index != -1:
        lis.append(nums[max_index])
        max_index = prev[max_index]
    
    return list(reversed(lis))

def main():
    # Test cases
    test_cases = [
        [10, 9, 2, 5, 3, 7, 101, 18],  # Expected: 4
        [0, 1, 0, 3, 2, 3],            # Expected: 4
        [7, 7, 7, 7, 7, 7, 7],         # Expected: 1
        [],                            # Expected: 0
        [1],                           # Expected: 1
        [1, 2, 3, 4, 5],              # Expected: 5
        [5, 4, 3, 2, 1],              # Expected: 1
        [1, 3, 6, 7, 9, 4, 10, 5, 6], # Expected: 6
    ]
    
    print("Testing Dynamic Programming solution:")
    for nums in test_cases:
        length = length_of_lis_dp(nums)
        print(f"Input: {nums}")
        print(f"Length of LIS: {length}")
        print()
    
    print("\nTesting Binary Search solution:")
    for nums in test_cases:
        length = length_of_lis_binary_search(nums)
        print(f"Input: {nums}")
        print(f"Length of LIS: {length}")
        print()
    
    print("\nTesting Get LIS solution:")
    for nums in test_cases:
        lis = get_lis(nums)
        print(f"Input: {nums}")
        print(f"LIS: {lis}")
        print(f"Length: {len(lis)}")
        print()

if __name__ == "__main__":
    main() 