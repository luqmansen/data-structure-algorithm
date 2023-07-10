class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import defaultdict

        g = defaultdict(int)

        for n in nums:
            g[n]+=1

        b = [[]] * (len(nums) + 1)

        for key,val in g.items():
            if len(b[val]) > 0:
                b[val].append(key)
            else:
                b[val] = [key]

        res = []
        for i in list(reversed(b)):
            if len(i) > 0 and len(res) < k:
                res=[*res ,*i]

        return res  





        

