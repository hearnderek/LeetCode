from queue import Queue
import sys
import re
import string
from dataclasses import dataclass
from typing import Any, List
from functools import partial

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

def too_short(password):
    return len(password) < 6

def too_long(password):
    return len(password) > 20

def no_lowercase(password):
    return not re.search(r'[a-z]', password)

def no_uppercase(password):
    return not re.search(r'[A-Z]', password)

def no_digit(password):
    return not re.search(r'\d', password)

def repeated_char(password) -> bool:
    return bool(re.search(r'(.)\1\1+', password))

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
        while q:
            path = q.get()
            if path.action:
                print(path.password, path.cost, ' -- ', path.action)
                
                new_pass = path.action(path.password)
                
                path.password = new_pass
                path.cost += 1
            
            if(path.password in seen):
                continue
            else:
                seen[path.password] = True

            remove = too_long(path.password)
            replace = repeated_char(path.password)
            add = no_lowercase(path.password) or no_uppercase(path.password) or no_digit(path.password) or too_short(path.password)

            if any([remove, replace, add]):
                if remove:
                    for i in range(len(path.password)):
                        q.put(PassPath(path.password, path.cost, partial(remove_char, at=i)))
                else:
                    for i in range(len(path.password)):
                        q.put(PassPath(path.password, path.cost, partial(replace_char, at=i)))
                    for i in range(len(path.password)+1):
                        q.put(PassPath(path.password, path.cost, partial(add_char, at=i)))
               

            else:
                # BFS so first find is best find
                print(path.password, path.cost)
                return path.cost

if __name__ == '__main__':
    s = Solution()
    #print(re.findall(r'((.)\2\2+)', 'aaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbb'))
    #print(repeated_char('aaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbb'))
    exit() 

    "aA1"
    print(s.strongPasswordChecker('aA1'))
    print(s.strongPasswordChecker('aaaB1'))
    print(s.strongPasswordChecker('1111111111'))
    print(s.strongPasswordChecker('ABABABABABABABABABAB1'))
    print(s.strongPasswordChecker('a'*20))
