from collections import defaultdict

def min_window(s, t):
    """
    Find the minimum window in s which will contain all the characters in t.
    
    Args:
        s (str): The string to search in
        t (str): The string containing characters to find
        
    Returns:
        str: The minimum window substring, or empty string if not found
    """
    if not s or not t or len(s) < len(t):
        return ""
        
    # Create frequency maps
    target_counts = defaultdict(int)
    window_counts = defaultdict(int)
    
    # Initialize target counts
    for char in t:
        target_counts[char] += 1
        
    # Variables for sliding window
    left = 0
    min_len = float('inf')
    min_left = 0
    required = len(target_counts)
    formed = 0
    
    # Expand the window
    for right in range(len(s)):
        char = s[right]
        window_counts[char] += 1
        
        # Check if current character satisfies the requirement
        if char in target_counts and window_counts[char] == target_counts[char]:
            formed += 1
            
        # Contract the window
        while left <= right and formed == required:
            # Update minimum window
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left
                
            # Move left pointer
            left_char = s[left]
            window_counts[left_char] -= 1
            if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                formed -= 1
            left += 1
    
    return s[min_left:min_left + min_len] if min_len != float('inf') else ""

# Test cases
def test_min_window():
    # Example 1
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    assert min_window(s1, t1) == "BANC"
    
    # Example 2
    s2 = "a"
    t2 = "a"
    assert min_window(s2, t2) == "a"
    
    # Example 3
    s3 = "a"
    t3 = "aa"
    assert min_window(s3, t3) == ""
    
    # Additional test cases
    s4 = "aab"
    t4 = "aab"
    assert min_window(s4, t4) == "aab"
    
    s5 = "aa"
    t5 = "aa"
    assert min_window(s5, t5) == "aa"
    
    s6 = "abc"
    t6 = "ac"
    assert min_window(s6, t6) == "abc"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_min_window() 