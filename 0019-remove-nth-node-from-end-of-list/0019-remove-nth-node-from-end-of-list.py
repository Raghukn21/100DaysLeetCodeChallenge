class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node points to head to handle edge cases (like removing the first node)
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        
        # Move fast forward n + 1 steps to create the gap
        for _ in range(n + 1):
            fast = fast.next
            
        # Move both until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next
            
        # slow is now at the (n+1)-th node from the end
        # Skip the nth node
        slow.next = slow.next.next
        
        return dummy.next