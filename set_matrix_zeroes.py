class Solution(object):
    def setZeroes(self, mat):
        n=len(mat)
        m=len(mat[0])
        row=set()
        col=set()
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]==0:
                    row.add(i)
                    col.add(j)
                    
        for i in row:
            for j in range(m):
                mat[i][j]=0
        for i in col:
            for j in range(n):
                mat[j][i]=0
        return mat
