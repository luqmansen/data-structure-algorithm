class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile('[\W_]+')
        s = pattern.sub('', s)
        
        left, right = 0, len(s)-1
        
        while left != right and right >= 0 and left >= 0:
            if s[left].lower() != s[right].lower():
                return False
        
            left +=1
            right -=1
            
        return True
        