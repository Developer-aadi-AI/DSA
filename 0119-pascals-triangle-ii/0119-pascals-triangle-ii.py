class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        pascal = []
        for i in range(rowIndex + 1):
            elem = []
            for j in range(i+1):
                if j == i or j == 0:
                    elem.append(1)
                else:
                    elem.append(pascal[i-1][j-1] + pascal[i-1][j])
            pascal.append(elem)
        return pascal[rowIndex]