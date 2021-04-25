# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        setattr(ListNode,"__it__", lambda self, other: self.val<=other.val)
        heap=[]
        for elt in lists:
            if elt:
                heapq.heappush(heap ,elt)
        temp=ListNode(None)
        p=temp
        while len(heap)>0:
            n=heapq.heappop(heap)
            p.next=n
            p=n
            if n.next:
                heapq.heappush(heap,n.next)
        return temp.next
