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

    public int maximumGain(String s, int x, int y) {
        if (x<y) {
            int tmp=x;
            x=y;
            y=tmp;
            s=s.replace("a",".").replace("b","a").replace(".","b");
        }
        Deque<Character> s1=new LinkedList<>();
        Deque<Character> s2=new LinkedList<>();
        int out=0;
        // System.out.println(s);
        for(int i=0;i<s.length();i++) {
            char c=s.charAt(i);
            if(c!='b') {
                s1.add(c);
            } else {
                if(s1.size()>0 && s1.peekLast()=='a') {
                    s1.pollLast();
                    out+=x;
                } else {
                    s1.add(c);
                }
            }
        }
        // System.out.println(s1);
        // System.out.println(out);
        for(char c:s1) {
            if(c!='a') {
                s2.add(c);
            } else {
                if(s2.size()>0 && s2.peekLast()=='b') {
                    s2.pollLast();
                    out+=y;
                } else {
                    s2.add(c);
                }
            }
        }
        return out;
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        String s = "cdbcbbaaabab";
        int x = 4, y = 5;
        System.out.println(sl.maximumGain(s,x,y));
    }
}

