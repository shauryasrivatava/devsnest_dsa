class Solution(object):
    def exist(self, board, word):
        n=len(board)
        m=len(board[0])
        for i in range(n):
            for j in range(m):
                if word[0]==board[i][j] and self.kuchbhi(board,word,i,j):
                        return True
        return False            
    def kuchbhi(self,board,word,n,m,i=0):
        if len(word)==i:
            return True
        if n>=len(board) or n<0 or m>=len(board[0]) or m<0 or word[i]!=board[n][m]:
            return False
        board[n][m]='*' 
        
        res = self.kuchbhi(board,word,n+1,m,i+1) or self.kuchbhi(board,word,n-1,m,i+1) or self.kuchbhi(board,word,n,m+1,i+1) or self.kuchbhi(board,word,n,m-1,i+1)
        board[n][m] = word[i]
        return res
