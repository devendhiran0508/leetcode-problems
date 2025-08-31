class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        # Fill initial state
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empties.append((i, j))
                else:
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)

        def backtrack(idx=0):
            if idx == len(empties):
                return True  # solved

            i, j = empties[idx]
            b = (i // 3) * 3 + (j // 3)

            for d in "123456789":
                if d not in rows[i] and d not in cols[j] and d not in boxes[b]:
                    # place digit
                    board[i][j] = d
                    rows[i].add(d)
                    cols[j].add(d)
                    boxes[b].add(d)

                    if backtrack(idx + 1):
                        return True

                    # undo
                    board[i][j] = "."
                    rows[i].remove(d)
                    cols[j].remove(d)
                    boxes[b].remove(d)

            return False

        backtrack()
