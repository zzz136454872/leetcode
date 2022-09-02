// wrong answer
public class LongestUnivaluePath {
    public static void main(String[] args) {
        TreeNode root=new TreeNode(4);
        root.left=new TreeNode(4);
        root.left.left=new TreeNode(4);
        root.left.left.left=new TreeNode(4);
        root.left.left.left.left=new TreeNode(4);
        root.left.right=new TreeNode(4);
        root.left.right.right=new TreeNode(4);
        root.left.right.right.right=new TreeNode(4);
        root.right=new TreeNode(4);
        

        System.out.println((new Solution()).longestUnivaluePath(root.left));
        System.out.println("done");
    }
}

public class TreeNode {
     int val;
     TreeNode left;
     TreeNode right;
     TreeNode() {}
     TreeNode(int val) { this.val = val; }
     TreeNode(int val, TreeNode left, TreeNode right) {
         this.val = val;
         this.left = left;
         this.right = right;
     }
 }

class Solution {
    public int longestUnivaluePath(TreeNode root) {
        if(root==null)
            return 0;
        return sub(root)[0]-1;
    }

    private int[] sub(TreeNode root) {
        int[] res=new int[]{1,1};
        int[] tmp1={0,0},tmp2={0,0};
        
        if(root.left!=null) {
            tmp1=sub(root.left);
            if(root.val==root.left.val) {
                res[1]=Math.max(res[1],1+tmp1[1]);
                res[0]=Math.max(1+tmp1[1],tmp1[0]);
            } else {
                res[0]=Math.max(res[0],tmp1[0]);
                tmp1[1]=0;
            }
        }

        if(root.right!=null) {
            tmp2=sub(root.right);
            if(root.val==root.right.val) {
                res[1]=Math.max(res[1],1+tmp2[1]);
                res[0]=Math.max(1+tmp2[1],tmp2[0]);
            } else {
                res[0]=Math.max(res[0],tmp2[0]);
                tmp2[1]=0;
            }
        }

        res[0]=Math.max(res[0],1 + tmp1[1]+tmp2[1]);
        return res;
    }
}

