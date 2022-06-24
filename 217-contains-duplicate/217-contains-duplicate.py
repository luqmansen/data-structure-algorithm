class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        for n in nums:
            if n in temp:
                return True
            else:
                temp[n] = None
        
        return False
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
        
#         last = None
#         for n in nums:
#             if last is None:
#                 last = n
#                 continue
#             else:
#                 if n == last:
#                     return True
#             last = n
                
#         return False
        