n=int(input())
maps=[]
ans=float('inf')
for i in range(n):
    maps.append(list(input()))
visit=[[float('inf')]*(n+2) for _ in range(n+2)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs_mark(x, y): #选择一座岛屿作为起点并标记为“X” 
    if maps[x][y]!='1':
        return    
    maps[x][y] = 'X'
    visit[x+1][y+1] = 0
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if newx < n and newx >= 0 and newy < n and newy >= 0:
            dfs_mark(newx, newy)

def dfs_found(x,y):
    global ans
    distance=min(visit[x+1][y],visit[x][y+1],visit[x+1][y+2],visit[x+2][y+1])
    if maps[x][y]=='1'and visit[x+1][y+1]>distance+1:
        visit[x+1][y+1]=distance+1
        ans=min(ans,distance)
        return
    elif maps[x][y]=='0' and (visit[x+1][y+1]==float('inf') or visit[x+1][y+1]>distance+1):
        visit[x+1][y+1]=distance+1
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if newx < n and newx >= 0 and newy < n and newy >= 0:
                dfs_found(newx, newy)
    else:
        return


flag=True    
for i in range(0,n):
    for j in range(0,n):
        if maps[i][j]=='1':
            dfs_mark(i,j)
            flag=False
            break
    if not flag:
        break
flag=True    
for i in range(0,n):
    for j in range(0,n):
        if maps[i][j]=='0':
            dfs_found(i,j)
            flag=False
            break
    if not flag:
        break

print(ans)