class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse the second half of the list
        # 'slow' is at the middle; the second half starts at slow.next
        curr = slow.next
        slow.next = None # Sever the connection between halves
        prev = None
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # 3. Merge the two halves
        # first half starts at head, second half (reversed) starts at prev
        first, second = head, prev
        while second:
            # Temporary storage to keep track of the rest of the lists
            tmp1, tmp2 = first.next, second.next
            
            # Re-link nodes
            first.next = second
            second.next = tmp1
            
            # Move pointers forward
            first = tmp1
            second = tmp2