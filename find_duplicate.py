def find_duplicate(nums: list[int]) -> int:
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1  # Should never happen based on problem description

# Example usage
if __name__ == "__main__":
    print(find_duplicate([1, 3, 4, 2, 2]))  # Output: 2
    print(find_duplicate([3, 1, 3, 4, 2]))  # Output: 3
