from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Assumption that list 1 and 2 are always sorted.

        # edge cases where we can quickly exit
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        # we now know both lists are not empty

        # personally I don't like it when the initial parameter references are lost.
        # For that reason I'm using temporary variables.
        a = list1
        b = list2

        # first iteration
        if a.val < b.val:
            head = a
            a = a.next
        else:
            head = b
            b = b.next
        
        # will be our final return
        top = head

        # second iteration
        while(a is not None and b is not None):
            if a.val < b.val:
                head.next = a
                a = a.next
            else:
                head.next = b
                b = b.next
            head = head.next
            

        # handling the remaining non-null path
        c = a if a is not None else b
        while c is not None:
            head.next = c
            head = head.next
            c = c.next

        # since this is a singly-listed list you want to return the first node
        return top






        

if __main__ == '__main__':
    s = Solution()
    print(s.mergeTwoLists(None, None))