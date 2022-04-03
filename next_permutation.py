from typing import Generator, List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies the list "nums" in-place.
        
        fist idea:
        create a sorted array of tuples
        each tuple is a representation of a single permutation
        
        getnext():
            perms[cur+1] # loop around?

        positives: it is easy to concepualize working with this model

        negatives: need to store every single permutation


        second idea:
        what can we know about our data?
        how can we build the sorted array from the first idea in order?

        list.sort()
        """
        snums = sorted(nums)
        g = skipping_gen_perms(snums, nums)
        
        next(g)
        ret = next(g, snums)
        for i in range(len(nums)):
            nums[i] = ret[i]
        
            


def gen_perms(nums) -> List[List[int]]: 
    if len(nums) == 1:
        yield nums
        return

    for i in range(len(nums)):
        cur = list(nums)
        x = int(cur[i])
        del cur[i]
        
        perms = gen_perms(cur)
        for ret in perms:
            ret.insert(0, x)
            yield ret

def skipping_gen_perms(nums, skipto) -> List[List[int]]: 
    if len(nums) == 1:
        yield nums
        return
    seek = True
    for i in range(len(nums)):
        if seek:
            if nums[i] != skipto[0]:
                continue
            
            cur = list(nums)
            x = int(cur[i])
            del cur[i]
            
            perms = skipping_gen_perms(cur, skipto[1:])
            for ret in perms:
                ret.insert(0, x)
                yield ret
            seek = False
        else:
            if nums[i] == nums[i-1]:
                continue
            cur = list(nums)
            x = int(cur[i])
            del cur[i]
            
            perms = gen_perms(cur)
            for ret in perms:
                ret.insert(0, x)
                yield ret

if __name__ == '__main__':
    print("hello")
    for xs in skipping_gen_perms([1,2,3], [2,1,3]):
        print(xs)

    t = [2,1,3]
    Solution().nextPermutation(t)
    print(t)
    print()

    t = [1,5,1]
    for xs in skipping_gen_perms(sorted(t), t):
        print(xs)

    print()


    Solution().nextPermutation(t)
    print(t)



    t = [6,7,5,3,5,6,2,9,1,2,7,0,9]
    Solution().nextPermutation(t)
    print(t)


