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
    public int consecutiveNumbersSum(int n) {
        int i=1;
        int res=0;
        n*=2;

        while (i*i<n) {
            if (n%i==0&&((i%2)^((n/i)%2))==1) {
                res+=1;
            }
            i++;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        int n = 5;
        n=9;
        n=15;
        n=6;
        System.out.println(sl.consecutiveNumbersSum(n));
    }
}

