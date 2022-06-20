from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]

        if target < 0:
            return []

        result = []
        for w in candidates:
            comb = self.combinationSum(candidates, target - w)
            for i in comb:
                i = [w, *i]
                result.append(i)

        nodup = []
        temp = {}
        for i in result:
            i.sort()
            key = str(i)
            if key not in temp:
                temp[key] = None
                nodup.append(i)
        return nodup


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))

