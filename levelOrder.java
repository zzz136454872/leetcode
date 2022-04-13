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
    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> out=new ArrayList<>();
        if (root == null) {
            return out;
        }
        List<Node> lis=new ArrayList<>();
        lis.add(root);
        while(lis.size()>0) {
            List<Node> newList=new ArrayList<>();
            List<Integer> tmp=new ArrayList<>();
            for(Node node:lis) {
                tmp.add(node.val);
                if(node.children!=null) {
                    for (Node nn:node.children) {
                        newList.add(nn);
                    }
                }
            }
            lis=newList;
            out.add(tmp);
        }
        return out;
    }

    public static void main(String[] args) {
        Node root=new Node(1);
        Solution sl=new Solution();
        System.out.println(sl.levelOrder(root));
    }
}

