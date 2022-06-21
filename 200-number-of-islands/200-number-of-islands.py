
import typing
from typing import List


def explore(grid: List[List[str]], row: int, col: int, visited: typing.Set) -> bool:
    if not (0 <= row < len(grid)):
        return False
    if not (0 <= col < len(grid[0])):
        return False

    if grid[row][col] == "0":
        return False

    pos = f"{row}|{col}"
    if pos in visited:
        return False

    visited.add(pos)

    explore(grid, row - 1, col, visited)
    explore(grid, row + 1, col, visited)
    explore(grid, row, col - 1, visited)
    explore(grid, row, col + 1, visited)

    return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if explore(grid, row, col, visited):
                    count += 1

        return count
