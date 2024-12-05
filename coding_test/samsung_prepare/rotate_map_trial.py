board = [[1,2,3,4],[4,5,6,7],[7,8,9,10],[90,80,70,60]]

def show_board(b):
    print('---------')
    for r in b:
        for s in r:
            print(s,end=' ')
        print('')

def rotate_90(b):
    n,m = len(b),len(b[0])
    temp_board = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp_board[m-j-1][i] = b[i][j]
    return temp_board

def rotate_180(b):
    n,m = len(b),len(b[0])
    temp_board = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp_board[n-i-1][m-j-1] = b[i][j]
    return temp_board

def rotate_270(b):
    n,m = len(b),len(b[0])
    temp_board = [[-1 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp_board[j][n-i-1] = b[i][j]
    return temp_board

show_board(rotate_90(board))
show_board(rotate_180(board))
show_board(rotate_270(board))

