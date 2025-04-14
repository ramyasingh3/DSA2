def length_of_longest_substring(s):
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s (str): Input string
        
    Returns:
        int: Length of the longest substring without repeating characters
    """
    if not s:
        return 0
        
    # Initialize variables
    char_set = set()
    left = 0
    max_length = 0
    
    # Expand the window
    for right in range(len(s)):
        # If the current character is in the set, move the left pointer
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
            
        # Add the current character to the set
        char_set.add(s[right])
        
        # Update the maximum length
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test cases
def test_length_of_longest_substring():
    # Example 1
    s1 = "abcabcbb"
    assert length_of_longest_substring(s1) == 3
    
    # Example 2
    s2 = "bbbbb"
    assert length_of_longest_substring(s2) == 1
    
    # Example 3
    s3 = "pwwkew"
    assert length_of_longest_substring(s3) == 3
    
    # Additional test cases
    s4 = ""
    assert length_of_longest_substring(s4) == 0
    
    s5 = " "
    assert length_of_longest_substring(s5) == 1
    
    s6 = "dvdf"
    assert length_of_longest_substring(s6) == 3
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_length_of_longest_substring() 