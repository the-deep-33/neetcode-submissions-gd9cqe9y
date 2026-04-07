# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        duzina = 0

        while current:
            duzina += 1
            current = current.next

        if duzina == 1:
            head = None
            return head

        current = head

        for i in range(duzina - n - 1):
            current = current.next

        if current == head and n == duzina:
            head = head.next
        else:
            try:
                current.next = current.next.next
            except:
                current.next = None

        return head

            
        