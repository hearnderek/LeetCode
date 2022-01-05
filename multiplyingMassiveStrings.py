from typing import List


char_to_int_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

def char_to_int(c: chr) -> int:
    return char_to_int_dict[c]
    

def str_to_ints(s: str) -> List[int]:
    return [char_to_int(c) for c in s]

def add(xs: List[int], ys: List[int]) -> List[int]:
    # adds equal length lists together
    rs = []
    carry = 0
    for i in range(len(xs)-1, -1, -1):
        t = xs[i] + ys[i] + carry
        carry = t // 10
        rs.append(t - carry * 10)

    if carry > 0:
        rs.append(carry)

    rs.reverse()
    return rs

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        xs = str_to_ints(num1)
        ys = str_to_ints(num2)

        # basically I want this to be slow but able to calculate impossibly large numbers   

        # 1s place wil have 1 * 1 - carry
        # 2s place will have 2 * 1 + 1 * 2 + carry
        # 3s place will have 3 * 1 + 2 * 2 + 


        for i in range(len(xs)):
            pass
            
            

print(add([], []))
print(add([], [1]))
print(add([1,2,3], [4,5,6]))
print(add([9,2,3], [4,5,6]))