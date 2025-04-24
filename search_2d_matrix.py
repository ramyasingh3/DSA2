def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    """
    Search for a target value in a 2D matrix.
    
    Args:
        matrix (list[list[int]]): 2D matrix with sorted rows and columns
        target (int): Value to search for
        
    Returns:
        bool: True if target is found, False otherwise
    """
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Convert 1D index to 2D coordinates
        row = mid // n
        col = mid % n
        mid_val = matrix[row][col]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Test cases
if __name__ == "__main__":
    # Test case 1
    matrix1 = [
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]
    ]
    target1 = 3
    print(f"Input: matrix = {matrix1}, target = {target1}")
    print(f"Output: {searchMatrix(matrix1, target1)}")  # Expected: True
    
    # Test case 2
    matrix2 = [
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]
    ]
    target2 = 13
    print(f"\nInput: matrix = {matrix2}, target = {target2}")
    print(f"Output: {searchMatrix(matrix2, target2)}")  # Expected: False
    
    # Test case 3
    matrix3 = [[1]]
    target3 = 1
    print(f"\nInput: matrix = {matrix3}, target = {target3}")
    print(f"Output: {searchMatrix(matrix3, target3)}")  # Expected: True
    
    # Test case 4
    matrix4 = [[1,1]]
    target4 = 2
    print(f"\nInput: matrix = {matrix4}, target = {target4}")
    print(f"Output: {searchMatrix(matrix4, target4)}")  # Expected: False 