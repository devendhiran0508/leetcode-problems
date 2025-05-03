class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        result=float('inf')
        for i in range(1,7):
            result=min(result,self.rotation(tops,bottoms,i))
            result=min(result,self.rotation(bottoms,tops,i))
        return -1 if result==float('inf') else result

    def rotation(self,tops,bottoms,target):
        rotations=0
        for i in range(len(tops)):
            if tops[i]==target:
                continue
            if bottoms[i]==target:
                rotations+=1
            else:
                return float('inf')
        return rotations
        