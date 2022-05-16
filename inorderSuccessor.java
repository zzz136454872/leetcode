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
import javaUtils.TreeNode;

class Solution {
    boolean flag;
    TreeNode p;
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        flag=false;
        this.p=p;
        return sub(root);
    }

    private TreeNode sub(TreeNode root) {
        if(root==null)
            return null;
        if(root.val<p.val)
            return sub(root.right);
        if(root.val==p.val) {
            flag=true;
            return sub(root.right);
        }
        TreeNode tmp=sub(root.left);
        if(tmp!=null)
            return tmp;
        if(flag)
            return root;
        return null;
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        TreeNode root = TreeNode.fromStringArray("[2,1,3]");
        TreeNode p = new TreeNode(1);
        root = TreeNode.fromStringArray("[5,3,6,2,4,null,null,1]");
        p = new TreeNode(6);
        root = TreeNode.fromStringArray("[2,null,3]");
        p = new TreeNode(2);
        System.out.println(sl.inorderSuccessor(root,p).val);
    }
}

