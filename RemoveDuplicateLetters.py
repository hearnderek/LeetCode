from dataclasses import dataclass

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


class Solution:
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
        "abacb",
        "bcabc",
        "cbacdcbc",
        "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz",
        "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzaaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz"
        ]
    for x in xs:
        print(Solution().removeDuplicateLetters(x))
        print(Solution().new_removeDuplicateLetters(x))
        print(Solution().old_removeDuplicateLetters(x))
    
    
    print(removeDuplicateAdjecentLetters("rusrbofeggbbkyuyjsrzornpdguwzizqszpbicdquakqws"))
    print("bfegkuyjorndiqszpcaw")