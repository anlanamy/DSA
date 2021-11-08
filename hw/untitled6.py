m,n=map(int,input().split())
l=[input() for _ in range(m)]
output=[[0]*(n+1) for _ in range(m+1)]
count=0
for i in range(1,m+1):
    for j in range(1,n+1):
        if l[i-1][j-1]=='1':
            output[i][j]=min(output[i][j-1],output[i-1][j],output[i-1][j-1])+1
            count+=output[i][j]
        else:
            output[i][j]=0
print(count)