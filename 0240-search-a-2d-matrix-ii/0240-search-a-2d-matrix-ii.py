class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        row=0
        col=m-1
        while row<n and col>=0:
            val=matrix[row][col]
            if val==target:
                return True
            elif val>target:
                col-=1
            elif val<target:
                row+=1
        return False