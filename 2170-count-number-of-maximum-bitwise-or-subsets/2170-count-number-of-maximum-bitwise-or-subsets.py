class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.maxOR=0
        self.count=0
        def backtrack(index,curOR):
            if index==len(nums):
                if curOR>self.maxOR:
                    self.maxOR=curOR
                    self.count=1
                elif curOR==self.maxOR:
                    self.count+=1
                return 
            backtrack(index+1,curOR|nums[index])
            backtrack(index+1,curOR)
        backtrack(0,0)
        return self.count