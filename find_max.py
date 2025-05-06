def find_max(nums: list[int]) -> int:
    if not nums:
        raise ValueError("List is empty")
    max_num = nums[0]
    for num in nums[1:]:
        if num > max_num:
            max_num = num
    return max_num

# Example usage
if __name__ == "__main__":
    print(find_max([3, 5, 1, 8, 2]))  # Output: 8
    print(find_max([-10, -5, -3]))    # Output: -3
