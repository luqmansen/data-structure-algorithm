class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        _s = defaultdict(int)
        _t = defaultdict(int)

        for i, j in zip(s, t):
            _s[i]+=1
            _t[j]+=1

        for i in _s:
            if i not in _t:
                return False

            if _s[i] != _t[i]:
                return False

        return True