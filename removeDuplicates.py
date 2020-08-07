from typing import *


# 删除字符串中的所有相邻重复项
class Solution:
    def removeDuplicates(self, S: str) -> str:
        out=''
        for letter in S:
            if len(out)==0:
                out+=letter
            else:
                if letter==out[-1]:
                    out=out[:-1]
                else:
                    out+=letter
        return out
sl=Solution()
S="abbaca"
print(sl.removeDuplicates(S))


# 删除字符串中的所有相邻重复项
# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         stack=[]
#         counter=[]
#         count=0
#         for letter in s:
#             stack.append(letter)
#             if len(stack)==1:
#                 count=1
#             elif letter==stack[-2]:
#                 count+=1
#                 if count==k:
#                     stack=stack[:-k]
#                     if len(stack)>0:
#                         count=counter.pop()
#             else:
#                 counter.append(count)
#                 count=1
#         return ''.join(stack)
# s = "deeedbbcccbdaa"
# k = 3
# sl=Solution()
# print(sl.removeDuplicates(s,k))
            
