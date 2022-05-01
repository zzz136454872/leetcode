package javaUtils;

import java.util.Deque;
import java.util.LinkedList;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode() {}
    public TreeNode(int val) { this.val = val; }
    public TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    public static TreeNode fromStringArray(String a) {
        if (a.equals("[null]")) {
            return null;
        }
        // System.out.println("a "+a);
        String[] values=a.split(", ?");
        values[0]=values[0].substring(1);
        values[values.length-1]=values[values.length-1].substring(0,values[values.length-1].length()-1);
        // System.out.println("values[0] "+values[0]);

        TreeNode root=new TreeNode(Integer.valueOf(values[0]));
        Deque<TreeNode> queue=new LinkedList<>();
        queue.add(root);
        // for(int i=0;i<values.length;i++) {
            // System.out.println(i+" "+values[i]);
        // }
        int i=1;
        while (i<values.length) {
            TreeNode now=queue.poll();
            String v=values[i];
            if (!v.equals("null")) {
                now.left=new TreeNode(Integer.valueOf(values[i]));
            }
            i++;
            if(i==values.length)
                break;
            v=values[i];
            if (!v.equals("null")) {
                now.right=new TreeNode(Integer.valueOf(values[i]));
            }
            queue.add(now.left);
            queue.add(now.right);
            i++;
        }
        return root;
    }

    public static void travel(TreeNode root,String order) {
        travelSub(root,order);
        System.out.println();
    }

    private static void travelSub(TreeNode root,String order) {
        if(root==null) 
            return;
        if(order.equals("pre"))
            System.out.print(root.val+" ");
        travelSub(root.left,order);
        if(order.equals("mid"))
            System.out.print(root.val+" ");
        travelSub(root.right,order);
        if(order.equals("post"))
            System.out.print(root.val+" ");
    }

    public static void main(String[] args) {
        String p = "[1,2,3,4,5]";
        TreeNode root = TreeNode.fromStringArray(p);
        if(root==null) {
            System.out.println("root is null");
        }
        travel(root,"pre");
        System.out.println("done");
    }
}
