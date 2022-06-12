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
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        mem=new HashMap<>();
        List<Integer> pid=id(pattern);
        List<String> res=new ArrayList<>();
        for(int i=0;i<words.length;i++) {
            if(pid.equals(id(words[i]))) {
                res.add(words[i]);
            }
        }
        return res;
    }
    
    HashMap<Character,Integer> mem;

    private List<Integer> id(String word) {
        mem.clear();
        List<Integer> res=new ArrayList<>();
        int ctr=0;
        for(int i=0;i<word.length();i++) {
            if(mem.containsKey(word.charAt(i))) {
                res.add(mem.get(word.charAt(i)));
            } else {
                res.add(ctr);
                mem.put(word.charAt(i),ctr);
                ctr++;
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        String[] words = new String[]{"abc","deq","mee","aqq","dkd","ccc"};
        String pattern = "abb";
        System.out.println(sl.findAndReplacePattern(words,pattern));
    }
}

