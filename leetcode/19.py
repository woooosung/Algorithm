# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 0
        while (temp):
            length += 1
            temp = temp.next
    
        if (n==1):
            if (length==1):
                return None
            temp_1 = head
            for i in range(length-2):
                temp_1 = temp_1.next
            temp_1.next = None
            return head
        if (n==length):
            temp = head
            head = temp.next
            return head

        temp = head
        for j in range(length-n-1):
            temp = temp.next
        temp_2 = temp.next
        temp_2 = temp_2.next
        temp.next = temp_2
        return head