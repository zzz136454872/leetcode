from typing import *

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old=image[sr][sc]
        if old==newColor:
            return image
        self.image=image
        self.refresh(sr,sc,old,newColor)
        return self.image

    def refresh(self,i,j,old,new):
        if i<0 or j<0 or i>=len(self.image) or j>= len(self.image[0]):
            return 
        if self.image[i][j]!=old:
            return 
        self.image[i][j]=new
        self.refresh(i-1,j,old,new)
        self.refresh(i+1,j,old,new)
        self.refresh(i,j-1,old,new)
        self.refresh(i,j+1,old,new)

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
sl=Solution()
print(sl.floodFill(image,sr,sc,newColor))

