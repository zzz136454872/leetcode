from typing import *

class Solution:
    def minSwaps(self, s: str) -> int:
        dic={'0':0,'1':0}
        for letter in s:
            dic[letter]+=1
        
        s0=dic['0']
        s1=dic['1']
        if abs(s0-s1)>1:
            return -1
        def count(sp):
            e=0
            for i in range(len(s)):
                if i%2==0:
                    if s[i]!=sp:
                        e+=1
                else: 
                    if s[i]==sp:
                        e+=1

            return e//2

        if s0==s1:
            return min(count('0'),count('1'))
        if s0>s1:
            return count('0')
        return count('1')

sl=Solution()
s="1000101011"
print(sl.minSwaps(s))

