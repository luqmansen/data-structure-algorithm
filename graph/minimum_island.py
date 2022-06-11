import typing
from typing import List

import typing
from typing import List


def explore(grid: List[List[str]], row: int, col: int, visited: typing.Set) -> int:
    if not (0 <= row < len(grid)):
        return 0
    if not (0 <= col < len(grid[0])):
        return 0

    if grid[row][col] == 0:
        return 0

    pos = f"{row}|{col}"
    if pos in visited:
        return 0

    visited.add(pos)
    cnt = 1

    cnt += explore(grid, row - 1, col, visited)
    cnt += explore(grid, row + 1, col, visited)
    cnt += explore(grid, row, col - 1, visited)
    cnt += explore(grid, row, col + 1, visited)

    return cnt


class Solution:
    def maxAreaOfIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        largest = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                curr = explore(grid, row, col, visited)
                largest = max(largest, curr)

        return largest


if __name__ == '__main__':
    s = Solution()
    grid = [[1,1,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,0],
            [0,0,0,0,0,0,1,1]]

    print(s.numIslands(grid))
