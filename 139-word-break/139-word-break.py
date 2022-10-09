class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def find(s, memo):
            if s in memo:
                return memo[s]
            
            if s == "":
                return True
            
            for word in wordDict:
                prefix = s[0:len(word)]
                
                if word == prefix:
                    to_find = s[len(word):] 
                    if find(to_find, memo):
                        memo[to_find] = True
                        return True
            
            memo[s] = False
            return False
        
        
        memo = {}
        return find(s, memo)