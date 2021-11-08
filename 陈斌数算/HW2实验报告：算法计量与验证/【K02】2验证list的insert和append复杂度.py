#1.验证向一个列表添加数据项的两种方法，复杂度对比
from timeit import Timer
print("i,thetimeins,thetimeapp")
for i in range(100000,1000001,100000):
    t1=Timer("thelist1.insert(0, None)", "from __main__ import thelist1")
    t2=Timer("thelist2.append(None)", "from __main__ import thelist2")
    thelist1=list(range(i))
    thelist2=list(range(i))
    thetimeins=t1.timeit(number=1000)
    thetimeapp=t2.timeit(number=1000)
    thelist1.pop(0)
    thelist2.pop()
    print("%d,%f,%f"%(i,thetimeins,thetimeapp))