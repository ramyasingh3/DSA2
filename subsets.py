def subsets(nums: list[int]) -> list[list[int]]:
    result = []

    def backtrack(start=0, path=[]):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack()
    return result

# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3]
    print(subsets(nums))
