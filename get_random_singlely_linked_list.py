import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __int__(self, head):
        self.head = head
        self.center = head # todo walk list
        self.len = -1 # todo walk list

    def getRandom(self) -> int:
        # Nieve solution Head Only:
        # Worst Case is taking tail: n
        # Best case is taking head: 1
        # Average case: n/2

        # Nieve solution Head & Center: 
        # Worst Case is taking center-1 or tail: n/2
        # Best case is taking head or center: 1
        # Average case: n/4

        # Memory intensive nieve solution:
        # store the values in an array

        # Solving the problem in a vacuum solution:
        # store the values in an array and don't forget the linked list

        # Non-memory intensive solution: (similar to a clustered index)
        # Create a partition index list with a buffer
        # n(1) lookup with a worst case of O(buffer)
        pass