class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        row = len(matrix)
        column = len(matrix[0])
        ra = set()
        ca = set()
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0:
                    ra.add(i)
                    ca.add(j)
        
        for i in ra:
            for j in range(column):
                matrix[i][j] = 0

        for i in ca:
            for j in range(row):
                matrix[j][i] = 0
        # def fixrowzeros(r,n):
        #     for i in range(n):
        #         if matrix[r][i] != 0: 
        #             matrix[r][i] = -1
        
        # def fixcolzeros(c,n):
        #     for i in range(n):
        #         if matrix[i][c] != 0: 
        #             matrix[i][c] = -1
        
        # for i in range(row):
        #     for j in range(column):
        #         if matrix[i][j] == 0:
        #             fixrowzeros(i,column)
        #             fixcolzeros(j,row)
        # for i in range(row):
        #     for j in range(column):
        #         if matrix[i][j] == -1 :
        #             matrix[i][j] = 0
        return matrix