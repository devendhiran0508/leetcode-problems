class Solution:
    def maxOperations(self, s: str) -> int:
        count1 = 0
        res = 0
        i = 0
        while i < len(s):
            if s[i] == '0':
                while i + 1 < len(s) and s[i + 1] == '0':
                    i += 1
                res += count1
            else:
                count1 += 1
            i += 1
        return res