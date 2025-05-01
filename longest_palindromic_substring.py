def longest_palindrome(s: str) -> str:
    """
    Given a string s, return the longest palindromic substring in s.
    
    Args:
        s (str): Input string
        
    Returns:
        str: Longest palindromic substring
    """
    if not s:
        return ""
    
    def expand_around_center(left: int, right: int) -> str:
        """Helper function to expand around center and find palindrome"""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    for i in range(len(s)):
        # Check for odd length palindromes
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        
        # Check for even length palindromes
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    
    return longest

def test_longest_palindrome():
    """Test cases for longest palindromic substring implementation"""
    test_cases = [
        # Basic cases
        ("babad", "bab"),      # "aba" is also a valid answer
        ("cbbd", "bb"),
        
        # Edge cases
        ("", ""),              # Empty string
        ("a", "a"),            # Single character
        ("aa", "aa"),          # Two same characters
        
        # Special cases
        ("racecar", "racecar"),  # Full string is palindrome
        ("abcde", "a"),          # No palindrome longer than 1
        ("aacabdkacaa", "aca"),  # Multiple palindromes
        ("bb", "bb"),            # Two same characters
        ("ccc", "ccc"),          # Three same characters
    ]
    
    for input_str, expected in test_cases:
        result = longest_palindrome(input_str)
        assert result == expected, f"Test failed for input '{input_str}'. Expected '{expected}', got '{result}'"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_longest_palindrome()
    
    # Example usage
    example_strings = [
        "babad",
        "cbbd",
        "racecar",
        "aacabdkacaa",
        "ccc",
    ]
    
    for s in example_strings:
        result = longest_palindrome(s)
        print(f"Input: s = '{s}'")
        print(f"Output: '{result}'")
        print(f"Explanation: The longest palindromic substring is '{result}'\n") 