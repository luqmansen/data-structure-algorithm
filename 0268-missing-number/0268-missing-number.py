class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # 3 + 2 + 1 = 6
        # n + n-1 + n-2 + ... = 
        
        should_total = 0
        for n in range(len(nums)+1):
            should_total += n
        
        actual = sum(nums)
        
        return should_total - actual
            
        