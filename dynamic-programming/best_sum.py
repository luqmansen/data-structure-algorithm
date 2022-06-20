
"""
bruteforce
m = target
n = nums length

time: O(n^m)

"""

def best_sum(target: int, nums: list[int], memo=None) -> list[int]:
    if memo is None:
        memo = dict()

    if target in memo:
        return memo[target]

    if target == 0:
        return []
    if target < 0:
        return None

    current_shortest = None
    for n in nums:
        res = best_sum(target - n, nums, memo)
        if res is not None:
            if current_shortest is None or len(res) < len(current_shortest):
                current_shortest = [*res, n]

    memo[target] = current_shortest
    return current_shortest


if __name__ == '__main__':
    print(best_sum(8, [2, 3, 5]))  # [5,3]
    print(best_sum(8, [1, 4, 5]))  # [4,4]
    print(best_sum(100, [1, 2, 3, 6, 7, 5, 25]))  # [25,25,25,25]
