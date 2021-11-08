l=[int(x) for x in input().split()]
n=len(l)
dp=[[l[-1],n-1]]
location=list(range(n))
output=[]
for i in range(n-1):
    if l[n-2-i]>l[n-1-i]:
        location[n-2-i]=n-1-i
        dp.append([l[n-2-i],n-2-i])
    else:
        while dp and dp[-1][0]>=l[n-2-i]:
            dp.pop()
        if dp:
            location[n-2-i]=dp[-1][1]
        else:
            location[n-2-i]=n-2-i
        dp.append([l[n-2-i],n-2-i])
for i in range(n):
    output.append(location[i]-i if location[i]-i>0 else -1)
print(' '.join([str(x) for x in output]))