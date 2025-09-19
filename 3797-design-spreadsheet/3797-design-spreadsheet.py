class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula: str) -> int:
        expr = formula[1:]  
        left, right = expr.split("+")
        return self._getValue(left) + self._getValue(right)

    def _getValue(self, token: str) -> int:
        if token[0].isdigit():   
            return int(token)
        return self.cells.get(token, 0)  


# Example usage:
# obj = Spreadsheet(3)
# obj.setCell("A1", 10)
# obj.setCell("B2", 25)
# print(obj.getValue("=A1+B2"))  # 35
# obj.resetCell("A1")
# print(obj.getValue("=A1+B2"))  # 25
