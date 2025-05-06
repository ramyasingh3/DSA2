# DSA Another Question

# Problem Statement:
# Given a string, find the length of the longest substring without repeating characters.
# This problem is commonly known as the "Longest Substring Without Repeating Characters".

# Example:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Function to find the length of the longest substring without repeating characters
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

# Test the function
if __name__ == "__main__":
    test_string = "abcabcbb"
    print("Length of the longest substring without repeating characters is", length_of_longest_substring(test_string))
