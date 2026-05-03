class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.mat_sum = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.mat_sum[r][c + 1]
                self.mat_sum[r + 1][c + 1] += prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1

        bottomLeft = self.mat_sum[row2][col2]
        top = self.mat_sum[row1 - 1][col2]
        left = self.mat_sum[row2][col1 - 1]
        topLeft = self.mat_sum[row1 - 1][col1 - 1]

        return bottomLeft - top - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
