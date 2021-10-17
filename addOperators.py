from typing import List


#TLE
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def genOp(n):
            base=['+','-','*','']
            if n==0:
                return [[]]
            return [op+[no] for op in genOp(n-1) for no in base]

        ops=genOp(len(num)-1)
        out=[]
        for op in ops:
            expression=[]
            for i in range(len(op)):
                expression.append(num[i])
                expression.append(op[i])
            expression.append(num[-1])
            expression=''.join(expression)
            flag=True
            for i in range(len(expression)-1):
                if expression[i]=='0' and expression[i+1].isdigit() and (i==0 or not expression[i-1].isdigit()):
                    flag=False
            if not flag:
                continue
            if target==eval(expression):
                out.append(expression)
        return out

num = "123"
target = 6
num = "232"
target = 8
num = "105"
target = 5
num = "00"
target = 0
num = "3456237490"
target = 9191
# num="1000000009"
# target=9
output=Solution().addOperators(num,target)
print(output)
print(len(output))
                    
