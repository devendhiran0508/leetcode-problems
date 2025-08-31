class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        empty=[]

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    empty.append((i,j))
                else:
                    val=board[i][j]
                    row[i].add(val)
                    col[j].add(val)
                    box[(i//3)*3+(j//3)].add(val)

        def backtrack(idx=0):
            if idx==len(empty):
                return True
            i,j=empty[idx]
            b=(i//3)*3+(j//3)
            for d in "123456789":
                if d not in row[i] and d not in col[j] and d not in box[b]:
                    board[i][j]=d
                    row[i].add(d)
                    col[j].add(d)
                    box[b].add(d)
                    if backtrack(idx+1):
                        return True
                    board[i][j]=="."
                    row[i].remove(d)
                    col[j].remove(d)
                    box[b].remove(d)
            return False
        backtrack()
        