class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        an = {} # key word, v [w]
        
        # time complexity = n * m log m
        
        for w in strs:
            count = [0] * 26
            
            for c in w:
                count[ord(c) - ord("a")] += 1
            
            s = tuple(count)
            
            if s in an:
                an[s].append(w)
            else:
                an[s] = [w]
                
        l = []
        for _, v in an.items():
            l.append(v)
        
        return l
                
        
        
        
        
        