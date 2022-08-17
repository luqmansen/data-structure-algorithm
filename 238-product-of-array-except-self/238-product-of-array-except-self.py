class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod = 1
        
        zCnt = 0
        
        for i, n in enumerate(nums):
            if n != 0:
                prod *= n
                    
            if n == 0:
                zCnt += 1                    
        
        for i, n in enumerate(nums):
            if zCnt == 0:
                nums[i] = int(prod/n)
            else:
                if n == 0 and zCnt == 1:
                    nums[i] = prod
                else:
                    nums[i] = 0
            
        return nums
                
        
        
        