class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        i = 0
        for line in board:
            if 'R' in line:
                j = line.index('R')
                break
            i += 1
        # print(i, j)
        res = 0
        x, y = i, j
        while True:
            x -= 1
            if x == -1:
                break
            if board[x][y] == 'p':
                res += 1
                break
            elif board[x][y] == 'B':
                break
        x, y = i, j
        while True:
            x += 1
            if x == 8:
                break
            if board[x][y] == 'p':
                res += 1
                break
            elif board[x][y] == 'B':
                break
        x, y = i, j
        while True:
            y -= 1
            if y == -1:
                break
            if board[x][y] == 'p':
                res += 1
                break
            elif board[x][y] == 'B':
                break
        x, y = i, j
        while True:
            y += 1
            if y == 8:
                break
            if board[x][y] == 'p':
                res += 1
                break
            elif board[x][y] == 'B':
                break
        return res
