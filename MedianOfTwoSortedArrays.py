from typing import List
import random


def iof(xs, i, len_xs):
    if i < 0:
        return float("-inf")
    
    if i < len_xs:
        return xs[i]
    
    return float("inf")


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        xs, ys, len_xs, len_ys = nums1, nums2, len(nums1), len(nums2)
        len_tot = len_xs + len_ys
        half_tot = len_tot // 2

        
        ## handle single empty list case -- simple median O(1)
        if len_xs > len_ys:
            xs, ys, len_xs, len_ys = ys, xs, len_ys, len_xs
        if len_xs == 0:
            median_index = (len_tot - 1) // 2
            first_median = ys[median_index]
            if len_tot & 1: # odd
                return first_median
            else:
                second_median = ys[median_index + 1]
                return (first_median + second_median) / 2


        ## handle no-overlap -- treat as one list cases O(1)
        midpoint = (len_tot - 1) // 2
        no_overlap = False
        if xs[-1] <= ys[0]: # xs [0, 1] ys [2, 3]
            no_overlap = True
        elif ys[-1] <= xs[0]: # ys [0, 1] xs [2, 3]
            no_overlap = True
            xs, ys, len_xs, len_ys = ys, xs, len_ys, len_xs
        
        if no_overlap: # found answer!
            # assertion: xs[-1] <= ys[0]
            median_index = None
            if midpoint < len(xs):
                median_index = midpoint
            else:
                median_index = midpoint - len_xs
                xs, ys, len_xs, len_ys = ys, xs, len_ys, len_xs

            # assertion: xs contains midpoint
            first_median = xs[median_index]

            if len_tot & 1: # odd
                return first_median
            else:
                second_median = None
                if median_index + 1 == len_xs:
                    second_median = ys[0]
                else:
                    second_median = xs[median_index + 1]
                return (first_median + second_median) / 2


        ## Solve through Binary Search driven partition creation 
        # worst case O(Log(0m + n)) where n <= m
        if len_xs > len_ys:
            xs, ys, len_xs, len_ys = ys, xs, len_ys, len_xs 

        # assertion: len(xs) <= len(ys)
        # assertion: xs and ys overlap
        xl = 0 # inclusive start
        xr = len_xs # non-inclusive end
        while True:
            xp = (xr - xl) // 2 + xl # midpoint of bounded xs range
            yp = half_tot - xp # this requies len(ys) <= len(xs)

            # out of bounds indexs become infinities
            # -inf [...] inf
            if iof(xs, xp-1, len_xs) > iof(ys, yp, len_ys):
                xr = xp
            elif iof(ys, yp-1, len_ys) > iof(xs, xp, len_xs):
                xl = xp + 1
            # using slices & list concatatination to ignore out of bounds cases
            elif len_tot & 1: # odd
                return min(xs[xp:xp+1] + ys[yp:yp+1])
            else:             # even 
                return (max(xs[xp-1:xp] + ys[yp-1:yp]) + min(xs[xp:xp+1] + ys[yp:yp+1])) / 2
            

    def slow_findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        xs = sorted(nums1 + nums2)
        return median(xs)



def midpoint_indexs(xs):
    len_xs = len(xs)
    if len_xs == 1:
        return [0]

    mid = (len_xs - 1) // 2
    if len_xs & 1: # Odd
        return [mid]
    return [mid, mid+1]

def median(xs):
    median_ = 0
    midpoint_indexs_ = midpoint_indexs(xs)
    for i in midpoint_indexs_:
        median_ += xs[i]
    median_ /= len(midpoint_indexs_)
    return median_



def analyze(xs, ys):
    truth = s.slow_findMedianSortedArrays(list(xs), list(ys))
    result = s.findMedianSortedArrays(list(xs), list(ys))

    if truth != result:
        print("FAIL---")
        print("xs:", xs, '- len:',  len(xs))
        print("ys:", ys, '- len:',  len(ys))
        print("truth:", truth) 
        print("median:", result) 
        print()
    


s = Solution()
xs = range(1, 100, 6)
ys = range(1, 150, 7)
zs = range(50, 150, 4)

for (a, b) in [(xs, ys), (xs, zs), (ys, zs)]:
    analyze(a, b)
    print()


analyze([], [1,2,3])
analyze([], [2,3])
analyze([1,2,3], [])
# print()

def r(): 
    return random.randint(1, 100)

for _ in range(100000):
    ar = r()
    a = range(ar, ar + r(), random.randint(1, 5))
    
    br = r()
    b = range(br, br+r(), random.randint(1, 5))
    analyze(a, b)
    # print()
