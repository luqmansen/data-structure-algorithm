from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        s = set(nums)
        
        res = []
        
        for i in nums:
            
            # find start of seq
            if i-1 not in s:
                cnt = 0
                while True:
                    if i in s:
                        cnt +=1
                        i+=1
                    else:
                        break
                
                res.append(cnt)
        
        return max(res)
                
                
                
                
