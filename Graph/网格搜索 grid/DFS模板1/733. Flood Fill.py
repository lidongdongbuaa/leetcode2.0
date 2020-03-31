#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 20:46
# @Author  : LI Dongdong
# @FileName: 733. Flood Fill.py
''''''
'''
题目分析
1.要求：An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
2.理解：given a node, color its neighbor, return colored imagine
3.类型：matrix search
4.确认输入输出及边界条件：
    input: image matrix, [[]]; start point [r, c], index from 0; node numb range? [1, 50]; the numb of color, range? [0, 65535]
    output: colored image matrix, [[]]
    corner case: start point out of image range? N; matrix is None or [[]]? No;
5.方法及方法分析：DFS, BFS
time complexity order: DFS = BFS (N)
space complexity order: BFS O(N/2) =  DFS O(N)
6.如何考
'''
'''
A. DFS
    Method
        1. from the start point to visit its neighbors by dfs(r, c, image, newColor)
            a. End: index out of image range or it has been colored or it is not color pixel
            b. change the visiting node color to new color
            b. visited 4 directional neighbor by dfs()
        3. return image
    time complexity: O(N), space complexity O(N)
易错点：不需要visited
    对右边界的判断，要小于等于len(image)和len(image[0])
'''


class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        startColor = image[sr][sc]
        self.dfs(sr, sc, image, newColor, startColor)
        return image

    def dfs(self, sr, sc, image, newColor, startColor):  # dfs to color all neighbor of start node
        if sr < 0 or sc < 0 or sr > len(image) - 1 or sc > len(image[0]) - 1 or image[sr][sc] == newColor or image[sr][
            sc] != startColor:
            return

        image[sr][sc] = newColor

        self.dfs(sr - 1, sc, image, newColor, startColor)
        self.dfs(sr + 1, sc, image, newColor, startColor)
        self.dfs(sr, sc - 1, image, newColor, startColor)
        self.dfs(sr, sc + 1, image, newColor, startColor)
        return


'''
test code
image = [[1,1,1],[1,1,0],[1,0,1]] sr = 1, sc = 1, newColor = 2
'''
x = Solution()
print(x.floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1))
print(x.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2))

'''
简化版
'''


class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        color = image[sr][sc]
        if newColor == color:  # start pixel color same as newColor
            return image

        def dfs(r, c):  # paint pixels
            if r < 0 or r > len(image) - 1 or c < 0 or c > len(image[0]) - 1 or image[r][c] == newColor or image[r][
                c] != color:
                return

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        return

        dfs(sr, sc)
        return image


'''
B. BFS
    Method:
        1. adding starting cell to the queue
        2. poll a cell out of queue. keep putting all the valid neighbors in the queue
            the valid means in the inbound of the matrix and have same color with starting color 
    time complexity O(N) space complexity (N/2) = O(N)
    易错点： corner case:image[sr][sc] = newColor
'''


class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        if image[sr][sc] == newColor:  # corner case
            return image

        color = image[sr][sc]
        from collections import deque
        queue = deque([(sr, sc)])
        image[sr][sc] = newColor

        while queue:
            r, c = queue.popleft()
            if r - 1 >= 0 and image[r - 1][c] == color:
                queue.append([r - 1, c])
                image[r - 1][c] = newColor
            if r + 1 <= len(image) - 1 and image[r + 1][c] == color:
                queue.append([r + 1, c])
                image[r + 1][c] = newColor
            if c - 1 >= 0 and image[r][c - 1] == color:
                queue.append([r, c - 1])
                image[r][c - 1] = newColor
            if c + 1 <= len(image[0]) - 1 and image[r][c + 1] == color:
                queue.append([r, c + 1])
                image[r][c + 1] = newColor
        return image
