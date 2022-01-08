from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        p = -1
        head = strs[0]
        tail = strs[1:]

        for c in head:
            p += 1
            if any([1 for s in tail if s[p:p+1] != c]):
                p -= 1
                break

        if p == -1:
            return ""
        else:
            return strs[0][:p+1]

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["flight","flight","flight"]))