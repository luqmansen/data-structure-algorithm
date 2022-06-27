class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long = 0
        right = 0
        left = 0

        seen = set()
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right+=1
                
            else:
                seen.remove(s[left])
                left += 1
                
            
        
            # print(seen)
            long = max(long, len(seen))
            
        return long
            
            
        