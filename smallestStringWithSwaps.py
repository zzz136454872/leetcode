from typing import *

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n=len(s)
        flags=[i for i in range(n)]
        heights=[0 for i in range(n)]
        roots=[0 for i in range(n)]
        def find(loc):
            if flags[loc]==loc:
                return loc;
            flags[loc]=find(flags[loc]);
            return flags[loc];

        def merge(a,b):
            af=find(a);
            bf=find(b);
            if heights[af]>heights[bf]:
                flags[bf]=af;
            else:
                flags[af]=bf;
                if heights[af]==heights[bf]:
                    heights[bf]+=1;

        for i in range(len(pairs)):
            merge(pairs[i][0],pairs[i][1]);
        for i in range(n):
            roots[i]=find(i);
        
        table={}
        loc={}

        for i in range(n):
            r=roots[i]
            if r not in table.keys():
                table[r]=[ord(s[i])]
                loc[r]=[i]
            else:
                table[r].append(ord(s[i]))
                loc[r].append(i)
        for v in table.values():
            v.sort()
        out=['a' for i in range(n)]
        for k in table.keys():
            for j in range(len(table[k])):
                out[loc[k][j]]=chr(table[k][j])

        return ''.join(out);

sl=Solution()
s = "dcab"
pairs = [[0,3],[1,2],[0,2]]
print(sl.smallestStringWithSwaps(s,pairs))

    
