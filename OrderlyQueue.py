"""
899. Orderly Queue
Hard


You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..

Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

 

Example 1:

Input: s = "cba", k = 1
Output: "acb"
Explanation: 
In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".
Example 2:

Input: s = "baaca", k = 3
Output: "aaabc"
Explanation: 
In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".
 

Constraints:

1 <= k <= s.length <= 1000
s consist of lowercase English letters.

"""



class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # Can we calculate the best answer and skip the actual steps?
        
        # If you have k >= 2 you can swap adjacent letters
        # If we swap any letters we can arrange the letters in what ever way we like.
        # This means for k >= 2 your string will always be the optimum arrangement
        # Sort the string and return it.
        
        # If you have k = 1 you can choose your starting letter.
        
        
        if k > 1:
            return "".join(sorted(s))
        
        # This can be optimized
        # If we walk through the characters we can avoid the string creation
        return min([ s[i:] + s[:i] for i in range(0,len(s))])