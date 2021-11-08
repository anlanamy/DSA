l=input()
count=[0,0]
output=0
turn=int(l[0])
if len(l)>1:
    count[turn]+=1
    for i in range(1,len(l)):
        if l[i]==l[i-1]:
            count[turn]+=1
        else:
            output+=min(count[0],count[1])
            turn=(turn+1)%2
            count[turn]=1
    output+=min(count[0],count[1])
print(output)