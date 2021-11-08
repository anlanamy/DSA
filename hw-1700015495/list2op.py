#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:06:12 2021

@author: anlanamy
"""

import timeit
import random
import matplotlib.pyplot as plt  

mini,maxi,step=map(int,input('输入N的参数，最小值，最大值，步长，用空格分隔：').split())
Nlist=[]
subscripttime=[]
indextime=[]
for i in range(mini, maxi+1,step):
    Nlist.append(i)
    mylist=list(range(i))    
    t1 = timeit.Timer("mylist[random.randrange({})]".format(i),"from __main__ import random, mylist")
    subscripttime.append(t1.timeit(1000))
    t2 = timeit.Timer("mylist.index(random.randrange({}))".format(i),"from __main__ import random, mylist")
    indextime.append(t2.timeit(1000))


plt.plot(Nlist, subscripttime, color='red', linestyle='-', linewidth=2.5, label='subscript time')
plt.plot(Nlist, indextime, color='blue', linestyle='-', linewidth=2.5, label='index time')
plt.xlabel('N')
plt.ylabel('Execution Time')
plt.title('Two way of indexing elements in a list')
plt.legend()
plt.show()