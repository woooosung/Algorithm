# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        result = root
        up = 0
        while l1 or l2 or up:
            if l1:
                up += l1.val
                l1 = l1.next
            if l2:
                up += l2.val
                l2 = l2.next
            result.next = ListNode(up%10)
            result = result.next
            up = up//10
        return root.next   