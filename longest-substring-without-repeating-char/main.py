class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        i = 0
        j = 0
        seen = {}

        while i < len(s):
            char = s[i]
            if char not in seen:
                seen[char] = 0
                maxLen = max(maxLen, i-j+1)
                i += 1
            else:
                del seen[s[j]]
                j += 1

        return maxLen



if __name__ == '__main__':
    sol = Solution()
    # print(sol.lengthOfLongestSubstring("ckilbkd"))
    # print(sol.lengthOfLongestSubstring("dvdf"))
    # print(sol.lengthOfLongestSubstring("bbbbb"))
    print(sol.lengthOfLongestSubstring("pwwkew"))

# "c k i l b k d"
