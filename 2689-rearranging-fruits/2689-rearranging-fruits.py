class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count = Counter(basket1)
        count.subtract(Counter(basket2))

        extra = []
        for fruit, diff in count.items():
            if diff % 2 != 0:
                return -1  
            extra.extend([fruit] * (abs(diff) // 2))

        if not extra:
            return 0

        extra.sort()
        minFruit = min(basket1 + basket2)
        total = 0

        for i in range(len(extra) // 2):
            total += min(extra[i], 2 * minFruit)

        return total