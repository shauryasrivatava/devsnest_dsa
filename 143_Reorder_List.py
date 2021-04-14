# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def cuthalf(head):
    slow=head
    fast=head.next
    if not fast:
        return None
    while fast.next and fast.next.next:
        fast=fast.next.next
        slow=slow.next
    if fast.next is not None:
        slow=slow.next
    p=slow.next
    slow.next=None
    return p

def reverse(head):
    if head and head.next is None:
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

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head.next is None:
            return head
        head1=cuthalf(head)
        head2=reverse(head1)
        head1=head
        k=head2
        while head1 and head2 is not None:
            temp2=head2.next
            head2.next=head1.next
            head1.next=head2
            head1=head1.next.next
            head2=temp2    
