class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        ans = []

        for d in range(m + n - 1):
            diagonal = []
            row = 0 if d < n else d - n + 1
            col = d if d < n else n - 1

            while row < m and col >= 0:
                diagonal.append(mat[row][col])
                row += 1
                col -= 1

            if d % 2 == 0:
                ans.extend(reversed(diagonal))
            else:
                ans.extend(diagonal)

        return ans