class Solution:
    def wordBreak(self, s: str, wordDict: List[str], memo=None) -> bool:
        if memo is None:
            memo = {}
        
        if s in memo:
            return memo[s]
            
        if s == "":
            return True
        
        result = False
        for word in wordDict:
            # leetcode
            # leet
            # s - word
            if word == s[:len(word)]:
                result = result or self.wordBreak(s[len(word):], wordDict, memo)
        
        memo[s] = result
        return result
            