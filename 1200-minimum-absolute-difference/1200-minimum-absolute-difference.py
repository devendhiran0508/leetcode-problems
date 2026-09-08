class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res = []
        n = len(arr)
        arr.sort()
        minAbsDiff = float('inf')
        for i in range(n - 1):
            diff = abs(arr[i] - arr[i + 1])
            if diff < minAbsDiff:
                minAbsDiff = diff
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            if diff == minAbsDiff:
                res.append([arr[i], arr[i + 1]])
        return res