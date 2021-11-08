#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 22:33:09 2021

@author: anlanamy
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 09:40:19 2021

@author: anlanamy
"""

class Node:
    def __init__(self,initdata=None):
        self.data=initdata
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data=newdata
    def setNext(self,newnext):
        self.next=newnext
    def __str__(self):
        return str(self.data)

class UnorderedList:
    def __init__(self):
        self.head=None
        
    def isEmpty(self):
        return self.head==None
    
    def add(self,item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp
        return self
        
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    
    def search(self,item):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
        return found
    
    def append(self,item):
        temp=Node(item)
        current=self.head
        if self.head==None:
            temp.setNext(None)
            self.head=temp
        else:
            while current.getNext()!=None:
                current=current.getNext()
            current.setNext(temp)
            temp.setNext(None)
        return self
            
    def index(self,item):
        current=self.head
        found=False
        count=0
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
                count+=1
        return count
    
    def pop(self,pos=None):
        current=self.head
        previous=None
        count=0
        if pos==None:
            if current.getNext()!=None:
                while current.getNext()!=None:
                    previous=current
                    current=current.getNext()
                previous.setNext(None)
            else:
                self.head=None
        elif pos==0:
            if current.getNext()!=None:
                self.head=current.getNext()
            else:
                self.head=None
        else:
            while count!=pos:
                previous=current
                current=current.getNext()
                count+=1
            previous.setNext(current.getNext())
        return current
    
    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while current!=None and not found:
            if current.getData()==item:
               break
            else:
                previous=current
                current=current.getNext()
        if previous!=None:
            previous.setNext(current.getNext())
        else:
            self.head=None           
        return self
    
    def insert(self,pos,item):
        temp=Node(item)
        current=self.head
        if self.head==None:
            temp.setNext(None)
            self.head=temp
        elif pos==0:
            self.head=temp
            temp.setNext(current)
        else:
            previous=None
            count=0
            while count!=pos:
                previous=current
                current=current.getNext()
                count+=1
            previous.setNext(temp)
            temp.setNext(current)
        return self
            
    def __str__(self):
        current=self.head
        out=[]
        while current!=None:
            out.append(current)
            current=current.getNext()
        return ' '.join([str(x) for x in out])
    __repr__=__str__
    
    def __getitem__(self,pos):
        current=self.head
        count=0
        while count!=pos:
            current=current.getNext()
            count+=1
        return current
    
class OrderedList(UnorderedList):
    def add(self,item):
        current=self.head
        previous=None
        while current!=None:
            if current.getData()>item:
                break
            previous=current
            current=current.getNext()
        temp=Node(item)
        if previous==None:
            temp.setNext(self.head)
            self.head=temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        return self

    def search(self,item):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getData()==item:
                found=True
            elif current.getData()>item:
                break
            else:
                current=current.getNext()
        return found    

class Queue:
    def __init__(self):
        self.head=None
        
    def isEmpty(self):
        return self.head==None
    
    def enqueue(self,item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp
        return self
    
    def dequeue(self):
        current=self.head
        previous=None
        while current.getNext()!=None:
            previous=current
            current=current.getNext()
        if previous!=None:
            previous.setNext(None)
        else:
            self.head=None
        return current
    
    def peek(self):
        current=self.head
        while current.getNext()!=None:
            current=current.getNext()
        return current if current else 'Stack is Empty!'
        
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count    

    def __str__(self):
        current=self.head
        out=[]
        while current!=None:
            out.append(current)
            current=current.getNext()
        return ' '.join([str(x) for x in out])
    __repr__=__str__    
    
    
class Stack:
    def __init__(self):
        self.head=None
        
    def isEmpty(self):
        return self.head==None
    
    def push(self,item):
        temp=Node(item)
        current=self.head
        if self.head==None:
            temp.setNext(None)
            self.head=temp
        else:
            while current.getNext()!=None:
                current=current.getNext()
            current.setNext(temp)
            temp.setNext(None)
    
    def pop(self):
        current=self.head
        previous=None
        while current.getNext()!=None:
            previous=current
            current=current.getNext()
        if previous!=None:
            previous.setNext(None)
        else:
            self.head=None
        return current
    
    def peek(self):
        current=self.head
        while current.getNext()!=None:
            current=current.getNext()
        return current if current else 'Stack is Empty!'
        
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count    

    def __str__(self):
        current=self.head
        out=[]
        while current!=None:
            out.append(current)
            current=current.getNext()
        return ' '.join([str(x) for x in out])
    __repr__=__str__  
    
class biNode:
    def __init__(self,initdata=None):
        self.data=initdata
        self.next=None
        self.prev=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev
    def setData(self,newdata):
        self.data=newdata
    def setNext(self,newnext):
        self.next=newnext
    def setPrev(self,newnext):
        self.prev=newnext
    def __str__(self):
        return str(self.data)

class biUnorderedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def isEmpty(self):
        return self.head==None
    
    def add(self,item):
        temp=biNode(item)
        current=self.head
        if current==None:
            self.tail=temp
        else:
            current.setPrev(temp)
        temp.setPrev(None)
        temp.setNext(current)
        self.head=temp
        return self
        
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    
    def search(self,item):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
        return found
    
    def append(self,item):
        temp=biNode(item)
        if self.tail==None:
            temp.setNext(None)
            temp.setPrev(None)
            self.head=temp
            self.tail=temp
        else:
            temp.setPrev(self.tail)
            self.tail.setNext(temp)
            temp.setNext(None)
            self.tail=temp
        return self
            
    def index(self,item):
        current=self.head
        found=False
        count=0
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
                count+=1
        return count
    
    def pop(self,pos=None):
        current=self.head
        previous=None
        count=0
        if pos==None:
            if current.getNext()!=None:
                current=self.tail
                previous=current.getPrev()
                previous.setNext(None)
                self.tail=previous
            else:
                self.head=None
                self.tail=None
        elif pos==0:
            if current.getNext()!=None:
                self.head=current.getNext()
                current.getNext().setPrev(None)
            else:
                self.head=None
                self.tail=None    
        else:
            while count!=pos:
                previous=current
                current=current.getNext()
                count+=1
            if current.getNext()==None:
                self.tail=previous
            else:
                current.getNext().setPrev(previous)
            previous.setNext(current.getNext())
        return current
    
    def remove(self,item):
        current=self.head
        previous=None
        if self.tail==item:
            if current.getNext()!=None:
                previous=self.tail.getPrev()
                previous.setNext(None)
                self.tail=previous
            else:
                self.head=None
                self.tail=None
        elif self.head==item:
            if current.getNext()!=None:
                self.head=current.getNext()
                current.getNext().setPrev(None)
            else:
                self.head=None
                self.tail=None    
        else:
            while current.getData()!=item:
                previous=current
                current=current.getNext()
            current.getNext().setPrev(previous)
            previous.setNext(current.getNext())
        return self
    
    def insert(self,pos,item):
        temp=biNode(item)
        current=self.head
        if self.head==None and pos==0:
            temp.setNext(None)
            temp.setPrev(None)
            self.head=temp
            self.tail=temp
        elif pos==0:
            current.setPrev(temp)
            self.head=temp
            temp.setNext(current)
            temp.setPrev(None)
        elif pos==self.size():
            previous=self.tail
            previous.setNext(temp)
            temp.setNext(None)
            temp.setPrev(previous)
            self.tail=temp
        elif pos<self.size():
            previous=None
            count=0
            while count!=pos:
                previous=current
                current=current.getNext()
                count+=1
            current.setPrev(temp)
            previous.setNext(temp)
            temp.setNext(current)
            temp.setPrev(previous)
        else:
            print('Error!')
        return self

           
    def __str__(self):
        current=self.head
        out=[]
        while current!=None:
            out.append(current)
            current=current.getNext()
        return ' '.join([str(x) for x in out])
    
    __repr__=__str__
    
    def __getitem__(self,pos):
        current=self.head
        count=0
        while count!=pos:
            current=current.getNext()
            count+=1
        return current  
    
'''
mylist=biUnorderedList()
#mylist=OrderedList()
for i in range(0, 20, 2):
    mylist.append(i)  
print(mylist) 
print(mylist.add(3))
print(mylist.remove(6))
print(mylist.search(5))  # False
print(mylist.size())  # 10
print(mylist.index(2))  # 2
print(mylist.pop())  # 18
print(mylist)
print(mylist.pop(2))  # 2
print(mylist)  # [3, 0, 4, 8, 10, 12, 14, 16]
mylist.insert(3, "10")
print(mylist[4])  # 8
print(mylist)
while mylist.size()!=0:
    print(mylist.pop())
    
s=Stack()
print(s.isEmpty())
s.push(3)
s.push(5)
print(s)
print(s.peek())
print(s.size())
print(s.pop())
print(s.isEmpty())
'''