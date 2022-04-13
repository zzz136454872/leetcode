import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.List;

class MagicDictionary {
    List<List<String>> mem;

    public MagicDictionary() {
        mem = new ArrayList<>(101);
        for (int i = 0; i < 101; i++)
            mem.add(new ArrayList<String>());
    }
    
    public void buildDict(String[] dictionary) {
        for(String s:dictionary) 
            mem.get(s.length()).add(s);
    }

    private int diff(String s1,String s2) {
        int count=0;
        for(int i=0;i<s1.length();i++) {
            if(s1.charAt(i)!=s2.charAt(i)) {
                count+=1;
                if(count>1)
                    return count;
            }
        }
        return count;
    }

    public boolean search(String searchWord) {
        for(String tmp:mem.get(searchWord.length())) {
            if(diff(tmp,searchWord)==1) {
                return true;
            }
        }
        return false;
    }
}

