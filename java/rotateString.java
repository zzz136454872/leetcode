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
    public boolean rotateString(String s, String goal) {
        for(int i=0;i<s.length();i++) {
            if(goal.equals(s.substring(i)+s.substring(0,i))) {
                return true;
            }
        }
        return false;
    }
    public static void main(String[] args) {
        Solution sl=new Solution();
        String s = "abcde", goal = "cdeab";
        System.out.println(sl.rotateString(s,goal));
    }
}

