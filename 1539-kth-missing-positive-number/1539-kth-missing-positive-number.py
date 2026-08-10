class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 0
        high = len(arr) - 1
        res = len(arr) + k

        while low <= high:
            mid = low + (high - low) // 2
            if(arr[mid] > mid + k):
                res = mid + k
                high = mid - 1
            else:
                low = mid + 1
        return res