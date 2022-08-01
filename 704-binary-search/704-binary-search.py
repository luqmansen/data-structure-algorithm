class Solution:
    def search(self, arr: list, target: int) -> int:
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