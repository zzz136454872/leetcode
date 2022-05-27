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
    public int findClosest(String[] words, String word1, String word2) {
        int res=1234567;
        Map<String,List<Integer>> mem=new HashMap<>();
        for(int i=0;i<words.length;i++) {
            if(!mem.containsKey(words[i])) {
                mem.put(words[i],new ArrayList<>());
            }
            mem.get(words[i]).add(i);
        }
        List<Integer> l1=mem.get(word1);
        List<Integer> l2=mem.get(word2);
        int j=0;
        for(int i=0;i<l1.size();i++) {
            res=Math.min(res,Math.abs(l1.get(i)-l2.get(j)));
            while(l1.get(i)>l2.get(j)) {
                if(j==l2.size()-1)
                    break;
                j+=1;
                res=Math.min(res,Math.abs(l1.get(i)-l2.get(j)));
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        
        String []words = {"I","am","a","student","from","a","university","in","a","city"};
        String word1 = "a", word2 = "student";
        println(sl.findClosest(words,word1,word2));
        System.out.println();
    }
}

