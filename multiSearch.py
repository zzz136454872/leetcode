from typing import *

#tle
class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        out=[]
        index=[[] for i in range(26)]
        def l2n(a):
            return ord(a)-ord('a')
        def n2l(a):
            return 
        for i in range(len(big)):
            index[l2n(big[i])].append(i)
        # print(index)
        for small in smalls:
            if len(small)==0:
                out.append([])
                continue
            tmp=[]
            for sp in index[l2n(small[0])]:
                flag=True
                for j in range(1,len(small)):
                    if sp+j>=len(big) or small[j]!=big[sp+j]:
                        flag=False
                        break
                if flag:
                    tmp.append(sp)
            out.append(tmp)
        return out

sl=Solution()
big = "mississippi"
smalls = ["is", "ppi","hi","sis","i","ssippi"]
print(sl.multiSearch(big,smalls))


                

