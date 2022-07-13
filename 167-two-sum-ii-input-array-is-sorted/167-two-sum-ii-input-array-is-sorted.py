class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        
        a, b = 0, len(num) -1
        while a < b :
            curr = num[a] + num[b] 
            if curr == target:
                return [a+1, b+1]
            else:
                if curr < target:
                    a +=1
                else:
                    b -= 1
                
