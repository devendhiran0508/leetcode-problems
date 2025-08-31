class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(90)]
        cols=[set() for _ in range(9)]
        box=[set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val=='.':
                    continue
                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                boxIndex=(r//3)*3+(c//3)
                if val in box[boxIndex]:
                    return False
                box[boxIndex].add(val)
        return True
        