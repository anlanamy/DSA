#1.验证list的按索引取值确实是O(1)
import random
from timeit import Timer
for i in range(20000,1000001,20000):
    t=Timer("a=thelist[x]", "from __main__ import thelist,x")
    thelist=list(range(i))
    x=random.randint(0,i-1)
    thetime=t.timeit(number=1000)
    print("%d,%f"%(i,thetime))

#2.验证dict的set item和get item都是O(1)的
import random
from timeit import Timer
for i in range(20000,1000001,20000):
    t1=Timer("thedict[x]=0", "from __main__ import thedict,x")
    t2=Timer("b= thedict[y]", "from __main__ import thedict,y")
    thedict={j:None for j in range(i)}
    x = random.randint(0, i - 1)
    y = random.randint(0, i - 1)
    thetimeset=t1.timeit(number=1000)
    thetimeget=t2.timeit(number=1000)
    print("%d,%f,%f"%(i,thetimeset,thetimeget))

#3.做计时实验，比较list和dict的del操作符性能
import random
from timeit import Timer
for i in range(2000,1000001,2000):
    t1=Timer("del thelist[x]", "from __main__ import thelist,x")
    t2=Timer("del thedict[random.randint(0, int(i-1001))]", "from __main__ import thedict,random,i")
    thelist=list(range(i))
    thedict = {j: None for j in range(i)}
    x = random.randint(0, int(i- 1001))
    thetimeldel=t1.timeit(number=10)
    thetimeddel=t2.timeit(number=10)
    print("%d,%f,%f" % (i, thetimeldel, thetimeddel))

#4.对一些随机数列表排序，验证Python自带的list.sort的时间复杂度为O(n logn)
import random
from timeit import Timer
for i in range(20,100001,20):
    t=Timer("thelist[:].sort()", "from __main__ import thelist")
    thelist= [random.randrange(10**6) for n in range(i)]
    thetimesort=t.timeit(number=10)
    print("%d,%f"%(i,thetimesort))
