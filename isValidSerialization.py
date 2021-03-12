from typing import *

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        po=preorder.split(',')
        if len(po)%2==0:
            return False
        if po[-1]!='#':
            return False
        n_count=0
        s_count=0
        for symbol in po[:-1]:
            if symbol=='#':
                s_count+=1
            else:
                n_count+=1
            if s_count>n_count:
                return False
        return True

sl=Solution()
inp="9,3,4,#,#,1,#,#,2,#,6,#,#"
print(sl.isValidSerialization(inp))

