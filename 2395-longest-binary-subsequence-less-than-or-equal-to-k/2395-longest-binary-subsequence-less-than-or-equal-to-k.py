class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        a=0
        count=0
        bits=k.bit_length()
        for i,j in enumerate(s[::-1]):
            if j=="1":
                if i<bits and a+(1<<i)<=k:
                    a+=1<<i
                    count+=1
            else:
                count+=1
        return count