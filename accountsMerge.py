from typing import *

#wrong answer
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        email2id={}
        id_list=[i for i in range(len(accounts))]
        
        # input: int
        def find(a):
            if  id_list[a]==a:
                return a
            return id_list[a]

        # input: int
        def union(a,b):
            a=find(a)
            b=find(b)
            if a>b:
                id_list[a]=b
            elif a<b:
                id_list[b]=a
        
        for i in range(len(accounts)):
            account=accounts[i]
            name=account[0]
            emails=account[1:]
            for email in emails:
                if email not in email2id.keys():
                    email2id[email]=i
                else:
                    j=email2id[email]
                    union(i,j)

        #print('email2id', email2id)
        #print('id_list',id_list)
        out=[]
        id2out={}
        for i in range(len(accounts)):
            account=accounts[i]
            name=account[0]
            emails=account[1:]
            for email in emails:
                loc=find(email2id[email])
                if loc not in id2out.keys():
                    id2out[loc]=len(out)
                    out.append([name, email])
                else:
                    if email2id[email]==i:
                        out[id2out[loc]].append(email)
        for i in range(len(out)):
            tmp=out[i]
            name=tmp[0]
            emails=tmp[1:]
            emails.sort()
            out[i]=[name]+emails
        return out

sl=Solution()
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

print(sl.accountsMerge(accounts))

