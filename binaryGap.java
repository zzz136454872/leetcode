import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;
import java.util.Deque;
import static javaUtils.Tools.println;

class Solution {
    public int binaryGap(int n) {
        int i=0;
        int res=0;
        int last=-1;
        while((1<<i)<=n) {
            if(((1<<i)&n)!=0) {
                if(last!=-1) {
                    res=Math.max(res,i-last);
                }
                last=i;
            }
            i++;
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        int n=22;
        // n=8;
        n=5;
        println(sl.binaryGap(n));
    }
}

