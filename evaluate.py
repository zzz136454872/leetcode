from typing import List

# 不知道是哪个
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        knowledge=dict(knowledge)

        out=[]
        i=0
        while i<len(s):
            if s[i]=='(':
                j=i+1
                while s[j]!=')':
                    j+=1
                key=s[i+1:j]
                if key in knowledge:
                    out.append(knowledge[key])
                else:
                    out.append('?')
                i=j
            else:
                out.append(s[i])
            i+=1
        return ''.join(out)

# sl=Solution()
# s = "(name)is(age)yearsold"
# knowledge = [["name","bob"],["age","two"]]
# print(sl.evaluate(s,knowledge))

