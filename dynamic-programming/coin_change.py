import math
from typing import List


class Solution:
    """
    1 2 3

    1 + 1 + 1 + ... = 5

    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        memo = {}
        few = self.explore(coins, amount, memo=memo)

        return few if few != math.inf else -1

    def explore(self, coins: List[int], amount, level=0, memo=None):
        if memo is None:
            memo = {}

        if amount in memo:
            return memo[amount]

        if amount == 0:
            return level

        if amount < 0:
            return math.inf

        minlvl = math.inf
        for i in coins:
            # print("level: ", level, "amount:", amount, "coin:", i)
            minlvl = min(minlvl, self.explore(coins, amount - i, level+1, memo))

        memo[amount] = minlvl
        return minlvl


if __name__ == "__main__":
    f = Solution()
    # print(f.coinChange([1, 2, 5], 10))
    # print(f.coinChange([2], 2))
    # print(f.coinChange([2], 3))
    # print(f.coinChange([1], 0))
    print(f.coinChange([3, 7, 405, 436], 8839))
    # print(f.coinChange([186, 419, 83, 408], 6249))
