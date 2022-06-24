class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        last = None
        for n in nums:
            if last is None:
                last = n
                continue
            else:
                if n == last:
                    return True
            last = n
                
        return False
        