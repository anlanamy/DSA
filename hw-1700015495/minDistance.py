#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 10:44:56 2021

@author: anlanamy
"""

#l1=input()
#l2=input()
l1='algorithm'
l2='alligator'
m=len(l1)
n=len(l2)
edit=[list(range(0,(n+1)*20,20))]+[[(i+1)*20]+[0]*(n) for i in range(m)]
editProcedure=[['']+[('replicate '+l2[i]) for i in range(n)]]+[['replicate '+l1[i]]+[' ']*(n) for i in range(m)]
for i in range(2,m+1):
    editProcedure[i][0]=editProcedure[i-1][0]+' '+editProcedure[i][0]
for i in range(2,n+1):
    editProcedure[0][i]=editProcedure[0][i-1]+' '+editProcedure[0][i]
for i in range(1,m+1):
    for j in range(1,n+1):
        if l1[i-1]==l2[j-1]:
            edit[i][j]=edit[i-1][j-1]+5
            editProcedure[i][j]=editProcedure[i-1][j-1]+' replicate '+l1[i-1]
        else:
            edit[i][j]=min(edit[i-1][j]+20,edit[i][j-1]+20)
            if edit[i-1][j]<=edit[i][j-1]:
                editProcedure[i][j]=editProcedure[i-1][j]+' delete '+l1[i-1]
            else:
                editProcedure[i][j]=editProcedure[i][j-1]+' insert '+l2[j-1]
print('最小编辑距离得分为',edit[i][j])
print('编辑过程为',editProcedure[i][j])