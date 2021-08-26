import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        i = 0  # for Nums1
        j = 0  # for nums2

        finalArr = []
        #      i     j
        # [1,2,4] [2,3]

        while i < len(nums1) or j < len(nums2):

            currI = nums1[i] if i < len(nums1) else pow(10,6)+1
            currJ = nums2[j] if j < len(nums2) else pow(10,6)+1

            if currI < currJ:
                finalArr.append(currI)
                i += 1
            elif currJ == currI:
                finalArr.append(currI)
                finalArr.append(currJ)
                i += 1
                j += 1

            else:
                finalArr.append(currJ)
                j += 1

        print(finalArr)

        arrLen = len(finalArr)
        if arrLen % 2 != 0:
            idx = int(math.ceil(arrLen/2)) - 1
            return finalArr[idx]
        else:
            idx = int(arrLen/2) -1
            return (finalArr[idx] + finalArr[idx+1])/2

if __name__ == '__main__':
    s = Solution()

    a = [100000]
    b = [100001]
    print(s.findMedianSortedArrays(a,b))