#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:13:40 2021

@author: anlanamy
"""

from pythonds.basic.stack import Stack

def infixToPrefix(infixexpr):
    prec={'*':3,'/':3,'+':2,'-':2,')':1}
    opStack=Stack()
    postfixList=[]
    tokenList=infixexpr.split()
    retokenList=reversed(tokenList)
    for token in retokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfixList.append(token)
        elif token==')':
            opStack.push(token)
        elif token=='(':
            topToken=opStack.pop()
            while topToken!=')':
                postfixList.append(topToken)
                topToken=opStack.pop()
        else:                    
            while (not opStack.isEmpty()) and (prec[opStack.peek()]>prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return ' '.join(reversed(postfixList))

print(infixToPrefix(input()))