class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        an = {} # key word, v [w]
        
        for w in strs:
            s = sorted(w)
            s = "".join(s)
            
            if s in an:
                an[s].append(w)
            else:
                an[s] = [w]
                
        l = []
        for _, v in an.items():
            l.append(v)
            
        return l
                
        
        
        
        
        