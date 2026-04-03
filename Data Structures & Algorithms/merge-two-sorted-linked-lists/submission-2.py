# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        current1 = list1
        current2 = list2

        while current1 is not None and current2 is not None:
            if current1.val < current2.val:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next
            current = current.next

        if current1 is not None:
            current.next = current1
            current = current.next
            current1 = current1.next

        if current2 is not None:
            current.next = current2
            current = current.next
            current2 = current2.next

        return dummy.next

        