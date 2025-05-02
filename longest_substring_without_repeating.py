def length_of_longest_substring(s):
    """
    Find the length of the longest substring without repeating characters.
    Time Complexity: O(n)
    Space Complexity: O(min(m, n)) where m is the size of the character set
    """
    if not s:
        return 0
    
    # Dictionary to store the last position of each character
    char_positions = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If we find a repeating character, update the start position
        if char in char_positions and char_positions[char] >= start:
            start = char_positions[char] + 1
        else:
            # Update max_length if current window is longer
            max_length = max(max_length, end - start + 1)
        
        # Update the last position of current character
        char_positions[char] = end
    
    return max_length

def main():
    # Test cases
    test_cases = [
        "abcabcbb",     # Expected: 3 ("abc")
        "bbbbb",        # Expected: 1 ("b")
        "pwwkew",       # Expected: 3 ("wke")
        "",            # Expected: 0
        " ",           # Expected: 1
        "dvdf",        # Expected: 3 ("vdf")
        "abba",        # Expected: 2 ("ab" or "ba")
        "tmmzuxt",     # Expected: 5 ("mzuxt")
    ]
    
    for s in test_cases:
        result = length_of_longest_substring(s)
        print(f"Input: s = '{s}'")
        print(f"Output: {result}")
        print(f"Explanation: The longest substring without repeating characters has length {result}\n")

if __name__ == "__main__":
    main() 