class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        robA, robB = 0, 0
        
        for n in nums[0:len(nums)-1]:
            temp = max(robA + n, robB)
            robA = robB
            robB = temp
        
        rob1, rob2 = 0, 0
        
        for n in nums[1:]:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
            
        return max(rob2, robB)
        