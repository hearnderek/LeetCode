class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Github copilot solution
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # My solution
        # Use a dictionary to store the values and their indices
        # O(n) time and O(n) space
        d = dict()
        i = 0
        for n in nums:
            if n not in d:
                d[n] = list()
            d[n].append(i)
            i += 1
            
            tMatch = target - n
            if tMatch in d:
                if n == tMatch:
                    if len(d[n]) > 1:
                        return [d[n][0], d[n][1]]
                else:
                    return [d[tMatch][0], d[n][0]]