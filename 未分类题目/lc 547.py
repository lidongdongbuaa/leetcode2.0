# -*- coding: utf-8 -*-
# @Time    : 2019/9/13 7:55
# @Author  : LI Dongdong
# @FileName: lc 547.py

#定义的基本格式
class DisjointSet:
    def __init__(self,size_num):
        self.id=[]
        self.size=[]
        for i in range(size_num):
            self.id.append(i)
            #size表示某节点有几个子节点
            self.size.append(1)
        self.count=size_num

    def find(self, p):
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        # 此时返回id[p]和p是相同的
        return self.id[p]

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)

        if i == j:
            return

        if self.size[i]<self.size[j]:
            self.id[i]=j
            self.size[j]=self.size[j]+self.size[i]
        #i的规模大于或者等于j时，（尤其注意等于，此时相当于强制合并)
        elif self.size[i]>=self.size[j]:
            self.id[j]=i
            self.size[i]=self.size[i]+self.size[j]
        self.count=self.count-1


class Solution:
    def findCircleNum(self, M) -> int:
        disjoint_set=DisjointSet(len(M))
        for i in range(len(M)):
            for j in range(i+1,len(M)):
                if M[i][j]==1:
                    disjoint_set.union(i,j)
        return disjoint_set.count






#################### DFS法 #######################################
    # def findCircleNum(self, M) -> int:
    #     visit=[0]*(len(M))
    #     count=0
    #     for i in range(len(M)):
    #         if visit[i]==0:
    #             self.DFS(i,M,visit)
    #             count+=1
    #     return count
    #
    #
    #
    # def DFS(self,i,M,visit):
    #     visit[i]=1
    #     for j in range(len(M[i])):
    #         if visit[j]==0 and M[i][j]==1:
    #             self.DFS(j,M,visit)

################# 错误的找岛屿的DFS法 ####################################
    # def findCircleNum(self, M) -> int:
    #     count=0
    #     visit=[]
    #     for i in range(len(M)):
    #         visit.append([])
    #         for j in range(len(M[i])):
    #             visit[i].append(0)
    #
    #     for i in range(len(M)):
    #         for j in range(len(M[i])):
    #             if i!=j and M[i][j]==1 and visit[i][j]==0:
    #                 self.DFS(M,visit,i,j)
    #                 count+=1
    #             else:
    #                 continue
    #     return count
    #
    # def DFS(self,M,visit,x,y):
    #     visit[x][y]=1
    #     dx=[0,0,-1,1]
    #     dy=[-1,1,0,0]
    #     for i in range(len(dx)):
    #         new_x=x+dx[i]
    #         new_y=y+dy[i]
    #         if new_x>=0 and new_y>=0 and new_x<len(M) and new_y<len(M) and M[new_x][new_y]==1 and visit[new_x][new_y]==0:
    #             self.DFS(M,visit,new_x,new_y)
    #         else:
    #             continue


x = Solution()
print(x.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))
