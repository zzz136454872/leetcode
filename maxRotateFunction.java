import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;
import java.util.Deque;

class Solution {

    public int maxRotateFunction(int[] nums) {
        int sum=0;
        int tmp=0;
        int n=nums.length;
        for(int i=0;i<n;i++) {
            sum+=nums[i];
            tmp+=nums[i]*i;
        }
        int res=tmp;
        for(int i=n-1;i>0;i--) {
            tmp=tmp+sum-n*nums[i];
            res=Math.max(res,tmp);
        }
        return res;
    }

    public static void main(String[] args) {
        int []nums = {4,3,2,6};
        Solution sl=new Solution();
        System.out.println(sl.maxRotateFunction(nums));
    }
}

