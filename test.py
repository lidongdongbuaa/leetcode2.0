maxD = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
maxD.sort(key = lambda x: (x[1], x[0]), reverse= True )
print(maxD)