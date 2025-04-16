def is_valid(s: str) -> bool:
    """
    Check if a string of parentheses is valid.
    
    Args:
        s: String containing only parentheses characters
        
    Returns:
        True if the parentheses are valid, False otherwise
    """
    # Mapping of closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in bracket_map:
            # If stack is empty or top doesn't match, invalid
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:
            # Push opening bracket onto stack
            stack.append(char)
    
    # Stack should be empty for valid parentheses
    return not stack

def test_valid_parentheses():
    """Test cases for the valid parentheses solution."""
    
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        ("]", False),
        ("((()))", True),
        ("([{}])", True),
        ("([{)]}", False)
    ]
    
    print("Testing Valid Parentheses Solution...")
    for s, expected in test_cases:
        result = is_valid(s)
        print(f"\nInput: {s}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_valid_parentheses() 