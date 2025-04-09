from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_list_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative approach to reverse a linked list
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        current = head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        return prev
        
    def reverse_list_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive approach to reverse a linked list
        Time Complexity: O(n)
        Space Complexity: O(n) due to recursion stack
        """
        if not head or not head.next:
            return head
            
        new_head = self.reverse_list_recursive(head.next)
        head.next.next = head
        head.next = None
        
        return new_head
        
    def reverse_list_stack(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Stack-based approach to reverse a linked list
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not head:
            return None
            
        stack = []
        current = head
        
        while current:
            stack.append(current)
            current = current.next
            
        new_head = stack.pop()
        current = new_head
        
        while stack:
            current.next = stack.pop()
            current = current.next
            
        current.next = None
        return new_head

def create_linked_list(values: list) -> Optional[ListNode]:
    """Helper function to create a linked list from a list of values"""
    if not values:
        return None
        
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
        
    return head

def linked_list_to_list(head: Optional[ListNode]) -> list:
    """Helper function to convert a linked list to a list"""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
        
    return result

def test_solution():
    solution = Solution()
    
    # Test Case 1: Empty list
    print("Test Case 1: Empty list")
    head = create_linked_list([])
    result = solution.reverse_list_iterative(head)
    print(f"Result: {linked_list_to_list(result)}")
    print()
    
    # Test Case 2: Single node
    print("Test Case 2: Single node")
    head = create_linked_list([1])
    result = solution.reverse_list_iterative(head)
    print(f"Result: {linked_list_to_list(result)}")
    print()
    
    # Test Case 3: Multiple nodes
    print("Test Case 3: Multiple nodes")
    head = create_linked_list([1, 2, 3, 4, 5])
    result = solution.reverse_list_iterative(head)
    print(f"Result: {linked_list_to_list(result)}")
    print()
    
    # Test Case 4: Even number of nodes
    print("Test Case 4: Even number of nodes")
    head = create_linked_list([1, 2, 3, 4])
    result = solution.reverse_list_iterative(head)
    print(f"Result: {linked_list_to_list(result)}")
    print()
    
    # Test Case 5: Large list
    print("Test Case 5: Large list")
    head = create_linked_list(list(range(1, 11)))
    result = solution.reverse_list_iterative(head)
    print(f"Result: {linked_list_to_list(result)}")
    print()
    
    # Test all methods
    print("Testing all methods:")
    head = create_linked_list([1, 2, 3, 4, 5])
    
    print("Iterative:")
    result = solution.reverse_list_iterative(head)
    print(f"Result: {linked_list_to_list(result)}")
    
    print("Recursive:")
    head = create_linked_list([1, 2, 3, 4, 5])
    result = solution.reverse_list_recursive(head)
    print(f"Result: {linked_list_to_list(result)}")
    
    print("Stack-based:")
    head = create_linked_list([1, 2, 3, 4, 5])
    result = solution.reverse_list_stack(head)
    print(f"Result: {linked_list_to_list(result)}")

if __name__ == "__main__":
    test_solution() 