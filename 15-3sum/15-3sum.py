class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # print(nums)
        result = {}
        for i in range(len(nums)):
            a, b = i+1, len(nums) -1
            
            while a < b:
                curr = nums[i] + nums[a] + nums[b]
                # print(curr, nums[i] , nums[a] , nums[b])
                if curr == 0:
                    result[f"{nums[i]}|{nums[a]}|{nums[b]}"] =  [nums[i] ,nums[a] ,nums[b]]
                    b-=1
                    a+=1
                elif curr < 0:
                    a+=1
                elif curr > 0:
                    b-=1
        
        r = []
        for _, v in result.items():
            r.append(v)
                
        return r
                