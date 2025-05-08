def binary_search(nums, target, find_first):
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            if find_first:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def search_range(nums: list[int], target: int) -> list[int]:
    first = binary_search(nums, target, True)
    last = binary_search(nums, target, False)
    return [first, last]

# Example usage
if __name__ == "__main__":
    print(search_range([5,7,7,8,8,10], 8))  # Output: [3, 4]
    print(search_range([5,7,7,8,8,10], 6))  # Output: [-1, -1]
