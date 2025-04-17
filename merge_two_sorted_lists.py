from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Merge two sorted linked lists into one sorted linked list.
    
    Args:
        list1: Head of the first sorted linked list
        list2: Head of the second sorted linked list
        
    Returns:
        Head of the merged sorted linked list
    """
    # Create a dummy node to start the merged list
    dummy = ListNode()
    current = dummy
    
    # Traverse both lists
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach the remaining elements
    current.next = list1 if list1 else list2
    
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

def test_merge_two_lists():
    """Test cases for the merge two sorted lists solution."""
    
    test_cases = [
        # Basic cases
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        # Edge cases
        ([1], [], [1]),
        ([], [1], [1]),
        # Single element cases
        ([1], [2], [1, 2]),
        ([2], [1], [1, 2]),
        # Different lengths
        ([1, 2, 3], [4, 5], [1, 2, 3, 4, 5]),
        ([4, 5], [1, 2, 3], [1, 2, 3, 4, 5]),
        # Negative numbers
        ([-1, 0, 1], [-2, 2], [-2, -1, 0, 1, 2]),
        # Duplicate numbers
        ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]),
        # Large numbers
        ([100, 200, 300], [150, 250, 350], [100, 150, 200, 250, 300, 350])
    ]
    
    print("Testing Merge Two Sorted Lists Solution...")
    for list1, list2, expected in test_cases:
        # Convert lists to linked lists
        l1 = list_to_linked_list(list1)
        l2 = list_to_linked_list(list2)
        
        # Merge the lists
        merged = merge_two_lists(l1, l2)
        
        # Convert back to list for comparison
        result = linked_list_to_list(merged)
        
        print(f"\nInput: list1 = {list1}, list2 = {list2}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_merge_two_lists() 