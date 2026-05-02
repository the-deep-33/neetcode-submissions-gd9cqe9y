import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lista = list()
        heapq.heapify(lista)

        for i in range(len(lists)):
            if lists[i] is None:
                continue
            tup = (lists[i].val, i, lists[i])
            heapq.heappush(lista, tup)

        new_list = ListNode()
        copy = new_list

        while lista:
            tup = heapq.heappop(lista)
            new_element = tup[2]
            copy.next = new_element
            copy = copy.next
            if new_element.next:
                new_tup = (new_element.next.val, i := i+1, new_element.next)
                heapq.heappush(lista, new_tup)
        
        if new_list.next:
            return new_list.next
        else:
            return None
        