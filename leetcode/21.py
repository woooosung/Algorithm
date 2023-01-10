# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        result = root
        while list1 and list2:
            val = 0
            if list1.val>list2.val:
                val = list2.val
                list2 = list2.next
            else:
                val = list1.val
                list1 = list1.next
            result.next = ListNode(val)
            result = result.next
        if list1 or list2: 
            result.next = list1 if list1 else list2
        return root.next