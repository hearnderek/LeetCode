from typing import List
from dataclasses import dataclass

@dataclass
class Traveler:
    ref: List[int]
    travel: int
    travel_within_cur_ref: int
    ref_limit: int

class DefinedSets:
    ls: List[int]
    count: int

    

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Easy way is to merge the two arrays 
        # and then find the one or two in case of len being even numbers to find the median
        #
        # the time complexity goal is O(log(m+n))
        # This means that even half merging the two arrays will take O((m+n)/2) time ∴ no go
        #
        # Thus we need to eliminate roughly 1 - log(...) % of the possible cases
        #   
        # We can use the min and max of the two arrays for this culling

        # Thinking;
        # what things can we discern?
        # xs[n] is at least n/(x+y) of the way through the array
        # ys[n] is at least (n+z)/(x/+y) of the way through the array
        #   where z is an unknown number of elements

        # xs[x_mid] < ys[y_mid] ∴ ys[y_mid] is element number x_mid + y_mid


        # [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ] 
        # [10,20,30,40,50,60,70,80,90,100]
        m = len(nums1)
        m_min = nums1[0]
        m_max = nums1[-1]

        n = len(nums2)
        n_min = nums2[0]
        n_max = nums2[-1]

        # don't forget int floor
        true_middle = int((m + n) / 2)

        # this orders the sets, so they are easier to reasion about in my head
        # x can then be considered the set with a smaller bounding box
        if m_min <= n_min and not(m_min == n_min and m_max > n_max):
            x = m
            y = n
            xs = nums1
            ys = nums2
        else:
            x = n
            y = m
            xs = nums2
            ys = nums1

        if xs[-1] < ys[0]:
            # no overlap just return the median
            if x > y:
                # todo handle even case
                return xs[true_middle]
            elif y > x:
                # todo handle even case
                return ys[-true_middle]
            else:
                return (x[-1] + y[0]) / 2
        
        # setting pointers at edges of full set
        
        start_travel = 0
        start_ptr = 0
        start_ref = xs
        start_travel_within_cur_ref = 0
        start_ref_limit = x

        end_ptr = y-1
        end_travel = 0
        end_ref = ys
        end_travel_within_cur_ref = 0
        end_ref_limit = y

        target_travel = int((x + y) / 2)

        # while(start_travel < target_travel):
        #     travel_step = int(target_travel / 2)
            
        #     if start_ref

        # if man % 2 == 1:
        #     return start_ref[start_travel]
        # else:
        #     print("end_ref_limit - end_travel_within_cur_ref =", end_ref_limit, end_travel_within_cur_ref)
        #     return start_ref[start_travel_within_cur_ref] + end_ref[end_ref_limit - end_travel_within_cur_ref]

        # return min_value + max_value / 2

        # set possibilities
        # 1. x_max < y_min -- no overlap
        # 2. x_min < y_min and x_max < y_max
        # 3. x_min < y_min and x_max > y_max

def merge_sorted(xs: List[int], ys: List[int]) -> List[int]:
    i = 0
    j = 0
    zs = []
    while(i < len(xs) and j < len(ys)):
        if xs[i] < ys[j]:
            zs.append(xs[i])
            i += 1
        else:
            zs.append(ys[j])
            j += 1
    while(i < len(xs)):
        zs.append(xs[i])
        i += 1
    while(j < len(ys)):
        zs.append(ys[j])
        j += 1
    return zs


def midpoint_test(xs: List[int], ys: List[int]):
    xys = merge_sorted(xs, ys)
    
    x_mid = int(len(xs)/2-1)
    y_mid = int(len(ys)/2-1)

    if (xs[x_mid] <= ys[y_mid]):

        # we now have 4 groups and a floor floor of what % of the values they represent
        # 1. xs[     :x_mid]
        # 2. xs[x_mid:     ]
        # 3. ys[     :y_mid]
        # 4. ys[y_mid:     ]

        print(xs[:x_mid+1], 'is no more than',  (x_mid+1) / len(xys) * 100, '%', 'of the total')
        #print(xs[:x_mid], 'is no more than',  x_mid / len(xys), '%', 'of the total')
        print(ys[y_mid:], 'is no more than', (len(ys) - y_mid) / len(xys) * 100, '%', 'of the total')

        # print(xys)
        # print(xys[x_mid + y_mid], x_mid + y_mid , 'should <=', ys[y_mid], y_mid, 'in ys')
        

        
        # print("we've ruled out ", x_mid / len(xs), '%', 'of the xs')
        # print(xys[-(x_mid + y_mid)], 'should >=', xs[x_mid], x_mid, 'in xs')
        # print("we've ruled out ", (len(ys) - y_mid) / len(ys), '%', 'of the ys')
        # print([xs, ys])
        # print(xys)
        # print(xys[int(len(xys)/2)])
        # print(xs[x_mid:])
        # print(ys[:y_mid])
        # print()

    else:
        print(xys)
        print(xys[x_mid + y_mid], 'should <=', xs[x_mid], x_mid, 'in xs')
        print(xys[-(x_mid + y_mid)], 'should >=',  ys[y_mid], y_mid, 'in ys')
        print()



def quarter_walk(nums1: List[int], nums2: List[int]) -> float:
    len1 = len(nums1)
    len2 = len(nums2)
    mid = int((len1 + len2) / 2) -1
    p1 = 0
    p2 = 0
    steps = 0
    flipper = -1
    while(p1 + p2 < mid):
        if p1 < len1 and p2 < len2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
                flipper = 1
            else:
                p2 += 1
                flipper  = 2
        elif p1 < len1:
            p1 = mid - p2
            flipper = 1
        else:
            p2 = mid - p1
            flipper = 2
    fst = 0
    if flipper == 1:
        fst = nums1[p1]
    else:
        fst = nums2[p2]

    if (len1 + len2) % 2 == 1:
        #one more itteration of above loop
        if p1 < len1 and p2 < len2:
            if nums1[p1] < nums2[p2]:
                p1 += 1
                flipper = 1
            else:
                p2 += 1
                flipper  = 2
        elif p1 < len1:
            p1 = mid - p2
            flipper = 1
        else:
            p2 = mid - p1
            flipper = 2

    snd = fst
    if flipper == 1:
        snd = nums1[p1]
    else:
        snd = nums2[p2]

    print([nums1, nums2])
    print("p1 =", p1, "p2 =", p2, "steps =", steps)
    print("fst =", fst, "snd =", snd, "median =", (fst + snd) / 2)
    return (fst + snd) / 2




    

if __name__ == "__main__":
    # test midpoint_test
    quarter_walk([1,10], [10,20,30,40,50,60,70,80,90,100])
    quarter_walk([1,2,3,4,5,6,7,8,9,10], [10,20,30,40,50,60,70,80,90,100])
    quarter_walk([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10])
    quarter_walk([1,2,3,4,5,6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10,11])
    quarter_walk(list(range(1,1100,3)), list(range(20,990, 4)))
    #midpoint_test([6,7,8,9,10], [1,2,3,4,5,6,7,8,9,10,11,12])
    
    # s = Solution()
    
    # nums1 = [1,2]
    # nums2 = [3,4,5,6,7,8,9,10, 10,20,30,40,50,60,70,80,90,100]
    # print('expected: (10+10)/2 = 10 -- got:', s.findMedianSortedArrays(nums1, nums2))


    # nums1 = [1,2,3,4,5,6,7,8,9]
    # nums2 = [10,20,30,40,50,60,70,80,90,100]
    # print('expected: (10+10)/2 = 10 -- got:', s.findMedianSortedArrays(nums1, nums2))
    # print()

    
    # nums1 = [1,10,20]
    # nums2 = [2,3,4,5,6,7,8,9,10,30,40,50,60,70,80,90,100]
    # print('expected: (10+10)/2 = 10 -- got:', s.findMedianSortedArrays(nums1, nums2))


