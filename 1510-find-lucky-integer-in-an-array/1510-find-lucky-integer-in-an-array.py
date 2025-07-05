class Solution:
    def findLucky(self, arr: List[int]) -> int:
        fre=Counter(arr)
        res=-1
        for num,count in fre.items():
            if num==count:
                res=max(res,num)
        return res