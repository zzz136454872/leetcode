
parent=[i for i in range(n)]

def find(a):
    if a==parent[a]:
        return a
    parent[a]=find(parent[a])
    return parent[a]

def union(a,b):
    aa=find(a)
    bb=find(b)
    parent[max(aa,bb)]=min(aa,bb)

def reduction():
    for i in range(len(parent)):
        find(i)
    
