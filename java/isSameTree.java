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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null) {
            return q==null;
        }
        if(q==null) {
            return false;
        }
        if(p.val!=q.val) {
            return false;
        }
        return isSameTree(p.left,q.left)&&isSameTree(p.right,q.right);
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        System.out.println();
    }
}

