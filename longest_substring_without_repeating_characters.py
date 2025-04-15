class LongestSubstringWithoutRepeatingCharacters:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.
        
        Args:
            s: Input string
            
        Returns:
            int: Length of the longest substring without repeating characters
        """
        if not s:
            return 0
            
        char_set = set()
        left = 0
        max_length = 0
        
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

def test_longest_substring():
    # Test cases
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
        ("tmmzuxt", 5),
    ]
    
    solver = LongestSubstringWithoutRepeatingCharacters()
    
    for s, expected in test_cases:
        result = solver.lengthOfLongestSubstring(s)
        print(f"Input: s = '{s}'")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_longest_substring() 