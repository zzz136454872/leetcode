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
import java.util.Random;
import static javaUtils.Tools.println;

class Solution {
    Map<Integer,List<Integer>> mem=new HashMap<>();
    Random rd=new Random();

    public Solution(int[] nums) {
        for(int i=0;i<nums.length;i++) {
            int num=nums[i];
            if(mem.containsKey(num)) {
                mem.get(num).add(i);
            } else {
                List<Integer> tmp = new ArrayList<>();
                tmp.add(i);
                mem.put(num,tmp);
            }
        }
    }
    
    public int pick(int target) {
        List<Integer> now=mem.get(target);
        return now.get(rd.nextInt(now.size()));
    }

    public static void main(String[] args) {
        int[] nums = new int[] {1,2,3,3,3};
        Solution sl=new Solution(nums);
        println(sl.pick(3));
        println(sl.pick(1));
    }
}

