class Solution {
    public int findInMountainArray(int target, MountainArray mountainArr) {
        int left=0,right=mountainArr.length()-1;
        int mid;
        while(left<=right) {
            mid=(left+right)/2;
            if(mountainArr.get(mid)>mountainArr.get(mid+1))
                right=mid-1;
            else
                left=mid+1;
        }
        int large=left;
        left=0;
        right=large;
        while(left<=right) {
            mid=(left+right)/2;
            int mv=mountainArr.get(mid);
            if(mv>target)
                right=mid-1;
            else if(mv<target)
                left=mid+1;
            else
                return mid;
        }

        left=large;
        right=mountainArr.length()-1;
        while(left<=right) {
            mid=(left+right)/2;
            int mv=mountainArr.get(mid);
            if(mv>target)
                left=mid+1;
            else if(mv<target)
                right=mid-1;
            else
                return mid;
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        int target=0;
        int[] v={1,5,2};
        M m=new M(v);
        System.out.println(sl.findInMountainArray(target,m));
    }
}

interface MountainArray {
    public int get(int index);
    public int length();
}

class M implements MountainArray{
    int[] a;

    M(int[] a) {
        this.a=a;
    }

    public int get(int index) {
        return a[index];
    }

    public int length() {
        return a.length;
    }
}
