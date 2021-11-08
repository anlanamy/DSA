l=input()
count=0
output=[]
for i in l:
    count=count*2+int(i)
    if count%5==0:
        output.append(1)
    else:
        output.append(0)
print(''.join([str(x) for x in output]))