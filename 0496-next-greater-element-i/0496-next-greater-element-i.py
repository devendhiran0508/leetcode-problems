class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        nxtGreater={}
        for num in nums2:
            while stack and num>stack[-1]:
                nxtGreater[stack.pop()]=num
            stack.append(num)
        while stack:
            nxtGreater[stack.pop()]=-1
        return [nxtGreater[num] for num in nums1]