#include<iostream>

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))

using namespace std;

class Solution 
{
public:
    int superEggDrop(int K,int N)
    {
        this->K=K;
        this->N=N;
        log=new int[(K+1)*(N+1)];
        for(int i=0;i<K+1;i++)
        {
            for(int j=0;j<N+1;j++)
            {
                log[i*N+j]=-1;
            }
        }
        return count(K,N);
    }
        
    int count(int k,int n)
    {
        if(n==0)
            return 0;
        if(k==1)
            return n;
        int out=log[k*N+n];
        if(out!=-1)
            return out;
        out=10000000;
        int low=1;
        int high=n;
        int mid,broke,nb;
        while(low<=high)
        {
            mid=(low+high)/2;
            broke=count(k-1,mid-1);
            nb=count(k,n-mid);
            if(broke > nb)
            {
                high=mid-1;
                out=min(out,broke+1);
            }
            else
            {
                low=mid+1;
                out=min(out,nb+1);
            }
        }
        log[k*N+n]=out;
        return out;
    }
private:
    int *log;
    int K,N;
};

int main()
{
    Solution sl;
    cout<<sl.superEggDrop(4,10000)<<endl;
    return 0;
}

