# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        i = 0
        current1 = l1
        suma1 = 0

        while current1:
            suma1 += pow(10, i) * current1.val
            i += 1
            current1 = current1.next

        i = 0
        current1 = l2
        suma2 = 0

        while current1:
            suma2 += pow(10, i) * current1.val
            i += 1
            current1 = current1.next

        suma = suma1 + suma2

        novi = ListNode(0)
        novi.next = ListNode(0)
        current = novi
        i -= 1

        print(suma)

        while suma > 0:
            cifra = suma % 10
            suma = suma // 10
            current.next = ListNode(cifra)
            current = current.next

        return novi.next


        
        

        