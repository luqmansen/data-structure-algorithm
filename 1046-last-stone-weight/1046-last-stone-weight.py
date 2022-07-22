class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        
        while len(stones) >= 2:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            
            s = abs(a - b)
            if s > 0:
                heapq.heappush(stones, -s)
        
        if len(stones) == 0:
            return 0
        
        return -heapq.heappop(stones)
        