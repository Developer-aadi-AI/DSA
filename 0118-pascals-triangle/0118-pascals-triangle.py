class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal = []
        for i in range(0,numRows):
            elem = []
            for j in range(i+1):
                if j == i or j == 0:
                    elem.append(1)
                else:
                    el = pascal[i-1][j-1]+pascal[i-1][j]
                    elem.append(el)
            pascal.append(elem)
        
        return pascal