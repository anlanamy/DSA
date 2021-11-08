#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 09:47:37 2021

@author: anlanamy
"""
import turtle
import random
def tree(branchLen,w,t):
    if branchLen > 5:
        t.down()
        l=random.randrange(branchLen-3,branchLen+2)
        r1=random.randrange(15,45)
        r2=random.randrange(15,45)
        t.width(w)
        t.pencolor((162-3*w)/255,(205-5*w)/255,(90-w)/255)
        t.forward(l)
        t.right(r1)
        tree(branchLen-15,w-3,t)
        t.left(r1+r2)
        tree(branchLen-15,w-3,t)
        t.right(r2)
        t.up()
        t.backward(l)
def main():
    t=turtle.Turtle()
    myWin=turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75,12,t)
    myWin.exitonclick()
    
main()
    
