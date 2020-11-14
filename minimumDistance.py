from typing import *

class Solution:
    # 此解法不正确
    def minimumDistance(self, word: str) -> int:
        def get_loc(a):
            num=ord(a)-ord('A')
            x=num//6
            y=num%6
            return (x,y)
            
        def get_distance(a,b):
            if a[0]==-1 or b[0]==-1:
                return 0
            return abs(a[0]-b[0])+abs(a[1]-b[1])

        if len(word)<3:
            return 0
        log_l=[0 for i in range(len(word)+1)]
        log_r=[0 for i in range(len(word)+1)]
        log_l[0]=(0,(-1,-1),(-1,-1))
        log_r[0]=(0,(-1,-1),(-1,-1))
        for i in range(len(word)):
            # print(i)
            loc=get_loc(word[i])
            dist_l_l=get_distance(log_l[i][1],loc)+log_l[i][0]
            dist_r_l=get_distance(log_r[i][1],loc)+log_r[i][0]
            if dist_l_l<dist_r_l:
                log_l[i+1]=(dist_l_l,loc,log_l[i][2])
            else:
                log_l[i+1]=(dist_r_l,loc,log_r[i][2])
            dist_l_r=get_distance(log_l[i][2],loc)+log_l[i][0]
            dist_r_r=get_distance(log_r[i][2],loc)+log_r[i][0]
            if dist_l_r<dist_r_r:
                log_r[i+1]=(dist_l_r,log_l[i][1],loc)
            else:
                log_r[i+1]=(dist_r_r,log_r[i][1],loc)
        print(log_l)
        print(log_r)
        return min(log_l[-1][0],log_r[-1][0])
word = "CAKE"
sl=Solution()
out=sl.minimumDistance(word)
print(out)
