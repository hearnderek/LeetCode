# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def Build(x: int) -> 'ListNode':
        """ 
        506 -> [6,0,5] -> Head ListNode of value 6

        Gotta build the test inputs somewhere 
        """
        assert(x >= 0)
        
        # chosing the slow and easy way 
        # int -> str -> chr[] -> int[] -> ListNode[] -> return head ListNode
        # Note: 1's place first
        digits = list(reversed([int(c) for c in str(x)]))
        head = ListNode(val=digits[0])
        cur = head
        for d in digits[1:]:
            cur.next = ListNode(val=d)
            cur = cur.next

        return head
        
    def ToInt(self):
        """ 
        Just more helper functions to aid testing 
        """
        
        total = 0
        digit_multiplier = 1
        cur = self
        while(cur is not None):
            total += cur.val * digit_multiplier
            cur = cur.next
            digit_multiplier *= 10

        return total

    def ToList(self):
        xs = list()
        cur = self
        while(cur is not None):
            xs.append(cur.val)
            cur = cur.next
        return xs

    def ToString(self):
        """ The dead giveaway that I have a C# background """
        return str(self.ToList())

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r"""
        You are given two non-empty linked lists representing two non-negative integers. 
        The digits are stored in reverse order, and each of their nodes contains a single digit. 
        Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        """

        ## Thoughts:
        # The algorithm is split into 4 sections ##
        # Head, Zip, Tail, Final carry
        # This approach uses more LoC, tmp variables, and has code duplication, 
        # but with reduced branching I personally find this way more readable.
        # Each section can be examined in isolation, thus reducing mental load.

        # I don't like to work with the variable names l1 and l2
        x: ListNode = l1
        y: ListNode = l2

        ## Handle Head
        vsum = x.val + y.val
        carry = 0
        if vsum > 9:
            vsum -= 10
            carry = 1
        new_head_node = ListNode(val=vsum)
        x= x.next
        y= y.next

        ## handle zippable part of list
        cur = new_head_node
        while(x is not None and y is not None):
            vsum = x.val + y.val + carry
            
            carry = 0
            if vsum > 9:
                vsum -= 10
                carry = 1
            cur.next = ListNode(val=vsum)
            
            cur = cur.next
            x = x.next
            y = y.next

        ## handle tail where lists are of unequal size
        z: ListNode = x or y
        while(z is not None):
            vsum = z.val + carry
            
            carry = 0
            if vsum > 9:
                vsum -= 10
                carry = 1
            cur.next = ListNode(val=vsum)
            
            cur = cur.next
            z = z.next

        ## handle a hanging carry
        if carry > 0:
            cur.next = ListNode(val=carry)
        
        
        return new_head_node


def test(x: int, y: int):
    s = Solution()

    xs = ListNode.Build(x)
    print("xs:" ,xs.ToString())
    Passert(x, xs.ToInt())


    ys = ListNode.Build(y)
    print("ys:" ,ys.ToString())
    Passert(y, ys.ToInt())

    
    result = s.addTwoNumbers(xs, ys)
    print("zs: ", result.ToString())
    Passert(result.ToInt(), x + y)

def Passert(x, y):
    if x != y:
        print(f"{x} != {y}")

test(5, 5)
test(10, 11)
test(105, 5611)
test(105, 0)
test(0, 0)
test(4294967295, 4294967295)
