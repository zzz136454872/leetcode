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
    public static void main(String[] args) {
        Solution sl=new Solution();
        String []words = {"gin", "zen", "gig", "msg"};
        
        System.out.println(sl.uniqueMorseRepresentations(words));
    }

    private String[] table={".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};

    private String translate(String a) {
        String out="";
        for(int i=0;i<a.length();i++) { out+=table[a.charAt(i)-'a'];
        }
        return out;
    }
        
    public int uniqueMorseRepresentations(String[] words) {
        Set<String> s=new HashSet<>();
        for(String word:words)
            s.add(translate(word));
        return s.size();
    }
}

