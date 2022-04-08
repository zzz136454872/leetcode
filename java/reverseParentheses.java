import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public String reverseParentheses(String s) {
        Stack<Character> stack=new Stack<>();
        Queue<Character> queue=new LinkedList<>();
        for(int i=0;i<s.length();i++) {
            char c=s.charAt(i);
            if(c==')') {
                while(stack.peek()!='(') {
                    queue.add(stack.pop());
                }
                stack.pop();
            } else {
                stack.push(c);
            }
            while(queue.size()>0)
                stack.push(queue.remove());
        }

        StringBuilder sb=new StringBuilder();
        for(Character c:stack) {
            sb.append(c);
        }
        return new String(sb);
    }


    public static void main(String[] args) {
        String s="(abcd)";
        s = "(u(love)i)";
        s = "(ed(et(oc))el)";
        Solution sl=new Solution();
        System.out.println(sl.reverseParentheses(s));
    }
}
