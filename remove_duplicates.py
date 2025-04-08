class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def delete_duplicates_iterative(self, head: ListNode) -> ListNode:
        """
        Iterative solution with O(n) time complexity.
        Uses two pointers to track current and next nodes.
        """
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    def delete_duplicates_recursive(self, head: ListNode) -> ListNode:
        """
        Recursive solution with O(n) time complexity.
        More elegant but uses O(n) stack space.
        """
        if not head or not head.next:
            return head
            
        if head.val == head.next.val:
            return self.delete_duplicates_recursive(head.next)
        else:
            head.next = self.delete_duplicates_recursive(head.next)
            return head

def create_list(values):
    """Helper function to create a linked list from a list of values"""
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def list_to_string(head):
    """Helper function to convert linked list to string for printing"""
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    return "->".join(result)

def test_solution():
    solution = Solution()
    
    # Test Case 1: Basic case with duplicates
    head = create_list([1, 1, 2])
    print("Test Case 1:")
    print(f"Original: {list_to_string(head)}")
    result = solution.delete_duplicates_iterative(head)
    print(f"Iterative: {list_to_string(result)}")
    result = solution.delete_duplicates_recursive(head)
    print(f"Recursive: {list_to_string(result)}")
    print()
    
    # Test Case 2: Multiple duplicates
    head = create_list([1, 1, 2, 3, 3])
    print("Test Case 2:")
    print(f"Original: {list_to_string(head)}")
    result = solution.delete_duplicates_iterative(head)
    print(f"Iterative: {list_to_string(result)}")
    result = solution.delete_duplicates_recursive(head)
    print(f"Recursive: {list_to_string(result)}")
    print()
    
    # Test Case 3: No duplicates
    head = create_list([1, 2, 3, 4, 5])
    print("Test Case 3:")
    print(f"Original: {list_to_string(head)}")
    result = solution.delete_duplicates_iterative(head)
    print(f"Iterative: {list_to_string(result)}")
    result = solution.delete_duplicates_recursive(head)
    print(f"Recursive: {list_to_string(result)}")
    print()
    
    # Test Case 4: Empty list
    head = create_list([])
    print("Test Case 4:")
    print(f"Original: {list_to_string(head)}")
    result = solution.delete_duplicates_iterative(head)
    print(f"Iterative: {list_to_string(result)}")
    result = solution.delete_duplicates_recursive(head)
    print(f"Recursive: {list_to_string(result)}")
    print()
    
    # Test Case 5: All duplicates
    head = create_list([1, 1, 1, 1, 1])
    print("Test Case 5:")
    print(f"Original: {list_to_string(head)}")
    result = solution.delete_duplicates_iterative(head)
    print(f"Iterative: {list_to_string(result)}")
    result = solution.delete_duplicates_recursive(head)
    print(f"Recursive: {list_to_string(result)}")

if __name__ == "__main__":
    test_solution() 