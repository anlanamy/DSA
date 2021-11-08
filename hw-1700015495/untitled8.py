l=input()
t=[0,0]
turn=[1,0]
turnNumber=0
direction=[[1,0],[0,-1],[-1,0],[0,1]]
for i in l:
    if i=='G':
        t[0]+=turn[0]
        t[1]+=turn[1]
    elif i=='L':
        turnNumber=(turnNumber-1)%4
        turn=direction[turnNumber]
    else:
        turnNumber=(turnNumber+1)%4
        turn=direction[turnNumber]
print(0 if t!=[0,0] and turn==[1,0] else 1)