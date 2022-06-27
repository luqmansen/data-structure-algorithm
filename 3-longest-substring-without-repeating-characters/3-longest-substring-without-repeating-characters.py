class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long = 0
        right = 0
        left = 0

        seen = set()
        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
            else:
                left += 1
                right = left
                seen = {s[left]}
            
        
            right+=1
            # print(seen)
            long = max(long, len(seen))
            
        return long
            
            
        