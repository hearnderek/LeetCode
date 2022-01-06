class Solution:
    def longestPalindrome(self, s: str) -> str:
        # option1:
        # Breadth Search that simultaniously expands from every char until a palendrome cannot be found from it.
        # sort first is resturned
        # worst case "aaaaaaaa" of O(n^2) which appears to be good enough


        # option2:
        # we can improve option 1 by exiting early when the current center has no potental for being the new max

        # option3:
        # move from inside out, so we look at the biggest cases first

        longestLR = (None, None)

        nop_char = "\x90"
        line = nop_char + nop_char.join(s) + nop_char
        line_len = len(line)
        line_len_m1 = line_len - 1
        line_center = line_len_m1 // 2
        max_len = 0


        ## test best case center first
        l = line_center
        r = line_center
        count = 1
        line_center
        while(l > 0 and line[l-1] == line[r+1]):
            l-=1
            r+=1
            count += 2
        max_len = count
        longestLR = (l,r)

        ## expand left
        for center in range(line_center - 1, -1, -1):
            if (center+1)*2 < max_len:
                break
            
            l = center
            r = center
            count = 1
            while(l > 0 and line[l-1] == line[r+1]):
                l-=1
                r+=1
                count += 2

            if count >= max_len:
                max_len = count
                longestLR = (l,r)

        ## expand right
        distance_from_edge = line_center
        for center in range(line_center + 1, line_len):
            if distance_from_edge*2 < max_len:
                break
            
            l = center
            r = center
            count = 1
            while(r < line_len_m1 and line[l-1] == line[r+1]):
                l-=1
                r+=1
                count += 2

            if count > max_len:
                max_len = count
                longestLR = (l,r)

            distance_from_edge -= 1

        return line[longestLR[0]:longestLR[1]+1].replace(nop_char,'')



import random

s =Solution()
for i in range(1000000):
    random_pal_containing_str ="".join( ["{0:b}".format(random.randint(-24000000,24000000)) for _ in range(100)])
    #print()
    # print(random_pal_containing_str)
    # print("v")
    print(s.longestPalindrome(random_pal_containing_str))

# s.longestPalindrome("a")
# s.longestPalindrome("abcdefg")
# s.longestPalindrome("abcdef")
# s.longestPalindrome("otto")
# s.longestPalindrome("abcdff")
# s.longestPalindrome("aacdefggg")

