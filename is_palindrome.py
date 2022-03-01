class Solution:

    def isPalindrome(self, s: str) -> bool:
        # remove all characters that are invalid
        i = 0
        j = len(s) - 1
        while i < j:
            # move i forwards to next valid character
            ati = s[i]
            while not ati.isalnum(): 
                i += 1
                if i == j:
                    return True
                ati = s[i]

            # move j backwards to next valid character
            atj = s[j]
            while not atj.isalnum(): 
                j -= 1
                if i == j:
                    return True
                atj = s[j]

            # compare characters
            if ati.lower() != atj.lower():
                return False
            
            i += 1
            j -= 1
        return True


Solution().isPalindrome("A man, a plan, a canal: Panama")