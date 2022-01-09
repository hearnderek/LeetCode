class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        
        # slow but fast to write
        s = str(x)
        return s == s[::-1]