#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:13:30 2021

@author: anlanamy
"""

import sys

class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
pars={'<html>':'</html>','<head>':'</head>','<title>':'</title>','<body>':'</body>'}
def htmlChecker(symbolHtml):
    h=Stack()
    l=[]
    status=False
    match=False
    for c in symbolHtml:
        if status:
            l.append(c)
        if c=='<':
            status=True
        if c=='>':
            status=False
            item=str(''.join(l))
            l=[]
            if match==False:
                h.push(item)
            else:
                if h.isEmpty():
                    return False
                if h.peek()==item:
                    h.pop()
                    match=False
                else:
                    return False  
                    
        if c=='/' and l==['/']:
            l=[]
            match=True
            
    else:
        return h.isEmpty()

"""
Htmlfile=[]   
try:
    while True:
        Htmlfile.append(input().split())
except:
    Htmlfile='\n'.join(Htmlfile)
print(Htmlfile,'\n')
"""
print('yes' if htmlChecker(input()) else 'no')
