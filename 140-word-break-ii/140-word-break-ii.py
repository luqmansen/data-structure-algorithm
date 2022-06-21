from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = self.dfs(s, wordDict)

        if res is None:
            return []

        return res

    def dfs(self, s: str, wordDict: List[str]) -> List[str]:
        if s == "":
            return []

        result = None
        for word in wordDict:
            if word == s[:len(word)]:
                remainder = s[len(word):]
                comb = self.dfs(remainder, wordDict)
                if comb is None:
                    continue

                if len(comb) > 0:
                    for i, v in enumerate(comb):
                        comb[i] = word + " " + "".join(v)
                    if result is None:
                        result = []
                    result = [*comb, *result]
                else:
                    if result is None:
                        result = []
                    result = [word, *result]

        return result

