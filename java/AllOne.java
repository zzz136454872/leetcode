import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;
import java.util.Deque;
import java.util.Map;
import java.util.HashMap;

class AllOne {
    ListNode head=new ListNode(-1);
    ListNode tail=new ListNode(-1);
    Map<String,ListNode> mem=new HashMap<>();
    
    public AllOne() {
        head.next=tail;
        head.ss.add("");
        tail.prev=head;
        tail.ss.add("");
    }
    
    public void inc(String key) {
        if (!mem.containsKey(key)) {
            if (head.next.val!=1) {
                ListNode newNode=new ListNode(1);
                head.insertAfter(newNode);
            }
            mem.put(key, head.next);
            head.next.ss.add(key);
        } else {
            ListNode node=mem.get(key);
            int c=node.val;
            node.ss.remove(key);
            if(node.next.val!=c+1) {
                ListNode newNode=new ListNode(c+1);
                node.insertAfter(newNode);
            }
            node.next.ss.add(key);
            mem.put(key,node.next);
            if (node.ss.size()==0)
                node.remove();
        }
    }
    
    public void dec(String key) {
        ListNode node=mem.get(key);
        int c=node.val;
        node.ss.remove(key);
        if(c==1) 
            mem.remove(key);
        else {
            if (node.prev.val!=c-1) {
                ListNode newNode=new ListNode(c-1);
                node.insertBefore(newNode);
            }
            node.prev.ss.add(key);
            mem.put(key,node.prev);
        }
        if(node.ss.size()==0)
            node.remove();
    }
    
    public String getMaxKey() {
        return tail.prev.ss.iterator().next();

    }
    
    public String getMinKey() {
        return head.next.ss.iterator().next();
    }

    public static void main(String[] args) {
        AllOne a=new AllOne();
        a.inc("hello");
        a.inc("hello");
        System.out.println(a.getMaxKey());
        System.out.println(a.getMinKey());
        a.inc("leet");
        System.out.println(a.getMaxKey());
        System.out.println(a.getMinKey());
    }
}

class ListNode {
    int val;
    ListNode prev=null,next=null;
    Set<String> ss=new HashSet<>();

    public ListNode(int val) {
        this.val=val;
    }

    public void insertAfter(ListNode node){
        node.prev=this;
        node.next=next;
        next.prev=node;
        next=node;
    }

    public void insertBefore(ListNode node) {
        node.prev=prev;
        node.next=this;
        prev.next=node;
        prev=node;
    }

    public void remove() {
        prev.next=next;
        next.prev=prev;
    }
}
