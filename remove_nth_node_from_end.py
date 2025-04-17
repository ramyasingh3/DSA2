from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove the nth node from the end of the list and return its head.
    
    Args:
        head: Head of the linked list
        n: Position from the end to remove (1-based)
        
    Returns:
        Head of the modified linked list
    """
    # Create a dummy node to handle edge cases
    dummy = ListNode(0, head)
    fast = slow = dummy
    
    # Move fast pointer n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next
    
    # Move both pointers until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next
    
    # Remove the nth node
    slow.next = slow.next.next
    
    return dummy.next

def list_to_linked_list(lst: list) -> Optional[ListNode]:
    """Convert a list to a linked list."""
    if not lst:
        return None
    
    head = ListNode(lst[0])
    current = head
    
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head: Optional[ListNode]) -> list:
    """Convert a linked list to a list."""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

def test_remove_nth_from_end():
    """Test cases for the remove nth node from end solution."""
    
    test_cases = [
        # Basic cases
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
        # Edge cases
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        # Single element
        ([1], 1, []),
        # Multiple elements
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [1, 2, 3, 4, 5, 6, 8, 9]),
        # Remove last element
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
        # Remove first element
        ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
        # Large list
        (list(range(1, 101)), 50, list(range(1, 51)) + list(range(52, 101)))
    ]
    
    print("Testing Remove Nth Node From End Solution...")
    for lst, n, expected in test_cases:
        # Convert list to linked list
        head = list_to_linked_list(lst)
        
        # Remove nth node from end
        result_head = remove_nth_from_end(head, n)
        
        # Convert back to list for comparison
        result = linked_list_to_list(result_head)
        
        print(f"\nInput: list = {lst}, n = {n}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_remove_nth_from_end() 