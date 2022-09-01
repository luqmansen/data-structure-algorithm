from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)
        
        seen = {}

        def do(nums, idx, tot=0):
            
            if idx in seen:
                return seen[idx]

            if idx > len(nums) - 1 or idx < 0:
                return 0

            tot += nums[idx]

            meks = []
            for iv in range(2, len(nums)):
                meks.append(do(nums, idx + iv))

            tot += max(meks)
            
            seen[idx] = tot
            
            return tot

        res = []
        for i, _ in enumerate(nums):
            res.append(do(nums, i))

        return max(res)


if __name__ == '__main__':
    s = Solution()

    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2,1,1,2]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
    assert s.rob([1,1]) == 1
    assert s.rob([6,3,10,8,2,10,3,5,10,5,3]) == 39
