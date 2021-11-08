# coding=utf-8

#建立图
class Vertex: #点
    def __init__(self,key):
        self.id = key#点有名字key
        self.connectedTo = {}
        self.filmacted=[]
    def addfilm(self,film):
        self.filmacted.append(film)
    def addNeighbor(self,nbr,film,weight=1):
        if nbr in self.connectedTo and self.connectedTo[nbr][1] !=None:
            togetherfilm = self.connectedTo[nbr][1].append(film)
            self.connectedTo[nbr] = (weight, togetherfilm)
        else:
            togetherfilm = [film]
            self.connectedTo[nbr] = (weight, togetherfilm)
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self,n):
        return n in self.vertList
    def addEdge(self,f,t,film,cost=1):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],film,cost)
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())


import json
# 读取json文件内容,返回字典格式
with open('C:\\Users\\nyh\\Desktop\\Film.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)

def buildGraph(data):
    g = Graph()
    for film in json_data:
        actorstrthisfilm = film['actor']
        actorlstthisfilm = [x for x in actorstrthisfilm.split(",")]
        for actor1 in actorlstthisfilm:
            if actor1 not in g.vertList:
                nv=g.addVertex(actor1)
            g.vertList[actor1].addfilm(film)
            for actor2 in actorlstthisfilm:
                if actor1 != actor2:
                    g.addEdge(actor1,actor2,film)
    return g

mygraph=buildGraph(json_data)

'''
#强连通分支个数

def re_tr(G):
    GT = Graph()
    for u in G:
        for v in u.connectedTo:
            # print(GT)
            GT.addEdge(v,u,None)
    return GT

#递归实现深度优先排序
def rec_dfs(G,s,S=None):
    if S is None:
        #S = set()    #集合存储已经遍历过的节点
        S = list()    #用列表可以更方便查看遍历的次序，而用集合可以方便用difference求差集
    # S.add(s)
    S.append(s)
    print(S)
    temp=temp.connectedTo.keys()
    for u in temp:
        if u in S:continue
        rec_dfs(G,u,S)

    return S

#遍历有向图的强连通分量
def walk(G,start,S=set()):     #传入的参数S，即上面的seen很关键，这避免了通过连通图之间的路径进行遍历
    P,Q = dict(),set()      #list存放遍历顺序，set存放已经遍历过的节点
    P[start] = None
    Q.add(start)
    while Q:
        u = Q.pop()                      #选择下一个遍历节点（随机性）
        for v in G.vertList[u].difference(P,S):         #返回差集
            Q.add(v)
            P[v] = u
    print(P)
    return P


#获得各个强连通图
def scc(G):
    GT = re_tr(G)
    sccs,seen = [],set()
    for u in rec_dfs(G,mygraph.vertList['林更新']):    #以林更新为起点
        if u in seen:continue
        C = walk(GT,u,seen)
        seen.update(C)
        sccs.append(C)
    return sccs


print(scc(mygraph))

#scc打印出来最后一行就是了


#求直径
from pythonds.graphs import PriorityQueue, Graph, Vertex
def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)
'''



zhoulst=mygraph.vertList['林更新']
zhoulst=zhoulst.connectedTo
print(len(zhoulst)+1)#302
zhoufilm=mygraph.vertList['林更新'].filmacted
for ren in zhoulst:
    zhoufilm+=ren.filmacted
print(len(zhoufilm))

lst=mygraph.vertList
zhoulst=mygraph.vertList['周星驰']
zhoulst=zhoulst.connectedTo
print(len(zhoulst)+1)#302
zhoufilm=mygraph.vertList['周星驰'].filmacted
for ren in zhoulst:
    zhoufilm+=ren.filmacted
print(len(zhoufilm))


leilst={}
for f in zhoufilm:
    for i in f[3]:
        if i not in leilst:
            leilst[i]=1
        else:leilst[i]+=1
leilst.sort(key=lambda x : x[1])
print(leilst)


