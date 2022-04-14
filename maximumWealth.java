import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;
import java.util.Deque;
import java.lang.Math

class Solution {
    public int maximumWealth(int[][] accounts) {
        int out=0;
        for(int[] user:accounts) {
            out=Math.max(out,Arrays.stream(user).sum());
        }
        return out;
    }
    public static void main(String[] args) {
        Solution sl=new Solution();
        System.out.println();
    }
}

