class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i,j):
            left=i
            right=j-1
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        for i in range(len(s),0,-1):
            for j in range(len(s)-i+1):
                if check(j,i+j):
                    return s[j:j+i]
        return ""