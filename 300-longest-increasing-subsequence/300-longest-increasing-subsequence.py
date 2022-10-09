class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]

        # 3 2 1 0
        # [   2 1]
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):  #
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
    
    
    def lengthOfLIS2(self, nums: List[int]) -> int:
                
        def dfs(idx, memo):
            if idx in memo:
                return memo[idx]
            
            maks = 0
            
            for i in range(idx + 1 , len(nums)):
                if nums[i] > nums[idx] and i > idx:
                    maks = max (maks, 1 + dfs(i, memo))
            
            memo[idx] = maks
            return maks
        
        
        m = 0
        memo = {}
        
        for i, _ in enumerate(nums):
            m = max(m, 1 + dfs(i, memo))
        
        return m
            
        