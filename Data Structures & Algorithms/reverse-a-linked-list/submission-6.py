# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        brojac = 0

        i = head
        da = True

        while i is not None:
            brojac += 1
            i = i.next

        i = head
        brojac1 = brojac

        for j in range(brojac // 2):

            cvor = i

            for r in range(brojac1 - j - 1):
                cvor = cvor.next

            temp = cvor.val
            cvor.val = i.val
            i.val = temp

            brojac1 -= 1
            i = i.next

        
        return head
        