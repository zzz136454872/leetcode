class Solution:
    def maxDiff(self, num: int) -> int:
        if num ==0:
            return 9
        numstr=str(num)
        i=0
        while i<len(numstr) and numstr[i]=='9':
            i+=1
        if i==len(numstr):
            up=num
        else:
            up=int(numstr.replace(numstr[i],'9'))
        i=0
        while i<len(numstr) and (numstr[i]=='1' or numstr[i]=='0'):
            i+=1
        if len(numstr)==i:
            down=num
        else:
            if i==0:
                down=int(numstr.replace(numstr[i],'1'))
            else:
                down=int(numstr.replace(numstr[i],'0'))
        print(up)
        print(down)
        print(num)
        return up-down

sl=Solution()
print(sl.maxDiff(1101057))

