import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;

class Solution {

    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        List<Set<Integer>> adjList=new ArrayList<>();
        for(int i=0;i<n;i++) {
            adjList.add(new HashSet<>());
        }
        for (int[] edge : edges) {
            adjList.get(edge[0]).add(edge[1]);
            adjList.get(edge[1]).add(edge[0]);
        }
        List<Integer> queue=new ArrayList<>();
        for(int i=0;i<n;i++) {
            if(adjList.get(i).size()<=1) {
                queue.add(i);
            }
        }
        List<Integer> preQueue=queue;
        while(queue.size()>0) {
            preQueue=queue;
            queue=new ArrayList<>();
            for(int node:preQueue) {
                for(int np:adjList.get(node)) {
                    adjList.get(np).remove(node);
                    if(adjList.get(np).size()==1) {
                        queue.add(np);
                    }
                }
            }
        }
        return preQueue;
    }

    public static void main(String[] args) {
        int n = 4;
        // int[][] edges = {{1,0},{1,2},{1,3}};
        n = 6;
        int[][] edges = {{3,0},{3,1},{3,2},{3,4},{5,4}};
        Solution sl=new Solution();
        System.out.println(sl.findMinHeightTrees(n,edges));
    }
}

