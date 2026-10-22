class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        result = []

        for j in range(cols):
            row = []
            for i in range(rows):
                row.append(matrix[i][j])
            result.append(row)
        
        return result