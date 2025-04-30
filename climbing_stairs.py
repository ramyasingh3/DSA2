"""
Climbing Stairs Implementation

This file contains multiple implementations to solve the climbing stairs problem.

Problem Statement:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Time Complexity: O(n) for optimal solutions
Space Complexity: O(1) for optimal solutions
"""

def climb_stairs_recursive(n: int) -> int:
    """
    Solve climbing stairs using recursive approach.
    Note: This is not efficient for large n due to repeated calculations.
    
    Args:
        n (int): Number of steps
        
    Returns:
        int: Number of distinct ways to climb
    """
    if n <= 2:
        return n
    
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)

def climb_stairs_dp(n: int) -> int:
    """
    Solve climbing stairs using dynamic programming.
    This approach stores intermediate results to avoid repeated calculations.
    
    Args:
        n (int): Number of steps
        
    Returns:
        int: Number of distinct ways to climb
    """
    if n <= 2:
        return n
    
    # dp[i] represents number of ways to climb i steps
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

def climb_stairs_optimal(n: int) -> int:
    """
    Solve climbing stairs using optimal approach.
    This solution uses constant space by keeping track of only two previous values.
    
    Args:
        n (int): Number of steps
        
    Returns:
        int: Number of distinct ways to climb
    """
    if n <= 2:
        return n
    
    # Keep track of previous two values
    prev2, prev1 = 1, 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1

def climb_stairs_matrix(n: int) -> int:
    """
    Solve climbing stairs using matrix exponentiation.
    This approach uses the fact that the solution follows Fibonacci sequence.
    
    Args:
        n (int): Number of steps
        
    Returns:
        int: Number of distinct ways to climb
    """
    if n <= 2:
        return n
    
    def multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        """Multiply two 2x2 matrices"""
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]
        ]
    
    def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
        """Calculate matrix power using binary exponentiation"""
        if power == 1:
            return matrix
        
        if power % 2 == 0:
            half_power = matrix_power(matrix, power // 2)
            return multiply(half_power, half_power)
        else:
            return multiply(matrix, matrix_power(matrix, power - 1))
    
    # Initial matrix for Fibonacci sequence
    matrix = [[1, 1], [1, 0]]
    result = matrix_power(matrix, n - 1)
    
    return result[0][0] + result[0][1]

def test_climb_stairs():
    """Test cases for climbing stairs implementations"""
    test_cases = [
        (1, 1),      # One step
        (2, 2),      # Two steps
        (3, 3),      # Three steps
        (4, 5),      # Four steps
        (5, 8),      # Five steps
        (6, 13),     # Six steps
        (7, 21),     # Seven steps
        (8, 34),     # Eight steps
    ]
    
    for n, expected in test_cases:
        # Test recursive approach (only for small n)
        if n <= 10:
            assert climb_stairs_recursive(n) == expected, \
                f"Recursive test failed for n = {n}"
        
        # Test DP approach
        assert climb_stairs_dp(n) == expected, \
            f"DP test failed for n = {n}"
        
        # Test optimal approach
        assert climb_stairs_optimal(n) == expected, \
            f"Optimal test failed for n = {n}"
        
        # Test matrix approach
        assert climb_stairs_matrix(n) == expected, \
            f"Matrix test failed for n = {n}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_climb_stairs()
    
    # Example usage
    test_steps = [1, 2, 3, 4, 5, 6]
    
    print("\nTesting various step counts:")
    for n in test_steps:
        print(f"\nSteps: {n}")
        if n <= 10:
            print(f"Using recursive: {climb_stairs_recursive(n)}")
        print(f"Using DP: {climb_stairs_dp(n)}")
        print(f"Using optimal: {climb_stairs_optimal(n)}")
        print(f"Using matrix: {climb_stairs_matrix(n)}") 