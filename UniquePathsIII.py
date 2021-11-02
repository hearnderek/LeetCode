from typing import List, Tuple
from dataclasses import dataclass

OBSTACLE = -1
EMPTY = 0
START = 1
END = 2
AT = -2

def clone_grid(grid: List[List[int]]) -> List[List[int]]:
    return [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]


@dataclass
class Path:
    grid: List[List[int]]
    x_count: int
    y_count: int
    location: Tuple[int, int]
    steps: int

def is_valid(x, y, path: Path) -> bool:
    return 0 <= x < path.x_count and 0 <= y < path.y_count

def clone_path(path: 'Path') -> 'Path':
    return Path(clone_grid(path.grid), path.x_count, path.y_count, path.location, path.steps)

def get_possible_paths(path: 'Path') -> List['Path']:
    (x1, y1) = path.location
    for (x2, y2) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x2 = x1 + x2
        y2 = y1 + y2
        if is_valid(x2, y2, path) and path.grid[x2][y2] == EMPTY:
            cloned_path = clone_path(path)
            cloned_path.grid[x1][y1] = path.x_count * path.y_count - cloned_path.steps
            cloned_path.grid[x2][y2] = AT
            cloned_path.location = (x2, y2)
            cloned_path.steps += 1

            yield cloned_path

def is_end(path: 'Path') -> bool:
    (x1, y1) = path.location
    for (x2, y2) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        x2 = x1 + x2
        y2 = y1 + y2
        if is_valid(x2, y2, path) and path.grid[x2][y2] == END:
            return True

def fully_traversed(path: 'Path') -> bool:
    for row in path.grid:
        for cell in row:
            if cell == EMPTY:
                return False
    return True

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        foundPaths = 0
        path_stack = list()

        start_location: Tuple[int, int] = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == START:
                    start_location = (i, j)
                    break

        path_stack.append(Path(clone_grid(grid), len(grid), len(grid[0]), start_location, 0))

        while path_stack:
            path = path_stack.pop()
            paths = list(get_possible_paths(path))
            if len(paths) > 0:
                for foundpath in paths:
                    path_stack.append(foundpath)
            elif is_end(path) and fully_traversed(path):
                foundPaths += 1

        return foundPaths

        
if __name__ == "__main__":
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    print(Solution().uniquePathsIII(grid))