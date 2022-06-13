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
    public int heightChecker(int[] heights) {
        int[] s=Arrays.copyOf(heights,heights.length);
        Arrays.sort(s);
        int res=0;
        for(int i=0;i<heights.length;i++) {
            if(s[i]!=heights[i]) 
                res+=1;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        int[] heights = {1,1,4,2,1,3};
        System.out.println(sl.heightChecker(heights));
    }
}

