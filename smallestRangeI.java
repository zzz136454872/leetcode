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

    public int smallestRangeI(int[] nums, int k) {
        Arrays.sort(nums);
        return Math.max(0,nums[nums.length-1]-nums[0]-2*k);
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        int[] nums = {1};
        int  k = 0;
        nums = new int[]{0,10};
        k = 2;
        System.out.println(sl.smallestRangeI(nums,k));
    }
}

