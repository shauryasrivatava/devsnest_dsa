# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # if head.next is None and n==1:
        #     return head.next
        p=head
        q=head
        c=0
        prev=head
        while q is not None:
            c+=1
            q=q.next
            if c>n:
                prev=p
                p=p.next
            if q is None:
                prev.next=p.next    
        if c==n:
            head=head.next
        return head  
