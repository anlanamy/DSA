maze=[]  #创建迷宫
visited=[]  #访问过的结点
dis=[]
nx = [[1, 0], [-1, 0], [0, -1], [0, 1]] #移动范围
n,m=map(int,input().split())  #输入行与列
for i in range(n):
    temp = list(map(str, input()))
    maze.append(temp)
dis = [[float('inf') for i in range(m)] for i in range(n)]
for temp in maze:
    if "@" in temp:
        start=(maze.index(temp),temp.index("@"))
    if "*" in temp:
        end = (maze.index(temp), temp.index("*"))
def bfs():
    dis[start[0]][start[1]] = 0
    q = []
    node = (start[0],start[1])
    q.append(node)
    visited.append(node)
    while len(q)>0:
        point = q.pop(0)
        if (point[0] == end[0] and point[1] == end[1]):   #终点位置
            break
        for i in range(4): #下上左右
            dx = point[0] + nx[i][0]
            dy = point[1] + nx[i][1]
            if (0 <= dx < n and 0 <= dy < m and maze[dx][dy] != "#" and (dx,dy) not in visited):
                newPoint = (dx, dy)
                visited.append(newPoint)
                q.append(newPoint)
                dis[dx][dy] = dis[point[0]][point[1]] + 1
if __name__ == '__main__':
    bfs()
    if dis[end[0]][end[1]] != float("inf"):
        print(dis[end[0]][end[1]])
    else:
        print(-1)
