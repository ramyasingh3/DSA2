def move_zeros(nums: list[int]) -> list[int]:
    non_zeros = [num for num in nums if num != 0]
    zeros = [0] * (len(nums) - len(non_zeros))
    return non_zeros + zeros

# Example usage
if __name__ == "__main__":
    print(move_zeros([0, 1, 0, 3, 12]))   # [1, 3, 12, 0, 0]
    print(move_zeros([0, 0, 1]))          # [1, 0, 0]
    print(move_zeros([1, 2, 3]))          # [1, 2, 3]
