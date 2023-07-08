class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        
        g = defaultdict(list)

        for s in strs:

            k = str(sorted(s))

            g[k].append(s)

        return g.values()

