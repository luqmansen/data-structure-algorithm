class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        tm = {}
        sm = {}
        
        for c in s:
            if c in sm:
                sm[c]+=1
            else:
                sm[c] = 0
        
        for c in t:
            if c in tm:
                tm[c]+=1
            else:
                tm[c] = 0
                
        for k, v in sm.items():
            if k not in tm:
                return False
            if v != tm[k]:
                return False
        
        return True
        