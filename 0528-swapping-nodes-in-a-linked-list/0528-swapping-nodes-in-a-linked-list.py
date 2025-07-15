# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next
        first=head
        for _ in range(k-1):
            first=first.next
        second=head
        for _ in range(length-k):
            second=second.next
        first.val,second.val=second.val,first.val
        return head