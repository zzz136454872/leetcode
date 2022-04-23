from typing import List


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort()
        stack=[]
        n=len(trees)
        used=[True]*n

        def product(a,b):
            out=a[0]*b[1] - a[1]*b[0]
            print(a,b,out)
            return out

        def anti_clock(a,b,c):
            out= product([b[0]-a[0],b[1]-a[1]],[c[0]-a[0],c[1]-a[1]])>0
            print(a,b,c,out)
            return out


        for i in range(len(trees)):
            while len(stack)>=2 and anti_clock(trees[stack[-2]],trees[stack[-1]],trees[i]):
                used[stack.pop()]=False
            stack.append(i)
        
        print('trees',trees)
        print('stack',stack)
        print('used',used)
        used[0]=False

        upper=len(stack)
        
        for i in range(len(trees)-1,-1,-1):
            if used[i]:
                continue
            while len(stack)>upper and anti_clock(trees[stack[-2]],trees[stack[-1]],trees[i]):
                stack.pop()
            stack.append(i)
        
        return [trees[i] for i in stack[1:]]
            
inp=[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
inp=[[1,2],[2,2],[4,2]]
inp=[[0,0],[0,100],[100,100],[100,0],[50,50]]

print(Solution().outerTrees(inp))
