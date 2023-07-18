class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        valid = list("abcdefghijklmnopqrstuvwxyz0123456789")
        assert len(valid) == 26 + 10
        
        cleaned = ""
        for c in s:
            if c in valid:
                cleaned += c

        right = len(cleaned)-1

        for left, val in enumerate(cleaned):
            if val != cleaned[right-left]:
                return False

        return True
