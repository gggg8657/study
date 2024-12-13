
arr = [0,1,2,3,4]
visit = [False for _ in range(len(arr))]
n = 2

def DFS_comb(arr, x, path, result, n):
    if len(path)== n:
        result.append(path[:])
        return
    for i in range(x,len(arr)):
        path.append(arr[i])
        DFS_comb(arr, i+1, path, result, n)
        path.pop()

result = []
path = []
x = 0
DFS_comb(arr,x,path,result,3)

print(result)

arr =[ [2,0,0,0,0,0],
       [0,1,0,1,1,0],
       [-1,1,0,0,0,1],
       [0,0,1,0,-1,3],
       [0,0,1,0,-1,0],
       [0,0,0,0,0,0]]

def DFS(arr, x, y, visit, PATHS, all_paths):
    rows, cols = len(arr), len(arr[0])

    if x<0 or y<0 or x>=rows or y>=cols:
        return
    elif arr[x][y]==1 or arr[x][y]==-1:
        return
    elif visit[x][y]:
        return

    PATHS.append((x,y))

    if arr[x][y]==3:
        all_paths.append(PATHS[:])
        PATHS.pop()
        return

    visit[x][y]=True

    d = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        DFS(arr, nx,ny, visit, PATHS, all_paths)

    # Backtrack: Unmark the cell and remove from path
    visit[x][y]=False
    PATHS.pop()


for row in range(len(arr)):
    for col in range(len(arr[row])):
        if arr[row][col] == 2:
            x,y = row,col
            break

visit = [[False for _ in range(len(arr[0]))]for _ in range(len(arr))]
PATHS = []
all_paths=[]
DFS(arr, x, y, visit, PATHS, all_paths)

for path in all_paths:
    print("->".join(map(str,path)))