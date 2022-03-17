
def canCross(stones):
    return canCrossInner(stones, 1, dict())

def genMemoKey(stones, k):
    return (len(stones), k)

def possibleK(k):
    return (k - 1, k, k + 1)

def canCrossInner(stones, k, memo):
    memoKey = genMemoKey(stones, k)
    if memoKey in memo:
        return memo[memoKey]

    # On last stone
    if memoKey[0] <= 1:
        return True

    possableKs = possibleK(k)
    curStone = stones[0]
    i = 0
    for stone in stones[1:]:
        i += 1
        targetK = stone - curStone
        if targetK > possableKs[2]:
            break

        if targetK in possableKs:
            if canCrossInner(stones[i:], targetK, memo):
                return True

    memo[memoKey] = False
    return False


class Solution:
    def canCross(self, stones):
        numStones = len(stones)
        if numStones <= 1:
            return True

        if stones[1] != 1:
            return False

        return canCrossInner(stones, 0, dict())
    
