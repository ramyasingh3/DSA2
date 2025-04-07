class Solution:
    def is_valid_stack(self, s: str) -> bool:
        """
        Stack-based solution with O(n) time complexity.
        Uses a stack to track opening brackets and matches them with closing brackets.
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
        String replacement solution with O(n^2) time complexity.
        Repeatedly removes valid pairs until the string is empty or no more pairs can be removed.
        """
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return not s

    def is_valid_count(self, s: str) -> bool:
        """
        Counting solution with O(n) time complexity.
        Tracks the count of each type of bracket and ensures they match.
        """
        count = {'(': 0, '{': 0, '[': 0}
        last_open = []
        
        for char in s:
            if char in count:
                count[char] += 1
                last_open.append(char)
            else:
                if not last_open:
                    return False
                last = last_open.pop()
                if (char == ')' and last != '(') or \
                   (char == '}' and last != '{') or \
                   (char == ']' and last != '['):
                    return False
                count[last] -= 1
                
        return all(v == 0 for v in count.values())

def test_solution():
    solution = Solution()
    
    # Test Case 1: Valid simple parentheses
    s1 = "()"
    print("Test Case 1:")
    print(f"Input: {s1}")
    print(f"Stack Solution: {solution.is_valid_stack(s1)}")
    print(f"Replace Solution: {solution.is_valid_replace(s1)}")
    print(f"Count Solution: {solution.is_valid_count(s1)}")
    print()
    
    # Test Case 2: Valid mixed parentheses
    s2 = "()[]{}"
    print("Test Case 2:")
    print(f"Input: {s2}")
    print(f"Stack Solution: {solution.is_valid_stack(s2)}")
    print(f"Replace Solution: {solution.is_valid_replace(s2)}")
    print(f"Count Solution: {solution.is_valid_count(s2)}")
    print()
    
    # Test Case 3: Invalid parentheses
    s3 = "(]"
    print("Test Case 3:")
    print(f"Input: {s3}")
    print(f"Stack Solution: {solution.is_valid_stack(s3)}")
    print(f"Replace Solution: {solution.is_valid_replace(s3)}")
    print(f"Count Solution: {solution.is_valid_count(s3)}")
    print()
    
    # Test Case 4: Nested valid parentheses
    s4 = "([{}])"
    print("Test Case 4:")
    print(f"Input: {s4}")
    print(f"Stack Solution: {solution.is_valid_stack(s4)}")
    print(f"Replace Solution: {solution.is_valid_replace(s4)}")
    print(f"Count Solution: {solution.is_valid_count(s4)}")
    print()
    
    # Test Case 5: Empty string
    s5 = ""
    print("Test Case 5:")
    print(f"Input: {s5}")
    print(f"Stack Solution: {solution.is_valid_stack(s5)}")
    print(f"Replace Solution: {solution.is_valid_replace(s5)}")
    print(f"Count Solution: {solution.is_valid_count(s5)}")

if __name__ == "__main__":
    test_solution() 