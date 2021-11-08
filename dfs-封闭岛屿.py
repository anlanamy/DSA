n=10
maps=[]
visited=[[-1]*n for _ in range(n)]
for i in range(n):
    maps.append(list(input().split(',')))

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def dfs_mark(x,y):
    maps[x][y]='X'
    visited[x][y]=0
    for i in range(4):
        if x+dx[i]>=0 and x+dx[i]<n and y+dy[i]>=0 and y+dy[i]<n:
            if maps[x+dx[i]][y+dy[i]]=='0' and visited[x+dx[i]][y+dy[i]]==-1:
                dfs_mark(x+dx[i],y+dy[i])


count=0
for i in [0,n-1]:
    for j in range(n):
        if maps[i][j]=='0':
            dfs_mark(i,j)
for j in [0,n-1]:
    for i in range(n):
        if maps[i][j]=='0':
            dfs_mark(i,j)
for i in range(n):
    for j in range(n):
        if maps[i][j]=='0':
            dfs_mark(i,j)
            count+=1
print(count)