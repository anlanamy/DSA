#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 10:14:43 2021

@author: anlanamy
"""

#from pythonds.basic.queue import Queue
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item) #0为队尾
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    
def radixsort(sortlist):
    l=[]
    main=sortlist
    j=0
    for i in range(10):
        l.append(Queue())
    remain=[]
    while len(remain)<len(main):
        remain=[]
        for i in main:
            if i>=(10**j):
                l[i//(10**j)%10].enqueue(i)
            else:
                remain.append(i)
        main=remain[:]
        for i in range(10):
            while not l[i].isEmpty():
                main.append(l[i].dequeue())    
        j+=1
    return [str(x) for x in main]

print(' '.join(radixsort([int(x) for x in input().split()])))