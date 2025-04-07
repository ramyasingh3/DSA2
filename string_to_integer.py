class Solution:
    def my_atoi_naive(self, s: str) -> int:
        """
        Naive solution with O(n) time complexity.
        """
        s = s.strip()
        if not s:
            return 0
            
        sign = 1
        if s[0] in ['+', '-']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
            
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
            
        result *= sign
        return max(-2**31, min(2**31 - 1, result))

    def my_atoi_optimized(self, s: str) -> int:
        """
        Optimized solution with O(n) time complexity.
        """
        s = s.strip()
        if not s:
            return 0
            
        sign = 1
        if s[0] in ['+', '-']:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
            
        result = 0
        for char in s:
            if not char.isdigit():
                break
            digit = int(char)
            # Check for overflow before multiplying
            if result > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            result = result * 10 + digit
            
        return sign * result

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic conversion
    s1 = "42"
    print("Test Case 1:")
    print(f"Input: '{s1}'")
    print(f"Naive Solution: {solution.my_atoi_naive(s1)}")
    print(f"Optimized Solution: {solution.my_atoi_optimized(s1)}")
    print()
    
    # Test Case 2: Negative number
    s2 = "   -42"
    print("Test Case 2:")
    print(f"Input: '{s2}'")
    print(f"Naive Solution: {solution.my_atoi_naive(s2)}")
    print(f"Optimized Solution: {solution.my_atoi_optimized(s2)}")
    print()
    
    # Test Case 3: With words
    s3 = "4193 with words"
    print("Test Case 3:")
    print(f"Input: '{s3}'")
    print(f"Naive Solution: {solution.my_atoi_naive(s3)}")
    print(f"Optimized Solution: {solution.my_atoi_optimized(s3)}")
    print()
    
    # Test Case 4: Overflow case
    s4 = "91283472332"
    print("Test Case 4:")
    print(f"Input: '{s4}'")
    print(f"Naive Solution: {solution.my_atoi_naive(s4)}")
    print(f"Optimized Solution: {solution.my_atoi_optimized(s4)}")
    print()
    
    # Test Case 5: Empty string
    s5 = ""
    print("Test Case 5:")
    print(f"Input: '{s5}'")
    print(f"Naive Solution: {solution.my_atoi_naive(s5)}")
    print(f"Optimized Solution: {solution.my_atoi_optimized(s5)}")

if __name__ == "__main__":
    test_solution() 