class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_two_lists_iterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Iterative solution with O(n+m) time complexity.
        Uses a dummy node to build the merged list.
        """
        dummy = ListNode()
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        current.next = l1 if l1 else l2
        return dummy.next

    def merge_two_lists_recursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Recursive solution with O(n+m) time complexity.
        More elegant but uses O(n+m) stack space.
        """
        if not l1:
            return l2
        if not l2:
            return l1
            
        if l1.val < l2.val:
            l1.next = self.merge_two_lists_recursive(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_lists_recursive(l1, l2.next)
            return l2

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
    
    # Test Case 1: Both lists have elements
    l1 = create_list([1, 2, 4])
    l2 = create_list([1, 3, 4])
    print("Test Case 1:")
    print(f"List 1: {list_to_string(l1)}")
    print(f"List 2: {list_to_string(l2)}")
    merged = solution.merge_two_lists_iterative(l1, l2)
    print(f"Merged (Iterative): {list_to_string(merged)}")
    merged = solution.merge_two_lists_recursive(l1, l2)
    print(f"Merged (Recursive): {list_to_string(merged)}")
    print()
    
    # Test Case 2: One list is empty
    l1 = create_list([])
    l2 = create_list([0])
    print("Test Case 2:")
    print(f"List 1: {list_to_string(l1)}")
    print(f"List 2: {list_to_string(l2)}")
    merged = solution.merge_two_lists_iterative(l1, l2)
    print(f"Merged (Iterative): {list_to_string(merged)}")
    merged = solution.merge_two_lists_recursive(l1, l2)
    print(f"Merged (Recursive): {list_to_string(merged)}")
    print()
    
    # Test Case 3: Both lists are empty
    l1 = create_list([])
    l2 = create_list([])
    print("Test Case 3:")
    print(f"List 1: {list_to_string(l1)}")
    print(f"List 2: {list_to_string(l2)}")
    merged = solution.merge_two_lists_iterative(l1, l2)
    print(f"Merged (Iterative): {list_to_string(merged)}")
    merged = solution.merge_two_lists_recursive(l1, l2)
    print(f"Merged (Recursive): {list_to_string(merged)}")
    print()
    
    # Test Case 4: Lists with different lengths
    l1 = create_list([1, 2, 3, 4, 5])
    l2 = create_list([6, 7])
    print("Test Case 4:")
    print(f"List 1: {list_to_string(l1)}")
    print(f"List 2: {list_to_string(l2)}")
    merged = solution.merge_two_lists_iterative(l1, l2)
    print(f"Merged (Iterative): {list_to_string(merged)}")
    merged = solution.merge_two_lists_recursive(l1, l2)
    print(f"Merged (Recursive): {list_to_string(merged)}")
    print()
    
    # Test Case 5: Lists with duplicate values
    l1 = create_list([1, 1, 2, 2])
    l2 = create_list([1, 1, 2, 2])
    print("Test Case 5:")
    print(f"List 1: {list_to_string(l1)}")
    print(f"List 2: {list_to_string(l2)}")
    merged = solution.merge_two_lists_iterative(l1, l2)
    print(f"Merged (Iterative): {list_to_string(merged)}")
    merged = solution.merge_two_lists_recursive(l1, l2)
    print(f"Merged (Recursive): {list_to_string(merged)}")

if __name__ == "__main__":
    test_solution() 