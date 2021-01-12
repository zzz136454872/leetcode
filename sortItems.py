from typing import *

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        idx=max(group)+1
        for i in range(len(group)):
            if group[i]==-1:
                group[i]=idx
                idx+=1
        groupItems={}
        for i in range(len(group)):
            if group[i] not in groupItems.keys():
                groupItems[group[i]]=set()
            groupItems[group[i]].add(i)
        groupbefore={key:set() for key in groupItems.keys()}

        for i,before in enumerate(beforeItems):
            for b in before:
                if group[i]!=group[b]:
                    groupbefore[group[i]].add(group[b])
        groupnext={}
        for g1 in groupbefore.keys():
            for g2 in groupbefore[g1]:
                if g2 not in groupnext.keys():
                    groupnext[g2]=set()
                groupnext[g2].add(g1)
        
        # group 排序
        # visited=[key:False for key in groupItems.keys()]
        queue=[]
        grouporder=[]
        for key in groupbefore.keys():
            if len(groupbefore[key])==0:
                queue.append(key)
                # visited[key]=True
        while len(queue)>0:
            g=queue.pop(0)
            grouporder.append(g)
            if g in groupnext.keys():
                for g2 in groupnext[g]:
                    groupbefore[g2].discard(g)
                    if len(groupbefore[g2])==0:
                        queue.append(g2)
        # print(grouporder)
        
        # print(groupItems)
        if len(grouporder)!=len(groupItems):
            return []

        out=[]
        for g in grouporder:
            # 组内排序
            gout=[]
            gbefore={}
            gnext={}
            for item in groupItems[g]:
                gbefore[item]=set(filter(lambda x: x in groupItems[g],beforeItems[item]))

            for g1 in gbefore.keys():
                for g2 in gbefore[g1]:
                    if g2 not in gnext.keys():
                        gnext[g2]=set()
                    gnext[g2].add(g1)
            queue=[]
            for key in gbefore.keys():
                if len(gbefore[key])==0:
                    queue.append(key)
            # print(gbefore)
            # print(gnext)
            while len(queue)>0:
                g1=queue.pop(0)
                gout.append(g1)
                if g1 in gnext.keys():
                    for g2 in gnext[g1]:
                        gbefore[g2].discard(g1)
                        if len(gbefore[g2])==0:
                            queue.append(g2)
            if len(gout)!=len(groupItems[g]):
                # print(g,gout,groupItems[g])
                # print('error')
                return []
            out.extend(gout)

        return out

sl=Solution()
n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3],[],[4],[]]

print(sl.sortItems(n,m,group,beforeItems))

