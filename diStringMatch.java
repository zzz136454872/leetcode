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
    public int[] diStringMatch(String s) {
        int[] res=new int[s.length()+1];
        int high=s.length();
        int low=0;
        if(s.charAt(0)=='I') {
            res[0]=low++;
        } else {
            res[0]=high--;
        }

        for(int i=1;i<s.length();i++) {
            if(s.charAt(i)=='I') {
                res[i]=low++;
            } else {
                res[i]=high--;
            }
        }
        res[s.length()]=low;
        return res;
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        String s = "IDID";
        s = "III";
        s = "DDI";
        println(sl.diStringMatch(s));
    }
}

