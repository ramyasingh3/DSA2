"""
Valid Anagram

Problem:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Time Complexity: O(n) where n is the length of the strings
Space Complexity: O(1) since we're using a fixed-size array for character counts
"""

def is_anagram(s: str, t: str) -> bool:
    # If lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False
    
    # Create a character count array (assuming ASCII characters)
    char_count = [0] * 26
    
    # Count characters in first string
    for char in s:
        char_count[ord(char) - ord('a')] += 1
    
    # Decrement counts for second string
    for char in t:
        char_count[ord(char) - ord('a')] -= 1
        # If count becomes negative, it means t has more of this character
        if char_count[ord(char) - ord('a')] < 0:
            return False
    
    return True

# Test cases
def test_valid_anagram():
    # Test case 1: Valid anagram
    assert is_anagram("anagram", "nagaram") == True
    
    # Test case 2: Invalid anagram
    assert is_anagram("rat", "car") == False
    
    # Test case 3: Empty strings
    assert is_anagram("", "") == True
    
    # Test case 4: Single character
    assert is_anagram("a", "a") == True
    
    # Test case 5: Different lengths
    assert is_anagram("hello", "world") == False
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_valid_anagram() 