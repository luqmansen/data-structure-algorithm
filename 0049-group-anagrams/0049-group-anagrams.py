from collections import defaultdict
        
class Solution:
    def _calc(self, word) -> list:
        m = [0] * 26 # at most 26 alphabet english lowercase
        for c in word:
            idx = ord(c) - ord('a')
            m[idx]+=1
        return m

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        O(n * 26) solution
        """
  
        g = defaultdict(list)

        for s in strs:
            key = str(self._calc(s))
            g[key].append(s)

        return g.values()



    def groupAnagrams_2(self, strs: List[str]) -> List[List[str]]:
        """
        O(n * nlog(n)) solution
        for each input, need to sort the string (n log(n))
        """

        g = defaultdict(list)

        for s in strs:

            k = str(sorted(s))

            g[k].append(s)

        return g.values()

