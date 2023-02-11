# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def set_index(self, probe):
        if probe == None:
            return 0
        else:
            probe.index = self.set_index(probe.next) + 1
            return probe.index
    
    def helper(self, probe, n):
        if probe.index == n:
            return probe.next
        else:
            probe.next = self.helper(probe.next, n)
            return probe
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.set_index(head)
        if head.index == n:
            return head.next
        else:
            head.next = self.helper(head.next, n)
            return head
