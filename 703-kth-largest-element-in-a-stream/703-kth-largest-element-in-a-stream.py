import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = sorted(nums,reverse=True)[:k+1]
        heapq.heapify(self.arr)
        while len(self.arr) > k:
            heapq.heappop(self.arr)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        if len(self.arr) > self.k:
            heapq.heappop(self.arr)
            
        return self.arr[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# 10 5 3 4, 5, 8, 2 = 4