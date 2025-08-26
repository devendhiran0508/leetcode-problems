class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiag=0
        maxArea=0

        for l,w in dimensions:
            diagSq=(l*l)+(w*w)
            area=l*w
            if diagSq>maxDiag or(diagSq==maxDiag and area>maxArea):
                maxDiag=diagSq
                maxArea=area
        return maxArea