import math
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        maks = - math.inf

        # [1,8,6,2,5,4,8,3,7]
        while l < r:
            
            left = height[l]
            right = height[r]
            
            vol = min(left, right) * (r - l)

            # print(vol, r, l)
            maks = max(maks, vol)
            
            
            if left > right:
                r -=1
            else:
                l +=1
        
        return maks
            




