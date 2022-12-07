# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper(self, l1, l2, extra):
        if l1 == None and l2 != None:
            ans = ListNode((l2.val + extra) % 10)
            ans.next = self.helper(None, l2.next, (l2.val + extra) // 10)
            return ans
        elif l1 != None and l2 == None:
            ans = ListNode((l1.val + extra) % 10)
            ans.next = self.helper(l1.next, None, (l1.val + extra) // 10)
            return ans
        elif l1 != None and l2 != None:
            ans = ListNode((l1.val + extra + l2.val) % 10)
            ans.next = self.helper(l1.next, l2.next, (l1.val + l2.val + extra) // 10)
            return ans
        else:
            if extra == 0:
                return None
            else:
                return ListNode(extra)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode((l1.val + l2.val) % 10)
        ans.next = self.helper(l1.next, l2.next, (l1.val + l2.val) // 10)
        return ans

