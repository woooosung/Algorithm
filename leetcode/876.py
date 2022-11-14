class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        length = 0
        while (temp):
            length += 1
            temp = temp.next
        length = int((length)/2)
        temp = head
        for i in range(length):
            temp = temp.next
        return temp