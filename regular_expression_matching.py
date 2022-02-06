class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Only implementing * and .

        # FSM
        base = 0
        repeat = 1
        repeat_char = None
        simplematch = 2
        simplematch_char = None

        wildcard = 3
        

        state = base

        regex = p
        regex_p = 0
        regex_len = len(p)
        input = s
        input_p = 0
        input_len = len(s)


        while regex_p < regex_len and input_p < input_len:

            if state == base:
                
                # check repeating
                if regex[regex_p] == "*":
                    state = repeat

                    # todo: parse regex failure if this happens at index 0
                    # todo: parse regex failure if repeat_char char is also a *
                    repeat_char = regex[regex_p-1]
                elif regex[regex_p] == ".":
                    state = wildcard
                else:
                    state = simplematch
                    simplematch_char = regex[regex_p]

            elif state == simplematch:    
                
                # direct string comparison case
                if simplematch_char == input[input_p]:
                    regex_p += 1
                    input_p += 1
                    state == base
                else:
                    return False

            else: # state == repeat
                
                if repeat_char == input[input_p]:
                    input_p += 1
                else:
                    regex_p += 1
                    state == base

        
        return True
