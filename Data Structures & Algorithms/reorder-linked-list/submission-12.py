# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        duzina = 0
        current = head

        while current:
            duzina += 1
            current = current.next

        current = head

        while current and current.next:

            if current.next.next is None:
                break

            temp = current

            while temp.next and temp.next.next:
                temp = temp.next
                if temp.next is None:
                    break

            node = current.next

            current.next = temp.next
            current.next.next = node
            temp.next = None

            try:
                current = current.next.next
            except:
                break
            

        


        