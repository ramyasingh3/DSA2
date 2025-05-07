def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Example usage
if __name__ == "__main__":
    print(two_sum_sorted([2, 7, 11, 15], 9))     # Output: [1, 2]
    print(two_sum_sorted([1, 2, 3, 4, 4], 8))    # Output: [4, 5]
