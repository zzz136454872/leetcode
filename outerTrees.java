import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;
import java.util.Deque;
import static javaUtils.Tools.*;

class Solution {

    private int product(int[] a,int[]b) {
        return a[0]*b[1]-a[1]*b[0];
    }

    private boolean anti_clock(int[] a,int[] b,int[] c) {
        return product(new int[]{b[0]-a[0],b[1]-a[1]},
                       new int[]{c[0]-a[0],c[1]-a[1]})>0;
    }

    public int[][] outerTrees(int[][] trees) {
        Arrays.sort(trees,(a,b) -> {
            return (a[0]-b[0])*1000 + a[1]-b[1];
        });

        // print(trees);

        int n=trees.length;
        ArrayList<Integer> stack=new ArrayList<>();
        
        boolean[] used=new boolean[n];
        for(int i=0;i<n;i++)
            used[i]=true;

        for(int i=0;i<n;i++) {
            while(stack.size()>=2 && anti_clock(trees[stack.get(stack.size()-2)],trees[stack.get(stack.size()-1)],trees[i])) {
                used[stack.remove(stack.size()-1)]=false;
            }
            stack.add(i);
        }

        // System.out.println(stack);
        // print(used);

        used[0]=false;
        int upper=stack.size();
        for(int i=n-1;i>-1;i--) {
            if(used[i]) 
                continue;
            while(stack.size()>=Math.max(upper,2) && anti_clock(trees[stack.get(stack.size()-2)],trees[stack.get(stack.size()-1)],trees[i])) {
                stack.remove(stack.size()-1);
            }
            stack.add(i);
        }

        int[][] res= new int[stack.size()-1][];
        for(int i=0;i<stack.size()-1;i++) {
            res[i]=trees[stack.get(i)];
        }
        // System.out.println(stack.size());
        return res;
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        int[][] inp = {{1, 1}, {2, 2}, {2, 0}, {2, 4}, {3, 3}, {4, 2}};
        print(sl.outerTrees(inp));
        // System.out.println(sl.outerTrees(inp));
    }
}

