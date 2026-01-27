# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while True:
            curr = prev
            for _ in range(k):
                curr = curr.next
                if not curr:
                    return dummy.next
            last = prev.next
            curr = last.next
            for _ in range(k - 1):
                last.next = curr.next
                curr.next = prev.next
                prev.next = curr
                curr = last.next
            prev = last