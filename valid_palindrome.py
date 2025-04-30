"""
Valid Palindrome Implementation

This file contains multiple implementations to check if a string is a valid palindrome.

Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1) for two-pointer solution
"""

def is_palindrome_two_pointers(s: str) -> bool:
    """
    Check if string is palindrome using two pointers.
    This is the optimal solution with O(1) space complexity.
    
    Args:
        s (str): Input string
        
    Returns:
        bool: True if string is palindrome, False otherwise
    """
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Use two pointers from both ends
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

def is_palindrome_reverse(s: str) -> bool:
    """
    Check if string is palindrome by comparing with its reverse.
    This approach is more readable but uses extra space.
    
    Args:
        s (str): Input string
        
    Returns:
        bool: True if string is palindrome, False otherwise
    """
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Compare string with its reverse
    return s == s[::-1]

def is_palindrome_stack(s: str) -> bool:
    """
    Check if string is palindrome using a stack.
    This approach demonstrates a different way of thinking.
    
    Args:
        s (str): Input string
        
    Returns:
        bool: True if string is palindrome, False otherwise
    """
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Push first half of characters to stack
    stack = []
    mid = len(s) // 2
    
    for i in range(mid):
        stack.append(s[i])
    
    # Skip middle character if length is odd
    start = mid + 1 if len(s) % 2 == 1 else mid
    
    # Compare remaining characters with stack
    for i in range(start, len(s)):
        if stack.pop() != s[i]:
            return False
    
    return True

def test_valid_palindrome():
    """Test cases for valid palindrome implementations"""
    test_cases = [
        ("A man, a plan, a canal: Panama", True),    # Valid palindrome
        ("race a car", False),                       # Not a palindrome
        ("", True),                                  # Empty string
        (" ", True),                                 # Single space
        ("a", True),                                 # Single character
        ("ab", False),                               # Two different characters
        ("aa", True),                                # Two same characters
        ("0P", False),                               # Numbers and letters
        ("12321", True),                             # Numbers only
        ("Was it a car or a cat I saw?", True),      # Complex palindrome
        ("hello", False),                            # Not a palindrome
        ("Madam, I'm Adam", True),                   # Case-insensitive
    ]
    
    for s, expected in test_cases:
        # Test two pointers approach
        assert is_palindrome_two_pointers(s) == expected, \
            f"Two pointers test failed for '{s}'"
        
        # Test reverse approach
        assert is_palindrome_reverse(s) == expected, \
            f"Reverse test failed for '{s}'"
        
        # Test stack approach
        assert is_palindrome_stack(s) == expected, \
            f"Stack test failed for '{s}'"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_valid_palindrome()
    
    # Example usage
    test_strings = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "hello",
        "12321",
        "Madam, I'm Adam"
    ]
    
    print("\nTesting various strings:")
    for s in test_strings:
        print(f"\nString: '{s}'")
        print(f"Using two pointers: {is_palindrome_two_pointers(s)}")
        print(f"Using reverse: {is_palindrome_reverse(s)}")
        print(f"Using stack: {is_palindrome_stack(s)}") 