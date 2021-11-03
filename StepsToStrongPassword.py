from queue import Queue
import sys
import re
import string
from dataclasses import dataclass
from typing import Any, List
from functools import partial, lru_cache

### State ###

# Timing out on test case "bbaaaaaaaaaaaaaaacccccc"
# I need to figure out how to limit the number of paths to test.
# 
# 1. method I can think of is to target repeated characters as a first priority issue,
#    then, I'll split them into even groups of 2
#    the seperators will all take a replace, add, and remove action.
#
# 2. I can also calculate a rough estimate of the number of actions to make
#    For example, number of issues found (tripplet+ chars counted too)
#    I worry that this will hide some better path.

###

# Strong password requirement

# 6 <= x <= 20
# r'[a-z]'
# r'[A-Z]'
# r'\d'

ALPHA_NUMERIC = string.ascii_lowercase + string.ascii_uppercase + string.digits

### Corrective Actions ###

# add_char,
# add_lower,
# add_upper,
# add_digit,
# remove_char
# replace_char

def set_choice(possibles):
    return possibles[0]

def add_char(password, at=None) -> str:
    # add a random character from ALPHA_NUMERIC
    if at and 0 <= at < len(password):
        return password[:at] + get_best_possible_char(password, at) + password[at:]
    else:
        return password + set_choice(get_best_possible_char(password, len(password)-1))



def add_lower(password) -> str:
    # add a random lowercase letter
    can_add = string.ascii_lowercase.replace(password[-1], '')
    return password + set_choice(can_add)


def add_upper(password) -> str:
    # add a random uppercase letter
    can_add = string.ascii_uppercase.replace(password[-1], '')
    return password + set_choice(can_add)


def add_digit(password) -> str:
    # add a random digit
    can_add = string.digits.replace(password[-1], '')
    return password + set_choice(can_add)


def remove_char(password, at):
    return password[:at] + password[at+1:]

def replace_char(password, at):
    return password[:at] + get_best_possible_char(password, at) + password[at+1:]

def get_best_possible_char(password: str, at: int = None) -> str:
    possibles = ALPHA_NUMERIC
    if no_lowercase(password):
        possibles = string.ascii_lowercase
    if no_uppercase(password):
        possibles = string.ascii_uppercase
    if no_digit(password):
        possibles = string.digits
    
    if at:
        after_removal = password[:at] + password[at+1:]
    else:
        after_removal = password

    if no_lowercase(after_removal):
        possibles = string.ascii_lowercase
    if no_uppercase(after_removal):
        possibles = string.ascii_uppercase
    if no_digit(after_removal):
        possibles = string.digits

    if at:
        if at-1 >= 0:
            possibles = possibles.replace(password[at-1], '')
        if at+1 < len(password):
            possibles = possibles.replace(password[at+1], '')

    return set_choice(possibles)

### find issues ###

@lru_cache(maxsize=None)
def count_lower(password) -> int:
    return len(re.findall(r'[a-z]', password))

@lru_cache(maxsize=None)
def count_upper(password) -> int:
    return len(re.findall(r'[A-Z]', password))

@lru_cache(maxsize=None)
def count_digits(password) -> int:
    return len(re.findall(r'\d', password))

def too_short(password):
    return len(password) < 6

def too_long(password):
    return len(password) > 20

def no_lowercase(password):
    return count_lower(password) == 0

def no_uppercase(password):
    return count_upper(password) == 0

def no_digit(password):
    return count_digits(password) == 0

def repeated_char(password) -> bool:
    return bool(re.search(r'(.)\1\1+', password))

def first_third_repeated_char(password) -> int:
    return re.search(r'(.)\1\1', password).end() - 1

def repeated_char_count(password) -> int:
    count = 0
    for (x,_) in re.findall(r'((.)\2\2+)', password):
        print(x)
        count += len(x)

    return count

@dataclass
class PassPath:
    password: str
    cost: int
    action: Any

### main ###

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        q = Queue()
        q.put(PassPath(password, 0, None))
        
        seen = dict()
        
        best = sys.maxsize
        while q.qsize() > 0:
            path = q.get()
            if path.action:
                #print(path.password, path.cost, ' -- ', path.action)
                
                new_pass = path.action(path.password)
                
                path.password = new_pass
                path.cost += 1
            
            if(path.password in seen or path.cost >= best):
                continue
            else:
                seen[path.password] = True

            has_repeating = repeated_char(path.password)
            remove = too_long(path.password)
            replace = has_repeating
            add = no_lowercase(path.password) or no_uppercase(path.password) or no_digit(path.password) or too_short(path.password)
            
            # Once we're just removing characters, we can accurately calculate the cost without simulation
            if remove and not add and not replace:
                #print(path.password, path.cost, q.qsize())
                best = min(best, path.cost + len(path.password) - 20)
                continue

            if any([remove, replace, add]):
                #print("adding more actions", remove, add, replace)
                if has_repeating:
                    # fastest way to break up a repeating string
                    # is to split it into groups of 2
                    # the two ways of doing that is to ]
                    # 1. replace 'aaaa' -> 'aa.a' 
                    # 2. add 'aaaa' -> 'aa.aa'
                    q.put(PassPath(path.password, path.cost, partial(replace_char, at=first_third_repeated_char(path.password)))) 
                    q.put(PassPath(path.password, path.cost, partial(add_char, at=first_third_repeated_char(path.password)))) 
                    if remove:
                        q.put(PassPath(path.password, path.cost, partial(remove_char, at=first_third_repeated_char(path.password)))) 
                elif remove and add and not has_repeating:
                    # if we replace before adding, we can get the string into a state that we can simply calculate how many to remove
                    for i in range(len(path.password)):
                        q.put(PassPath(path.password, path.cost, partial(replace_char, at=i)))
                elif remove:
                    # if you have too many chars it will never be faster to do anything other than remove
                    # Instead of calculating which character to remove, I am brute forcing every path
                    lower_count = count_lower(path.password)
                    upper_count = count_upper(path.password)
                    digit_count = count_digits(path.password)
                    for i in range(len(path.password)):
                        if lower_count == 1 and path.password[i] in string.ascii_lowercase:
                            continue
                        if upper_count == 1 and path.password[i] in string.ascii_uppercase:
                            continue
                        if digit_count == 1 and path.password[i] in string.digits:
                            continue

                        q.put(PassPath(path.password, path.cost, partial(remove_char, at=i)))
                else:
                    # This is the needlessly expensive part
                    # I am brute forcing every possible path for both replace and add
                    for i in range(len(path.password)):
                        q.put(PassPath(path.password, path.cost, partial(replace_char, at=i)))
                    for i in range(len(path.password)+1):
                        q.put(PassPath(path.password, path.cost, partial(add_char, at=i)))
               

            else:
                # BFS so first find is best find
                print(path.password, path.cost)
                return path.cost
        
        return best


if __name__ == '__main__':
    s = Solution()
    #print(re.findall(r'((.)\2\2+)', 'aaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbb'))
    #print(first_third_repeated_char('aaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbb'))
    #exit() 

    "aA1"
    print(s.strongPasswordChecker('aA1'))
    print(s.strongPasswordChecker('aaaB1'))
    print(s.strongPasswordChecker('1111111111'))
    print(s.strongPasswordChecker('ABABABABABABABABABAB1'))
    print(s.strongPasswordChecker('a'*20))
    print(s.strongPasswordChecker("hoAISJDBVWD09232UHJEPODKNLADU1"))
    print(s.strongPasswordChecker("aaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbb"))
    print(s.strongPasswordChecker(string.ascii_lowercase))
    print(s.strongPasswordChecker(string.ascii_lowercase + 'aaaaaaaaaaa'))
