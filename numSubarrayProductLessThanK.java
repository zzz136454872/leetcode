import java.util.HashSet;
import java.util.Set;
import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import static javaUtils.Tools.println;

class Solution {

    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int res=0;
        int j=0;
        int tmp=1;
        for(int i=0;i<nums.length;i++) {
            while(j<nums.length&&tmp*nums[j]<k) {
                tmp*=nums[j++];
                println("inside "+j + " " +tmp);
            }
            res+=j-i;
            println("outer "+i + " " +j);
            if(j>i) 
                tmp/=nums[i];
            else
                j++;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        int []nums = {10,5,2,6}; 
        int k = 0;
        System.out.println(sl.numSubarrayProductLessThanK(nums,k));
    }

}

