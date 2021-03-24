class Solution(object):
    def spiralOrder(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        output=[]
        top=0
        down=m-1
        left=0
        right=n-1
        direction=0
        while top<=down and left<=right :
            if(direction==0):
                for i in range(left,right+1):
                    output.append(matrix[top][i])
                # right -=1
                top+=1
            if(direction==1):
                for i in range(top,down+1):
                    output.append(matrix[i][right])
                right-=1
            if(direction==2):
                for i in range(right,left-1,-1):
                    output.append(matrix[down][i])
                down-=1
            if(direction==3):
                for i in range(down,top-1,-1):
                    output.append(matrix[i][left])
                left+=1
            direction=(direction+1)%4    
        return output
