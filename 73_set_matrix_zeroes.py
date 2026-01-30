class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zero_rows = []
        zero_cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.append(i)
                    zero_cols.append(j)
        
        for i in range(len(matrix)):
            if i in zero_rows:
                matrix[i] = [0 for j in range(len(matrix[i]))]
                continue
            for j in range(len(matrix[0])):
                if j in zero_cols:
                    matrix[i][j] = 0
                    
# Example usage:
sol = Solution()
matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
sol.setZeroes(matrix1)
print(matrix1)  # Output: [[1,0,1],[0,0,0],[1,0,1]] 

matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol.setZeroes(matrix2)
print(matrix2)  # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]