class Solution:
    def longest_palindrome_brute(self, s: str) -> str:
        """
        Brute force solution
        Time Complexity: O(n³)
        Space Complexity: O(1)
        """
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]
        
        n = len(s)
        if n < 2:
            return s
            
        max_len = 1
        result = s[0]
        
        for i in range(n):
            for j in range(i + 1, n):
                if j - i + 1 > max_len and is_palindrome(s[i:j+1]):
                    max_len = j - i + 1
                    result = s[i:j+1]
                    
        return result

    def longest_palindrome_dp(self, s: str) -> str:
        """
        Dynamic Programming solution
        Time Complexity: O(n²)
        Space Complexity: O(n²)
        """
        n = len(s)
        if n < 2:
            return s
            
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        start = 0
        
        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
            
        # Check for substrings of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                max_len = 2
                start = i
                
        # Check for substrings of length > 2
        for length in range(3, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > max_len:
                        max_len = length
                        start = i
                        
        return s[start:start+max_len]

    def longest_palindrome_expand(self, s: str) -> str:
        """
        Expand around center solution
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        if not s:
            return ""
            
        result = ""
        for i in range(len(s)):
            # Odd length palindrome
            odd = expand_around_center(i, i)
            if len(odd) > len(result):
                result = odd
                
            # Even length palindrome
            even = expand_around_center(i, i+1)
            if len(even) > len(result):
                result = even
                
        return result

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case
    print("Test Case 1: Basic case")
    s = "babad"
    result = solution.longest_palindrome_brute(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 2: Single character
    print("Test Case 2: Single character")
    s = "a"
    result = solution.longest_palindrome_brute(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 3: All same characters
    print("Test Case 3: All same characters")
    s = "aaaa"
    result = solution.longest_palindrome_brute(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 4: No palindrome
    print("Test Case 4: No palindrome")
    s = "abc"
    result = solution.longest_palindrome_brute(s)
    print(f"Input: {s}")
    print(f"Output: {result}")
    print()
    
    # Test Case 5: Long string
    print("Test Case 5: Long string")
    s = "a" * 1000
    result = solution.longest_palindrome_brute(s)
    print(f"Input: {s[:10]}...")
    print(f"Output: {result[:10]}...")
    print()
    
    # Test all methods
    print("Testing all methods:")
    s = "babad"
    print(f"Input: {s}")
    print(f"Brute force: {solution.longest_palindrome_brute(s)}")
    print(f"Dynamic Programming: {solution.longest_palindrome_dp(s)}")
    print(f"Expand around center: {solution.longest_palindrome_expand(s)}")

if __name__ == "__main__":
    test_solution() 