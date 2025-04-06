class Solution:
    def is_valid_stack(self, s: str) -> bool:
        """
        Stack-based solution with O(n) time complexity.
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack

    def is_valid_replace(self, s: str) -> bool:
        """
        String replacement solution with O(n²) time complexity.
        """
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return not s

def test_solution():
    solution = Solution()
    
    # Test Case 1: Valid parentheses
    s1 = "()"
    print("Test Case 1:")
    print(f"Input: {s1}")
    print(f"Stack Solution: {solution.is_valid_stack(s1)}")
    print(f"Replace Solution: {solution.is_valid_replace(s1)}")
    print()
    
    # Test Case 2: Valid nested parentheses
    s2 = "({[]})"
    print("Test Case 2:")
    print(f"Input: {s2}")
    print(f"Stack Solution: {solution.is_valid_stack(s2)}")
    print(f"Replace Solution: {solution.is_valid_replace(s2)}")
    print()
    
    # Test Case 3: Invalid parentheses
    s3 = "(]"
    print("Test Case 3:")
    print(f"Input: {s3}")
    print(f"Stack Solution: {solution.is_valid_stack(s3)}")
    print(f"Replace Solution: {solution.is_valid_replace(s3)}")
    print()
    
    # Test Case 4: Empty string
    s4 = ""
    print("Test Case 4:")
    print(f"Input: {s4}")
    print(f"Stack Solution: {solution.is_valid_stack(s4)}")
    print(f"Replace Solution: {solution.is_valid_replace(s4)}")
    print()
    
    # Test Case 5: Unmatched parentheses
    s5 = "([)]"
    print("Test Case 5:")
    print(f"Input: {s5}")
    print(f"Stack Solution: {solution.is_valid_stack(s5)}")
    print(f"Replace Solution: {solution.is_valid_replace(s5)}")

if __name__ == "__main__":
    test_solution() 