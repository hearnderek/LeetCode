class Solution:
    def reverse(self, x: int) -> int:
        # Lazy str approach

        r = int(str(abs(x))[::-1]) 
        if x < 0:
            r = -r
        
        if -2147483647 > r or r >= 2147483647:
            return 0
        
        return r