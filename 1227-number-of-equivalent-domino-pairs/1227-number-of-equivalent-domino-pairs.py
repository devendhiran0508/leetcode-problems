class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num=[0]*100
        result=0
        for x,y in dominoes:
            value=x*10+y if x<=y else y*10+x
            result+=num[value]
            num[value]+=1
        return result