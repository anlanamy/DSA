s=input()
n=len(s)
dp=[[False]*n for _ in range(n)]
maxL=0
mini=0
for i in range(n):
    dp[i][i]=True
    if i>0:
        dp[i-1][i]=(s[i]==s[i-1])
    if dp[i-1][i]==True:
        maxL=1
        mini=i-1
for i in range(n-2):
    for j in range(0,n-2-i):
        if s[j]==s[j+i+2]:
            dp[j][j+2+i]=dp[j+1][j+i+1]
            if dp[j][j+2+i]==True and i+2>maxL:
                maxL=i+2
                mini=j
print(s[mini:mini+maxL+1])