# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        values=set(nums)
        temp=ListNode(0,head)
        prev=temp
        while prev.next:
            if prev.next.val in values:
                prev.next=prev.next.next
            else:
                prev=prev.next
        return temp.next
        