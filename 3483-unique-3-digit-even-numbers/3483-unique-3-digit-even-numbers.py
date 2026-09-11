class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        avai_count = Counter(digits)
        count = 0

        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            need_count = Counter([d1, d2, d3])

            if all(avai_count[d] >= count for d, count in need_count.items()):
                count += 1
        return count