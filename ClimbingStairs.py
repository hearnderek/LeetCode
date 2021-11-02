class Solution:
    def climbStairs(self, n: int) -> int:
        # return number of distinct ways you can climb the stairs
        # possible moves: 1 step, 2 steps
        # n = 1 ∴ r = 1
        # n = 2 ∴ r = n[1] + n[0]
        # trying to reduce memory usage
        
        prev1 = 1
        if n == 1:
            return prev1

        prev2 = 2
        if n == 2:
            return prev2
        
        for i in range(3, n):
            prev2 = prev1 + prev2
            prev1 = prev2 - prev1
            
        return prev1 + prev2


    def first_climbStairs(self, n: int) -> int:
        # return number of distinct ways you can climb the stairs
        # possible moves: 1 step, 2 steps
        # n = 1 ∴ r = 1
        # n = 2 ∴ r = n[1] + n[0]
        solutions = {0:1, 1:1}
        i = 2
        while (n not in solutions):
            solutions[i] = solutions[i-1] + solutions[i-2]
            i += 1

        return solutions[n]


if __name__ == "__main__":
    sol = Solution()
    for i in range(1, 10):
        print(sol.climbStairs(i), 'vs', sol.first_climbStairs(i))