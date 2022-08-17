class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        an = {} # key word, v [w]
        
        # time complexity = n * m log m
        
        for w in strs:
#             this solution is slightly longer even in theory it has better 
#.            time complexity n * m -> m is average length of the word            
#             prolly because of need to realocate below var multiple times

#             count = [0] * 26
#             for c in w:
#                 count[ord(c) - ord("a")] += 1
#             s = tuple(count)

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
                
        
        
        
        
        