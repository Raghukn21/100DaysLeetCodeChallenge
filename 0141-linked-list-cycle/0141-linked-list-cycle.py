# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        # We check fast and fast.next because fast moves 2 steps at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, there's a loop!
            if slow == fast:
                return True
                
        # If we exit the loop, the fast pointer reached the end (no cycle)
        return False