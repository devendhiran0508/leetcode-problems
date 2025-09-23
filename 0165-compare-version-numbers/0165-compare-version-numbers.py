class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        
        n, m = len(v1), len(v2)
        for i in range(max(n, m)):
            num1 = v1[i] if i < n else 0
            num2 = v2[i] if i < m else 0
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0