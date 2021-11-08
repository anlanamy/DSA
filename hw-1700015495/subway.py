#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:02:20 2021

@author: anlanamy
"""


#from pythonds.basic.queue import Queue
import random
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
    def head(self):
        return self.items[-1]
    

#西二旗地铁站乘客平均等车时间和站内人数模型
class Train:
    def __init__(self,capacity,intervals):   #capacity是一辆列车的载荷，intervals是列车的发车间隙
        self.capacity=capacity  #运力
        #self.currentWait=None  #初始情况默认地铁站没有人
        self.timeRemaining=intervals  #初始情况是车还没有发车
    def tick(self,intervals):           #计时器
        if self.timeRemaining>0:
            self.timeRemaining=self.timeRemaining-1
        else:
            self.timeRemaining=intervals #到站后将列车等待时间初始化
    def isDeparture(self,intervals):
        return self.timeRemaining==intervals 


class People:    #定义乘客的性质
    def __init__(self,time):
        self.timestamp=time
    def getStamp(self):
        return self.timestamp
    def getVolume(self):
        return self.volume
    def waitTime(self,currenttime):     #记录乘客在车站内的逗留时间，对于等待上车的人是等待时间，对于下车的人是出站的时间
        return currenttime-self.timestamp

def newPeople(rate):    #对于上车的人来说rate的定义是平均新来一位乘客的秒数，因此rate越小客流量越大；
    num=random.randrange(1,rate+1)
    if num==rate:
        return True
    else:
        return False


def simulation(numSeconds,capacity,intervals,inrate,outpassenger,outrate):
    train=Train(capacity,intervals)
    inpeopleQueue=Queue()
    outpeopleQueue=Queue()
    waitingtimes=[]    #平均等待时间
    currentVolumeList=[]     #目前地铁站人数
    currentvolume=0
    for currentSecond in range(numSeconds):
        outvolume=0 
        if newPeople(inrate):   #新乘客进站
            inpeople=People(currentSecond)
            inpeopleQueue.enqueue(inpeople)
            involume=1
        else:
            involume=0
        if train.isDeparture(intervals):    #列车到站
            if capacity<inpeopleQueue.size(): #如果现有的等待人数超过了列车的载荷
                for i in range(capacity):
                    nextpeople=inpeopleQueue.dequeue()
                    waitingtimes.append(nextpeople.waitTime(currentSecond))
                    outvolume+=1
            else: #如果现有等待人数小于列车的载荷
                while not inpeopleQueue.isEmpty():
                    nextpeople=inpeopleQueue.dequeue()
                    waitingtimes.append(nextpeople.waitTime(currentSecond))
                    outvolume+=1
            outpeople=People(currentSecond)   #每一趟列车的出站人
            outpeopleQueue.enqueue(outpeople)
            involume+=outpassenger      #假定每一趟列车出站人数是给定的
        if not outpeopleQueue.isEmpty() and outpeopleQueue.head().waitTime==outrate: #outrate对于下车的人来说是出站所需要的秒数
            outpeopleQueue.dequeue()     #达到所设定的出站速度，出队列
            outvolume+=outpassenger    
        currentvolume=currentvolume+involume-outvolume
        currentVolumeList.append(currentvolume)


        train.tick(intervals)

    averageWait=sum(waitingtimes)/len(waitingtimes)
    averageVolume=sum(currentVolumeList)/len(currentVolumeList)
    print('======simulation of intervals= %3d, inrate= %3d '%(intervals,inrate))
    print("Average Wait %6.2f secs %3d people remaining." %(averageWait,currentvolume))
    print("Average %3d people in the station." %(averageVolume))

for i in range(10):    #人流量大的模拟
    simulation(3600,30,120,2,10,3)
    
for i in range(10):   #人流量小的模拟
    simulation(3600,30,120,10,10,3)
    
for i in range(10):    #列车间隔变小的模拟
    simulation(3600,30,90,2,7,3)  

'''  
附加题思路：在更改13号线方向之后，车站变成6个方向，因此interval可以相应减少,每一趟列车的出站人也相应减少，情况类似于（1）和（3）的对比,
即平均等待时间变短，车站内平均滞留人数也减少
'''