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
    public long numberOfWays(String s) {
        long z=0,o=0,zo=0,oz=0,zoz=0,ozo=0;
        for(int i=0;i<s.length();i++) {
            char c = s.charAt(i);
            if(c=='0') {
                zoz+=zo;
                oz+=o;
                z++;
            } else {
                ozo+=oz;
                zo+=z;
                o++;
            }
            // println("i: "+i+" s[i] "+c+" z: "+z+" o: "+o+" zo: "+zo+" oz: "+oz+" zoz: "+zoz+" ozo: "+ozo);
        }
        
        return zoz+ozo;
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        String s = "001101";
        s = "11100";
        System.out.println(sl.numberOfWays(s));
    }
}

