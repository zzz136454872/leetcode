from typing import *

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        table=[i for i in range(len(row)//2)]
        def find(a):
            if table[a]==a:
                return a
            return find(table[a])
        
        def union(a,b):
            fa=find(a)
            fb=find(b)
            if fb<fa:
                table[fa]=fb
            else:
                table[fb]=fa

        for i in range(0,len(row),2):
            union(row[i]//2,row[i+1]//2)
        circle=0
        for i in range(len(row)//2):
            if table[i]==i:
                circle+=1
        return len(row)//2-circle

sl=Solution()
row = [0, 2, 1, 3]
print(sl.minSwapsCouples(row))

