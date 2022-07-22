import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)[:k]
        heapq.heapify(nums)
        
        return heapq.heappop(nums)
        
        
        