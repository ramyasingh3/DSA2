def climb_stairs(n: int) -> int:
    """
    Calculate the number of distinct ways to climb n stairs,
    taking either 1 or 2 steps at a time.
    
    Args:
        n: Number of stairs to climb
        
    Returns:
        Number of distinct ways to climb
    """
    if n <= 2:
        return n
    
    # Initialize variables for first two steps
    prev_prev = 1  # ways to reach step 0
    prev = 2       # ways to reach step 1
    
    # Calculate ways for each step
    for i in range(2, n):
        current = prev + prev_prev
        prev_prev = prev
        prev = current
    
    return prev

def test_climb_stairs():
    """Test cases for the climbing stairs solution."""
    
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (7, 21),
        (8, 34),
        (9, 55),
        (10, 89)
    ]
    
    print("Testing Climbing Stairs Solution...")
    for n, expected in test_cases:
        result = climb_stairs(n)
        print(f"\nInput: n = {n}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_climb_stairs() 