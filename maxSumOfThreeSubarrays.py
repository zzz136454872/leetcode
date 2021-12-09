from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        pre=[0]*(n+1)
        for i in range(n):
            pre[i+1]=pre[i]+nums[i]
        log=[0]*(n-k+1)
        for i in range(n-k+1):
            log[i]=pre[i+k]-pre[i]
        mem=[[(-1,0) for j in range(n-k+1)] for i in range(4)]
        print(mem)

        def search(start,count):
            print(start,count)
            if start>n-k:
                return (-123456789,-1)
            if count==0:
                return (0,-1)
            if mem[count][start][0]>0:
                return mem[count][start]
            s=0
            loc=-1
            for i in range(start,n-k+1-(k-1)*count):
                test=search(i+k,count-1)
                if pre[i]+test[0]>s:
                    s=pre[i]+test[0]
                    loc=test[1]
            mem[count][start]=(s,loc)
            return (s,loc)
        tmp=search(0,3)
        out=[tmp[1]]
        print(out)
        out.append(mem[2][out[-1]])
        out.append(mem[1][out[-1]])
        return out

nums = [1,2,1,2,6,7,5,1]
k = 2
print(Solution().maxSumOfThreeSubarrays(nums,k))

