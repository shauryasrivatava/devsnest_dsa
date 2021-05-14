class Solution:
    def dfs(self,i,j,r,c,board):
        if i<0 or i>r-1 or j<0 or j>c-1 or board[i][j]=='X' or board[i][j]=='z':
            return;
        # if board[i][j]=='O' and i>=0 and j>=0 and i<r and j<c:
            
        # print("spiderman")
        board[i][j]='z'
        self.dfs(i+1,j,r,c,board)
        self.dfs(i-1,j,r,c,board)
        self.dfs(i,j+1,r,c,board)
        self.dfs(i,j-1,r,c,board)
            
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r=len(board)
        if r<=2:
            return board
        c=len(board[0])
        if c<=2:
            return board
        for i in range(r):
            for j in range(c):
                if board[i][j]=='O' and(i==0 or j==0 or i==r-1 or j==c-1):
                    # print("superman")
                    self.dfs(i,j,r,c,board)
        for i in range(r):
            for j in range(c):
                if board[i][j]=='z':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
