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
    public int[] sortArrayByParity(int[] nums) {
        int i=0;
        int j=nums.length-1;
        while(i<j) {
            while(i<j&&nums[i]%2==0)
                i++;
            while(i<j&&nums[j]%2==1)
                j--;
            int tmp=nums[i];
            nums[i]=nums[j];
            nums[j]=tmp;
            i++;
            j--;
        }
        return nums;
    }

    public static void main(String[] args) {
        int[] nums = {3,1,2,4};
        nums=new int[]{0};
        Solution sl=new Solution();
        println(sl.sortArrayByParity(nums));
    }
}

