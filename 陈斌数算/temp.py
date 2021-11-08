N={
    "a":{"b"},   #a
    "b":{"c"},   #b
    "c":{"a","d","g"},   #c
    "d":{"e"},   #d
    "e":{"f"},   #e
    "f":{"d"},   #f
    "g":{"h"},   #g
    "h":{"i"},   #h
    "i":{"g"}    #i
}

def re_tr(G):
    GT = {}
    for u in G:
        for v in G[u]:
            # print(GT)
            if GT.get(v):
                GT[v].add(u)
            else:
                GT[v] = set()
                GT[v].add(u)

    return GT

#递归实现深度优先排序
def rec_dfs(G,s,S=None):
    if S is None:
        #S = set()    #集合存储已经遍历过的节点
        S = list()    #用列表可以更方便查看遍历的次序，而用集合可以方便用difference求差集
    # S.add(s)
    S.append(s)
    print(S)
    for u in G[s]:
        if u in S:continue
        rec_dfs(G,u,S)

    return S

def walk(G,start,S=set()):     #传入的参数S，即上面的seen很关键，这避免了通过连通图之间的路径进行遍历
    P,Q = dict(),set()      #list存放遍历顺序，set存放已经遍历过的节点
    P[start] = None
    Q.add(start)
    while Q:
        u = Q.pop()                      #选择下一个遍历节点（随机性）
        for v in G[u].difference(P,S):         #返回差集
            Q.add(v)
            P[v] = u
    print(P)
    return P

def scc(G):
    GT = re_tr(G)
    sccs,seen = [],set()
    for u in rec_dfs(G,"a"):    #以a为起点
        if u in seen:continue
        C = walk(GT,u,seen)
        seen.update(C)
        sccs.append(C)
    return sccs

print(scc(N))


from pythonds.graphs import PriorityQueue, Graph, Vertex
def dijkstra(aGraph,start):
pq = PriorityQueue()
start.setDistance(0)
pq.buildHeap([(v.getDistance(),v) for v in aGraph])
while not pq.isEmpty():
currentVert = pq.delMin()
for nextVert in currentVert.getConnections():
newDist = currentVert.getDistance() \
+ currentVert.getWeight(nextVert)
if newDist < nextVert.getDistance():
nextVert.setDistance( newDist )
nextVert.setPred(currentVert)
pq.decreaseKey(nextVert,newDist)