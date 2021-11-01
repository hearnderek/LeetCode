def between(x, min, max):
    return min < x < max

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    
        
        # All of the changes to return with no chance on elements needing changes
        if not board:
            return
        cols = len(board)
        if cols < 3:
            return board
        rows = len(board[0])
        if rows < 3:
            return board
        
        IS_X = 0
        IS_O = 1
        IS_UNKNOWN = 2
        
        # our unique stack of spots to check
        # honestly it could just be a list
        to_check = set()
        

        # dict key = (row, col)
        # dict value = IS_X or IS_O or IS_UNKNOWN
        state_board = dict()
        
        # Populate state_board -- identifing anything that could possibly change
        # All 'O's on found on the outside get added to stack for a depth first search
        for i in range(cols):
            for j in range(rows):
                if board[i][j] == 'X':
                    state_board[(i, j)] = IS_X
                else:
                    if (i == 0 or i == cols - 1 or j == 0 or j == rows - 1):
                        state_board[(i, j)] = IS_O
                        to_check.add((i, j))
                    else:
                        state_board[(i, j)] = IS_UNKNOWN

        # Anything in to_check is a 'O'
        # This way we can deduce that anything 'unknown' is ultimately connected to the edge
        while to_check:
            (i, j) = to_check.pop()
            for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if between(x, 0, cols - 1) and between(y, 0, rows - 1) and state_board[(x, y)] == IS_UNKNOWN:
                    if state_board[(x, y)] == IS_UNKNOWN:
                        state_board[(x, y)] = IS_O
                        to_check.add((x, y))

        # inefficent way to set the board
        for ((i, j), state) in state_board.items():
            if state == IS_UNKNOWN:
                board[i][j] = 'X'
            elif state == IS_O:
                board[i][j] = 'O'


                    
        