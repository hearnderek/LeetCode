

class Solution:
    def new_removeDuplicateLetters(self, s: str) -> str:
        xs = set(s)
        for c in sorted(xs):
            rs = "".join(reversed(s))
            i = s.find(c)
            j = (rs.find(c) + 1) * -1
            print(i, s[i], j, s[j])
            s1 = s[:i+1] + "".join([x for x in s[i+1:] if x != c])
            s2 = "".join([x for x in s[:j] if x != c]) + s[j:]
            s = min( 
                s1,
                s2)
            print(s1)
            print(s2)
            print(c, s)

        return s
        
        pass


    def removeDuplicateLetters(self, s: str) -> str:
        """
        My initial solution was incorrect use to a misunderstanding of the problem.
        We are not able to reorder the characters, we can only remove characters.
        
        O(n) time complexity
        O(n) space complexity
        """

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
        # "abacb",
        # "abacb",
        # "bcabc",
        # "cbacdcbc",
        # "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz",
        # "aaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzaaaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzz"
        ]
    for x in xs:
        print(Solution().new_removeDuplicateLetters(x))