from collections import Counter

def find_lonely(nums: list[int]) -> list[int]:
    freq = Counter(nums)
    result = []
    for num in nums:
        if freq[num] == 1 and freq.get(num - 1, 0) == 0 and freq.get(num + 1, 0) == 0:
            result.append(num)
    return result

# Example usage
if __name__ == "__main__":
    print(find_lonely([10, 6, 5, 8]))  # Output: [10, 8]
