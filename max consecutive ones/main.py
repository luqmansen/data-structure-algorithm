from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    curr = 0
    maks = 0
    for i in nums:
        if i == 1:
            curr += 1
        else:
            maks = max(curr, maks)
            curr = 0

    return max(maks, curr)


if __name__ == '__main__':
    arr = [1, 0, 1, 1, 0, 1]
    assert findMaxConsecutiveOnes(arr) == 2
    arr = [1]
    assert findMaxConsecutiveOnes(arr) == 1
    arr = [1, 0, 1, 1]
    assert findMaxConsecutiveOnes(arr) == 2


