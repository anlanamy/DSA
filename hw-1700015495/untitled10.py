class Queue:
    def __init__(self):
        self.lst = []
        self.head = 0 
    def push(self, obj):
        self.lst.append(obj) 
    def pop(self):
        self.head += 1 
    def top(self):
        return self.lst[self.head] 
    def empty(self):
        return (self.head >= len(self.lst)) 
class Pos:
    def __init__(self, x, y): 
        self.x = x
        self.y = y
n = int(input())
maps = [None for i in range(n)] #存储地图 
for i in range(n):
    string = list(input()) 
    maps[i] = string
visit = [[-1 for i in range(n)] for j in range(n)] #存储距离，未访 问则为-1
queue = Queue()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dfs_mark(x, y): #选择一座岛屿作为起点并标记为“X” 
    maps[x][y] = 'X'
    visit[x][y] = 0
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if newx < n and newx >= 0 and newy < n and newy >= 0:
            if maps[newx][newy]=='1' and visit[newx][newy]==-1:
                dfs_mark(newx, newy)
            elif maps[newx][newy] == '0' and visit[newx][newy] == -1: 
                queue.push(Pos(newx,newy))
                visit[newx][newy] = 1 #与起点距离为1的点进入搜索队列
           
breakflag = 0
for i in range(n): 
    for j in range(n):
        if maps[i][j] == '1': 
            dfs_mark(i, j) 
            breakflag = 1 
            break
    if breakflag: 
        break
breakflag = 0
while not queue.empty(): #从距离为1的点开始计算距离，使用队列进行广度优先搜索
    tmp = queue.top() 
    x = tmp.x
    y = tmp.y 
    queue.pop()
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if newx < n and newx >= 0 and newy < n and newy >= 0 and visit[newx][newy] == -1: 
            queue.push(Pos(newx, newy))
            visit[newx][newy] = visit[x][y] + 1 
            if(maps[newx][newy] == '1'):
                print(visit[newx][newy] - 1) 
                breakflag = 1
                break
    if breakflag: 
        break