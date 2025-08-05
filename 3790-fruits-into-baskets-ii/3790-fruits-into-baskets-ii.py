class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count=0
        n=len(baskets)
        for fruit in fruits:
            a=1
            for i in range(n):
                if fruit<=baskets[i]:
                    baskets[i]=0
                    a=0
                    break
            count+=a
        return count