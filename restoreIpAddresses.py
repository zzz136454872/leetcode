from typing import *

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        out=[]
        if len(s)<4:
            return out
        for i in range(1,4):
            sub1=s[:i]
            #print('sub1',sub1)
            x=int(sub1)
            if sub1[0]=='0' and len(sub1)>1:
                break
            if x>255:
                break
            for j in range(i+1,min(i+4,len(s)-1)):
                sub2=s[i:j]
                #print('sub2',sub2)
                y=int(sub2)
                if sub2[0]=='0' and len(sub2)>1:
                    break
                if y>255:
                    break
                # print('sub21',sub2)
                for k in range(j+1,min(j+4,len(s))):
                    sub3=s[j:k]
                    # print('sub3',sub3)
                    if sub3[0]=='0' and len(sub3)>1:
                        break
                    z=int(sub3)
                    if z>255:
                        break
                    sub4=s[k:]
                    if sub4[0]=='0' and len(sub4)>1:
                        continue
                    w=int(sub4)
                    # print('sub4',sub4)
                    if w>255:
                        continue
                    out.append(sub1+'.'+sub2+'.'+sub3+'.'+sub4)
        return out

sl=Solution()
print(sl.restoreIpAddresses("100100"))

                    

                    
                





