class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## Explination
        # Slow set & range solution

        longest = 0

        len_s = len(s)

        # check only strings that are longest + 1 in length
        for start_i in range(len_s):
            last_end = None
            char_set = None
            for end_i in range(start_i + longest + 1, len_s+1):
                
                if char_set is None:
                    # create the set
                    char_set = set(s[start_i:end_i])
                else:
                    # adding new chars to existing set
                    char_set.update(s[last_end:end_i])

                len_i = end_i - start_i
                if len(char_set) != len_i:
                    break # out to start_i loop

                longest = len_i
                last_end = end_i - 1
                

        return longest

s = Solution()

print("abcabcbb", s.lengthOfLongestSubstring("abcabcbb"))
print("bbbbb", s.lengthOfLongestSubstring("bbbbb"))
print("pwwkew", s.lengthOfLongestSubstring("pwwkew"))
print(" ", s.lengthOfLongestSubstring(" "))
print("a", s.lengthOfLongestSubstring("a"))
print("au", s.lengthOfLongestSubstring("au"))

