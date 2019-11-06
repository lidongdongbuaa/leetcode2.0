#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/5/30 14:50
#@Author: LI Dongdong
#@File  : lc51.py
import copy
class Solution:
    def solveNQueens(self, n):
        result=[]
        mark=[]
        location=[]
        for i in range(n):
            mark.append([])
            location.append([])
            for j in range(n):
                mark[i].append(0)
                location[i].append('.')
        self.generate(0,n,location,result,mark)
        return result

    def generate(self,k,n,location,result,mark):
        if k==n:
            resultpart=[]
            for i in range(len(location)):
                line=''
                for j in range(len(location)):
                    line=line+location[i][j]
                resultpart.append(line)
            result.append(copy.deepcopy(resultpart))
            return
        for i in range(n):
            if mark[k][i]==0:
                tmp_mark=copy.deepcopy(mark)
                location[k][i]='Q'
                self.put_down_the_queue(k,i,mark)
                self.generate(k+1,n,location,result,mark)
                mark=copy.deepcopy(tmp_mark)
                location[k][i]='.'

    def put_down_the_queue(self,x,y,mark):
        dx=[-1,1,0,0,-1,-1,1,1]
        dy=[0,0,-1,1,-1,1,-1,1]
        mark[x][y]=1
        for i in range(1,len(mark)):
            for j in range(8):
                new_x=x+i*dx[j]
                new_y=y+i*dy[j]
                if new_x>=0 and new_x< len(mark)and new_y>=0 and new_y<len(mark):
                    mark[new_x][new_y]=1




x=Solution()
print(x.solveNQueens(4))