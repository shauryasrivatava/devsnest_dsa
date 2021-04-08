lass Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # ans=[]
        # res=[]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix)-1,-1,-1):
        #         ans.append(matrix[j][i])
        #     res.append(ans)
        #     ans=[]
        # print(res)
        # matrix=res
        
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):   
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        for i in range(n):
            for j in range(0,int(n/2)):
                temp=matrix[i][j]
                matrix[i][j]=matrix[i][n-1-j]
                matrix[i][n-1-j]=temp
       
        
