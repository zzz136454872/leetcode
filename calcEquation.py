from typing import *

class Solution:
    def calcEquation(self, equations: List[List[str]],
            values: List[float], queries: List[List[str]]) -> List[float]:
        variable=set()
        for equation in equations:
            variable.add(equation[0])
            variable.add(equation[1])
        
        # variable=list(variable)
        distance={v1: {v2:1 if v1==v2 else -1
            for v2 in variable} for v1 in variable}
        
        
        for i in range(len(equations)):
            distance[equations[i][0]][equations[i][1]]=values[i]
            distance[equations[i][1]][equations[i][0]]=1/values[i]
        
        # print(distance)

        # 弗洛伊德
        for v3 in variable:
            for v1 in variable:
                for v2 in variable:
                    if distance[v1][v2]==-1 and \
                            distance[v1][v3]!=-1 and \
                            distance[v3][v2]!=-1:
                        distance[v1][v2]=distance[v1][v3]*distance[v3][v2]
                        # print(v1,v2,v3,distance[v1][v2])
        
        out=[-1 for q in queries]
        print(distance)
        for i in range(len(queries)):
            if queries[i][0] in variable and queries[i][1] in variable:
                out[i]=(distance[queries[i][0]][queries[i][1]])
        return out

sl=Solution()
equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

print(sl.calcEquation(equations,values,queries))
            
