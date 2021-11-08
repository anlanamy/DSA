#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 15:45:20 2021

@author: anlanamy
"""

import turtle
t=turtle.Turtle()
n=4
l=100
x=l/(2*n+1)
def hilbert(n,m,t):
    if n==1:
        t.forward(x)
        t.right(180*m+90)
        t.forward(x)
        t.right(180*m+90)
        t.forward(x)
    else:
        hilbert(n-1,1-m,t)
        if n%2==0:  
            t.right(180*m+90)
            t.forward(x)
        else:
            t.forward(x)
            t.right(180*m+90)           
        hilbert(n-1,m,t)
        if n%2==0:
            t.left(180*m+90)
            t.forward(x)
            t.left(180*m+90)
        else:
            t.forward(x)          
        hilbert(n-1,m,t)
        if n%2==0:
            t.forward(x)
            t.right(180*m+90)
        else:
            t.right(180*m+90)
            t.forward(x)
        hilbert(n-1,1-m,t)
hilbert(n,0,t)
