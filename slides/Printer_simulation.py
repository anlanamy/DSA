import sys, os
sys.path.append(os.path.dirname(os.path.abspath('.')))
from ADTstatistics.ADT import Queue
import random
#打印机模拟
class Printer:
    def __init__(self,ppm):
        self.pagerate=ppm  #打印速度
        self.currentTask=None  #打印任务
        self.timeRemaining=0  #任务倒计时
    def tick(self):           #打印1秒
        if self.currentTask!=None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining<=0:
                self.currentTask=None
    def busy(self):
        if self.currentTask!=None:
            return True
        else:
            return False
    def startNext(self,newtask):
        self.currentTask=newtask
        self.timeRemaining=newtask.getPages()*60/self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)
    def getStamp(self):
        return self.timestamp
    def getPages(self):
        return self.pages
    def waitTime(self,currenttime):
        return currenttime-self.timestamp
def newPrintTask():
    num=random.randrange(1,181)
    if num==180:
        return True
    else:
        return False
def simulation(numSeconds,pagesPerMinute):
    labprinter=Printer(pagesPerMinute)
    printQueue=Queue()
    waitingtimes=[]
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task=Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask=printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." %(averageWait,printQueue.size()))

for i in range(10):
    simulation(3600,5)




