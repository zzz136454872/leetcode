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
import java.util.Collections;
import static javaUtils.Tools.println;
import javaUtils.TreeNode;

class Solution {
    List<Integer> res;

    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        res=new ArrayList<>();
        travel(root1);
        travel(root2);
        Collections.sort(res);
        return res;
    }

    private void travel(TreeNode root) {
        if(root==null) 
            return;
        travel(root.left);
        res.add(root.val);
        travel(root.right);
    }

    public static void main(String[] args) {
        TreeNode root1=TreeNode.fromStringArray("[2,1,4]");
        TreeNode root2=TreeNode.fromStringArray("[1,0,3]");
        Solution sl=new Solution();
        System.out.println(sl.getAllElements(root1,root2));
    }
}

