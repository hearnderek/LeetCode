class Solution:
    def isValid(self, s: str) -> bool:
        # having a non zero lenth list allows us to use parens_stack[-1] safely without checks
        parens_stack = [-1]
        
        # hardcoded equilivant to 
        # list([ord(c) for c in "()[]{}"])
        # Note that all open parens are on the even index
        filterTo = [40, 41, 91, 93, 123, 125]

        for c in s:
            ascii = ord(c)

            # index function gives an exception in the none so here in a modified inline version
            filterIndex = -1
            for i, f in enumerate(filterTo):
                if f == ascii:
                    filterIndex = i
                    break
            
            # Filtering out all inconsequential characters
            if filterIndex == -1:
                continue
            
            ## Handle all open tokens
            if not (filterIndex & 1): # even index
                parens_stack.append(ascii)
                continue

            ## Handle all close tokens
            # difference is correct when 1 or 2
            if abs(parens_stack[-1] - ascii) > 2:
                return False
            
            # must be the correct closing paren if here
            parens_stack.pop()

        # handle unclosed parens
        if len(parens_stack) > 1:
            return False

        return True
            
                

s = Solution()

print(s.isValid("()[]{}"))
print(s.isValid("()[{]}"))
print(s.isValid("([{}])"))

