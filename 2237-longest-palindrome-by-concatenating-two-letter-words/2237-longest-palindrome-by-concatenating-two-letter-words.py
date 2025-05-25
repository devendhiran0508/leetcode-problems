class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        n=Counter(words)
        count=0
        a=0
        for i,freq in n.items():
            s=i[::-1]
            if i==s:
                count+=(freq//2)*4
                if freq%2:
                    a=1
            elif i<s and s in n:
                count+=min(freq,n[s])*4
        return count+a*2