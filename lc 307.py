# -*- coding: utf-8 -*-
# @Time    : 2019/9/16 8:51
# @Author  : LI Dongdong
# @FileName: lc 307.py

class NumArray:

    def __init__(self, nums):
        if len(nums)==0:
            return
        n=len(nums)*3
        self.value=[0]*n
        self.build_segment_tree(self.value,nums,0,0,len(nums)-1)
        self.right_end=len(nums)-1

    def build_segment_tree(self, value: list, nums: list, pos: int, left: int, right: int):
        if left == right:
            value[pos]=nums[left]
            return
        mid = (left + right) // 2
        self.build_segment_tree(value, nums, 2*pos+1, left, mid)
        self.build_segment_tree(value, nums, 2*pos+2, mid+1, right)
        value[pos]=value[2*pos+1] + value[2*pos+2]

    def update(self, i: int, val: int) -> None:
        self.updata_segment_tree(self.value,0,0,self.right_end,i,val)

    def updata_segment_tree(self,value:int,pos,left,right,index,new_value):
        if left==right and left==index:
            value[pos]=new_value
            return
        mid=(left+right)//2
        if index<=mid:
            self.updata_segment_tree(value,pos*2+1,left,mid,index,new_value)
        else:
            self.updata_segment_tree(value,pos*2+2,mid+1,right,index,new_value)
        value[pos]=value[pos*2+1]+value[pos*2+2]

    def sumRange(self, i: int, j: int) -> int:
        return self.sum_range_segment_tree(self.value,0,0,self.right_end,i,j)

    def sum_range_segment_tree(self,value,pos,left,right,qleft,qright):
        if qleft>right or qright<left:
            return 0
        if qleft<=left and qright>=right:
            return value[pos]
        mid=(left+right)//2
        return self.sum_range_segment_tree(value,pos*2+1,left,mid,qleft,qright)+self.sum_range_segment_tree(value,pos*2+2,mid+1,right,qleft,qright)



# Your NumArray object will be instantiated and called as such:
obj = NumArray([1,3,5])
param_2 = obj.sumRange(0,2)
print(param_2)
obj.update(1,2)
param_2 = obj.sumRange(0,2)
print(param_2)



