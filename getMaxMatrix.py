from typing import *

class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        m=-123456789
        log=[0,0,0,0]
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)+1):
                if i==j-1:
                    tmp=[0 for i in range(len(matrix[0]))]
                for k in range(len(matrix[0])):
                    tmp[k]+=matrix[j-1][k]
                #print(i,j,tmp)
                tmp_sum=-1
                for k in range(len(tmp)):
                    #print(k,start,tmp_sum)
                    if tmp_sum<=0:
                        tmp_sum=tmp[k]
                        start=k
                        end=k
                    else:
                        tmp_sum+=tmp[k]
                    if tmp_sum>m:
                        m=tmp_sum
                        end=k
                        log=[i,start,j-1,end]
                #print(m)
        return log

inp=[[9,-8,1,3,-2],[-3,7,6,-2,4],[6,-4,-4,8,-7]]


sl=Solution()
print(sl.getMaxMatrix(inp))
                            


                    

                   


