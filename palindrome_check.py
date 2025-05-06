def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# Example usage
if __name__ == "__main__":
    test_cases = ["racecar", "hello", "madam", "12321", "python"]
    for word in test_cases:
        print(f"{word}: {is_palindrome(word)}")
