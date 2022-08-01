def search(arr: list, target: int) -> int:
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            
            mid = left + (right - left)//2
            
            if arr[mid] == target:
                return mid
                
            elif arr[mid] < target:
                left = mid + 1
                
            elif arr[mid] > target:
                right = mid - 1
           
                
        return -1

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        
        
        arr = []
        for i in matrix:
            arr = [*arr , *i]
        
        res = search(arr, target)
        
        return True if res != -1 else False
        

                