import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public boolean patternMatching(String pattern, String value) {
        if(pattern.charAt(0)!='a') {
            pattern=pattern.replace("a","c").replace("b","a").replace("c","b");
        }
        int ca=0,cb=0;
        for(int i=0;i<pattern.length();i++) {
            if(pattern.charAt(i)=='a')
                ca++;
            else
                cb++;
        }
        for(int i=0;i<=value.length();i++) {
            int bt=value.length()-ca*i;
            if(bt<0)
                continue;
            if(cb!=0&&bt%cb!=0)
                continue;
            int bl=0;
            if(cb!=0) 
                bl=bt/cb;
            String a=value.substring(0,i);
            String tmp="";
            String b=null;
            for(int j=0;j<pattern.length();j++) {
                if(pattern.charAt(j)=='a') {
                    tmp+=a;
                } else {
                    if(b==null) {
                        System.out.println(value+pattern+i+j+i*j+bl);
                        b=value.substring(j*i,j*i+bl);
                    }
                    tmp+=b;
                }
            }
            if(tmp.equals(value)&&!a.equals(b))
                return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        String pattern = "abba", value = "dogcatcatdog";
        pattern = "abba";
        value = "dogcatcatfish";
        System.out.println(sl.patternMatching(pattern,value));
    }
}

