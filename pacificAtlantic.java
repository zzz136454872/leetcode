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
    private int[][] heights;
    private int m;
    private int n;
    private Deque<int[]> queue;
    private int[][] change = {{1,0},{-1,0},{0,1},{0,-1}};
    private int[][] mem;

    private void bfs(int flag) {
        while(queue.size()>0) {
            int[] now=queue.poll();
            if((mem[now[0]][now[1]]&flag)!=0)
                continue;
            mem[now[0]][now[1]]|=flag;
            for(int[] nxt:change) {
                int nx=nxt[0]+now[0];
                int ny=nxt[1]+now[1];
                if(nx>=0&&nx<m&&ny>=0&&ny<n&&heights[nx][ny]>=heights[now[0]][now[1]])
                    queue.add(new int[]{nx,ny});
            }
        }
    }

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        m=heights.length;
        n=heights[0].length;
        this.heights=heights;
        queue=new LinkedList<>();
        mem=new int[m][n];
        for(int i=0;i<m;i++)
            queue.add(new int[]{i,0});
        for(int j=1;j<n;j++)
            queue.add(new int[]{0,j});
        bfs(1);
        for(int i=0;i<m;i++)
            queue.add(new int[]{i,n-1});
        for(int j=0;j<n-1;j++)
            queue.add(new int[]{m-1,j});
        bfs(2);
        List<List<Integer>> res=new ArrayList<>();
        for(int i=0;i<m;i++) {
            for(int j=0;j<n;j++) {
                if(mem[i][j]==3) {
                    res.add(Arrays.asList(i,j));
                }
            }
        }

        return res;
    }
    
    public static void main(String[] args) {
        int [][]heights = {{1,2,2,3,5},{3,2,3,4,4},{2,4,5,3,1},{6,7,1,4,5},{5,1,1,2,4}};
        heights=new int[][]{{2,1},{1,2}};
        Solution sl=new Solution();
        System.out.println(sl.pacificAtlantic(heights));
    }
}

