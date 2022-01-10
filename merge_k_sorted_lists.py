# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # k = number of lists
        # n = total number of elements

        # 1 intuitive answer:
        # sort with a single pass
        # return min of all current enumerators
        # lot of repeated wasteful compares
        # Worst case of O(nk)
        #   Where all lists are of equal length

        # 2 optimizing 1:
        # sort heads by val
        # O(n log(k))
        #
        # while len(heads) > 1:
        #   cur.next = first
        #   heads[0] = first.next
        #   if first > second
        #     toInsert = heads.pop(0)
        #     inplace_binary_insertion(heads, toInsert)

        # 3 Divide and conquer?
        # merge lists two at a time


        fake_head = ListNode()
        current = fake_head
        
        # Seriously... we have to handle null head nodes?
        heads = [n for n in lists if n]
        
        while any(heads):
            min_i = 0
            min_n = heads[0]
            for i, n in enumerate(heads):
                if n.val < min_n.val:
                    min_i = i
                    min_n = n

            # modifying the nodes, not working on copies
            current.next = min_n
            current = min_n

            if min_n.next != None:
                heads[min_i] = min_n.next
            else:
                heads.pop(min_i)
        
        return fake_head.next
