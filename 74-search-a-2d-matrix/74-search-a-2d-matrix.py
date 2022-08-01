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
            
        left, right = 0, len(matrix) - 1
        
        while left <= right:
            mid = left + (right - left ) // 2
            midVal = matrix[mid][0]

            if midVal == target:
                return True
            
            elif target < midVal:
                right = mid - 1
            
            elif target > midVal:
                last = matrix[mid]
                lastVal = last[-1]
                
                if target == lastVal:
                    return True
                
                elif target < lastVal:
                    res = search(last, target)
                    return True if res != -1 else False
                
                elif target > lastVal:
                    left = mid + 1
        
        return False
                
    

        

                