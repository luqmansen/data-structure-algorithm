class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 2n solution
        from collections import defaultdict

        _r = defaultdict(list)

        for idx, i in enumerate(nums):
            _r[i].append((target-i, idx))

        """
        [3,2,4]
        3: [(3,0)]
        2: [(4,1)]
        4: [(2,2)]
        """

        for k, v in _r.items():
            remainder, curr_idx = v.pop(0)
            if remainder in _r:
                if len(_r[remainder]) == 0:
                    continue
                    
                _, rem_idx = _r[remainder].pop(0)
                return [curr_idx, rem_idx]
