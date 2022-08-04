class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        
        change = 0
        maxB = nums[0]
        before = nums[:]
        
        for i,n in enumerate(nums):
            if i == len(nums) - 1:
                break
            
            nex = nums[i+1]
            
            if n > nex:
                if maxB > min(n, nex) and i != 0:
                    nums[i+1] = max(maxB, n, nex)
                    change+=1
                else:
                    nums[i] = min(n, nex)
                    change+=1
                        
            maxB = max(maxB, n)
            
        print(before, nums, change)
        return True if change <= 1 else False
            
        