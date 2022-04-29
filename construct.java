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
    int [][] grid;
    

    public Node construct(int[][] grid) {
        this.grid=grid;
        int n=grid.length;
        return sub(0,n,0,n);
    }

    public Node sub(int sx,int ex,int sy, int ey) {
        boolean same=true;
        int val=grid[sx][sy];
        for(int i=sx;i<ex;i++) {
            for(int j=sy;j<ey;j++) {
                if(grid[i][j]!=val) {
                    same=false;
                    break;
                }
            }
            if(!same) 
                break;
        }

        if(same) {
            if (val==0)
                return new Node(false, true);
            else
                return new Node(true,true);
        }
            
        int mx=(sx+ex)/2;
        int my=(sy+ey)/2;
        return new Node(false,false,
                        sub(sx,mx,sy,my),
                        sub(sx,mx,my,ey),
                        sub(mx,ex,sy,my),
                        sub(mx,ex,my,ey));
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        System.out.println();

    }
}

// Definition for a QuadTree node.
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;

    
    public Node() {
        this.val = false;
        this.isLeaf = false;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = null;
        this.topRight = null;
        this.bottomLeft = null;
        this.bottomRight = null;
    }
    
    public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
};

