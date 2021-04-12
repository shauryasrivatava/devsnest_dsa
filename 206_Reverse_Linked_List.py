# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # head1=ListNode()
        if head is None or head.next is None:
            return head
        prev=head
        current=head.next
        nxt=head.next.next
        prev.next=None
        while nxt is not None:
            current.next=prev
            prev=current
            current=nxt
            nxt=nxt.next
        current.next=prev
        return current
