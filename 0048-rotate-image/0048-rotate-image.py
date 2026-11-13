class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ni = len(matrix)
        nj = len(matrix[0]) - 1
        mat2 = []
        for i in range(ni):
            temp = []
            for j in range(nj,-1,-1):
                temp.append(matrix[j][i])
            mat2.append(temp)
        matrix[:] = mat2[:]
        return matrix
        