from dataclasses import dataclass
from typing import Counter, List

@dataclass
class BestRemoval:
    s: str
    c: str
    i: int

def removeDuplicateAdjecentLetters(s: str) -> str:
    sb = s[:1]
    for i in range(1, len(s)):
        if s[i] != sb[-1]:
            sb += s[i]
    return sb


class StringWrapper:

    def __init__(self, s) -> None:
        self.s: str = removeDuplicateAdjecentLetters(s)
        self.simplified: str = StringWrapper.get_simplified(self.s)

    @staticmethod
    def get_simplified(s: str) -> str:
        ctr = Counter(s)
        simplified = ""
        for c in s:
            if ctr[c] > 1:
                simplified += c
        return simplified

    def removeSimplifiedCharByIndex(self, i) -> 'StringWrapper':
        p1 = 0
        p2 = 0
        while p2 < len(self.simplified):
            while self.s[p1] != self.simplified[p2]:
                p1 += 1
            
            if p1 == i:
                ns = StringWrapper(self.self.s[:p1] + self.s[p1 + 1:])
                
                # Removing newly found equal adjecent letters
                while len(self.s) > p1 and self.s[p1-1] == self.s[p1]:
                    self.s = self.s[:p1] + self.s[p1 + 1:]
                self.simplified = self.get_simplified(self.s)
                break

@dataclass        
class GroupNode:
    left: 'GroupNode'
    volatile: bool
    s: str
    right: 'GroupNode'

    def __init__(self, left: 'GroupNode', volatile: bool, s: str, right: 'GroupNode') -> None:
        # assert left.volatile != volatile and right.volatile != volatile
        self.left = left
        self.volatile = volatile
        self.s = s
        self.right = right

    @staticmethod
    def build_linked_list(s: str) -> 'GroupNode':
        # split into volitile and non-volitile groups
        # volatile groups are groups that contain volatile letter(s)
        # volatile letters are letters that can be removed
        # a letter can be removed if there is more than one of it in the starting string

        groups: List['GroupNode'] = []
        ctr = Counter(s)
        ss: List[str] = []
        volatile: bool = None
        cur_volatile: bool = None
        for c in s:
            cur_volatile = ctr[c] > 1
            if cur_volatile != volatile:
                
                if len(ss) > 0:
                    l_group = None
                    if any(groups):
                        l_group = groups[-1]
                    groups.append(GroupNode(l_group, volatile, ss[-1], None))
                    if l_group:
                            l_group.right = groups[-1]

                ss.append(c)
                volatile = cur_volatile
                
            else:
                ss[-1] += c

        if cur_volatile is not None:
            l_group = None
            if any(groups):
                l_group = groups[-1]
            groups.append(GroupNode(l_group, cur_volatile, ss[-1], None))
            if l_group:
                    l_group.right = groups[-1]

        for g in groups:
            print(g.s, g.volatile)

        

    def left_most(self) -> str:
        return self.s[0]
    
    def right_most(self) -> str:
        return self.s[-1]
    

class Solution:
    


    def removeDuplicateLettersSimplified(self, s: str) -> str:
        """ Failed Greedy 3"""
        s = StringWrapper(s)
        cfs = dict()
        i = 0
        for c in s.s:
            if c not in cfs:
                cfs[c] = 1
            else:
                cfs[c] += 1
            i += 1
        

        while any(x > 1 for x in cfs.values()):
            br = None
            for (i, c) in enumerate(s):
                if cfs[c] == 1:
                    continue
                sr = s[0:i] + s[i+1:]
                if not br or br.s > sr:
                    br = BestRemoval(sr, c, i)
            cfs[br.c] -= 1
            s = br.s
            print(s)
        return s

    def removeDuplicateLetters(self, s: str) -> str:
        """ Failed Greedy 3"""
        s = removeDuplicateAdjecentLetters(s)
        
        cfs = dict()
        i = 0
        for c in s:
            if c not in cfs:
                cfs[c] = 1
            else:
                cfs[c] += 1
            i += 1
        
        while any(x > 1 for x in cfs.values()):
            br = None
            for (i, c) in enumerate(s):
                if cfs[c] == 1:
                    continue
                sr = s[0:i] + s[i+1:]
                if not br or br.s > sr:
                    br = BestRemoval(sr, c, i)
            cfs[br.c] -= 1
            s = br.s
            print(s)
        return s

    def new_removeDuplicateLetters(self, s: str) -> str:
        """ Failed Greedy 2 """
        s = removeDuplicateAdjecentLetters(s)
        
        xs = set(s)
        for c in sorted(xs):
            rs = "".join(reversed(s))
            i = s.find(c)
            j = (rs.find(c) + 1) * -1
            s1 = s[:i+1] + "".join([x for x in s[i+1:] if x != c])
            s2 = "".join([x for x in s[:j] if x != c]) + s[j:]
            s = min( 
                s1,
                s2)
            print(c, s)

        return s
        
        pass


    def old_removeDuplicateLetters(self, s: str) -> str:
        """
        Failed Greedy 1
        """

        s = removeDuplicateAdjecentLetters(s)
        
        sbx = ""
        sby = ""
        sbz = ""

        len_s = len(s)
        for i in range(len_s):
            
            j = len_s - i - 1
            x = s[i]
            y = s[j]



            if x not in sbx:
                sbx = sbx + x
            else:
                sbx = min(sbx, sbx.replace(x, "") + x)

            if y not in sby:
                sby = y + sby
            else:
                sby = min(sby, y + sby.replace(y, ""))


            print(sbx + '.' + s[i+1:] + ' : ' + s[:j] + '.' + sby)
            
        return min(sbx, sby)

if __name__ == "__main__":
    xs = [
        "rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws",
        StringWrapper.get_simplified("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws"),
        # "abacb",
        # "bcabc",
        # "cbacdcbc",
        # "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz",
        # "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzaaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz"
        ]
    for x in xs:
        GroupNode.build_linked_list(x)
        #print(Solution().removeDuplicateLetters(x))
        #print(Solution().new_removeDuplicateLetters(x))
        #print(Solution().old_removeDuplicateLetters(x))
    
    #print(StringWrapper.get_simplified("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws"))
    # print(removeDuplicateAdjecentLetters("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws"))
    # print("bfegkuyjorndiqszpcaw")
