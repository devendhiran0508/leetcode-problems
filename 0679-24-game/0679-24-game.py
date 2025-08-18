class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums):
            if len(nums)==1:
                return abs(nums[0]-24) < 1e-6
            n=len(nums)
            for i in range(n):
                for j in range(i+1,n):
                    a,b=nums[i],nums[j]
                    next_nums=[nums[k] for k in range(n) if k!=i and k!=j]

                    for res in {a+b,a-b,b-a,a*b} | ({a/b} if abs(b)>1e-6 else set()) | ({b/a} if abs(a)>1e-6 else set()):
                        if dfs(next_nums+[res]):
                            return True
            return False
        return dfs(cards)