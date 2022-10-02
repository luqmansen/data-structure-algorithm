from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0, 0
        # [rob1, rob2, n, n+1, ...]
        # rob1, rob2 [ n, n+1, ...]
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2
            
        
            

        


if __name__ == '__main__':
    s = Solution()

    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2,1,1,2]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
    assert s.rob([1,1]) == 1
    assert s.rob([6,3,10,8,2,10,3,5,10,5,3]) == 39
