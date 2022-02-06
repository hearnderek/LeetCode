from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        last = None
        beforeLast = None

        for i in range(len(nums)-1, -1, -1):
            n = nums[i]
            if n == beforeLast:
                del nums[i]
                continue
            length += 1
            beforeLast = last
            last = n

        return length


l = list([1,2,3,4,4,5,5,5,5,5,6,7,7,8])
print(l)
length = Solution().removeDuplicates(l)
print(length, l)