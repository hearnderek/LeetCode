from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        xmax = nums[0]
        numset = set()
        for x in nums:
            if x < 1:
                continue
            if x > xmax:
                xmax = x
            numset.add(x)

        if xmax <= 0:
            xmax = 0

        for i in range(1, xmax):
            if i not in numset:
                return i
        
        return xmax+1