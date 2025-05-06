# DSA Short Question

# Problem Statement:
# Given an array of integers, find the maximum sum of a contiguous subarray.
# This is a classic problem known as "Kadane's Algorithm".

# Example:
# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6.

# Function to implement Kadane's Algorithm
def max_subarray_sum(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

# Test the function
if __name__ == "__main__":
    test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum subarray sum is", max_subarray_sum(test_array))
