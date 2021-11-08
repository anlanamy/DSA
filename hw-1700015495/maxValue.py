#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 10:29:48 2021

@author: anlanamy
"""

#import ast
#treasure=ast.literal_eval(input())#接受形为[{'w':2,'v':3},{'w':3,'v':4}]的字符串输入
treasure=[{'w':2,'v':3},{'w':3,'v':4},{'w':4,'v':8},{'w':5,'v':8},{'w':9,'v':10}]
package=[0]*21
treasureUsed=['']*21
for i in range(len(treasure)):
    packagecopy=package[:]
    if treasure[i]['w']<=20:
        for j in range(treasure[i]['w'],21):
            package[j]=max(packagecopy[j-treasure[i]['w']]+treasure[i]['v'],packagecopy[j])
            if packagecopy[j-treasure[i]['w']]+treasure[i]['v']>packagecopy[j]:
                treasureUsed[j]=treasureUsed[j-treasure[i]['w']]+'treasure '+str(i)+';'
print('宝物最高价值为',package[20])
print('使用的宝物为',treasureUsed[20])