class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        duplicate = {}
        m = 0
        for i, char in enumerate(s):

            if char in duplicate and duplicate[char] >= l:
                l = duplicate[char] + 1
        
            m = max(m, i -l + 1)
            duplicate[char] = i

        return m