from typing import List


# class Solution:
#     # cheating solution
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         return sorted([i * i for i in nums])

class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = [i * i for i in nums]

        for _ in nums:
            for idx, val in enumerate(arr):
                if idx != 0:
                    if val > arr[idx - 1]:
                        arr[idx] = arr[idx - 1]
                        arr[idx - 1] = val
        new_arr = []
        for idx, val in enumerate(arr):
            new_arr.append(arr[len(arr)-1-idx])

        return new_arr


if __name__ == '__main__':
    s = Solution()
    arr = [-4, -1, 0, 3, 10]

    assert s.sortedSquares(arr) == [0, 1, 9, 16, 100]
