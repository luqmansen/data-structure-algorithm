from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for i in nums:
            word = [j for j in str(i)]
            if len(word) % 2 == 0:
                cnt +=1

        return cnt


if __name__ == '__main__':
    s = Solution()
    assert s.findNumbers([12, 345, 2, 6, 7896]) == 2
    assert s.findNumbers([555,901,482,1771]) == 1
