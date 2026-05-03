class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix_rows = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                self.prefix_rows[r][c] = prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0

        for r in range(row1, row2 + 1):
            if col1 > 0:
                res += self.prefix_rows[r][col2] - self.prefix_rows[r][col1 - 1]
            else:
                res += self.prefix_rows[r][col2]
        
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)