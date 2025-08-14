class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxDigit='\0'

        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                maxDigit=max(maxDigit,num[i])
        return '' if maxDigit=='\0' else maxDigit*3