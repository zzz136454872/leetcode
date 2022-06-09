
public class Solution {
    public ListNode sortList(ListNode head) {
        if(head==null||head.next==null) {
            return head;
        }
        ListNode p=head;
        ListNode q=head;
        ListNode prevP=head;
        while(q!=null) {
            prevP=p;
            p=p.next;
            q=q.next;
            if(q!=null) 
                q=q.next;
        }
        prevP.next=null;
        q=sortList(head);
        p=sortList(p);
        head=null;
        ListNode tail=null;
        if(p.val<q.val) {
            head=p;
            tail=p;
            p=p.next;
            tail.next=null;
        } else {
            head=q;
            tail=q;
            q=q.next;
            tail.next=null;
        }

        while(q!=null&&p!=null) {
            if(p.val<q.val) {
                tail.next=p;
                tail=p;
                p=p.next;
                tail.next=null;
            } else {
                tail.next=q;
                tail=q;
                q=q.next;
                tail.next=null;
            }
        }
        if(q!=null)
            tail.next=q;
        if(p!=null)
            tail.next=p;
        return head;
    }

    public static void main(String[] args) {
        // head = [4,2,1,3]
        ListNode a=new ListNode(4);
        ListNode b=new ListNode(2);
        ListNode c=new ListNode(1);
        ListNode d=new ListNode(3);
        a.next=b;
        b.next=c;
        c.next=d;
        ListNode.show(a);
        ListNode.show(new Solution().sortList(a));
    }
}

class ListNode {
    int val;
    ListNode next;
    public ListNode(int val) {
        this.val=val;
        next=null;
    }

    public static void show(ListNode n) {
        if(n==null)  {
            System.out.println();
            return;
        }
        System.out.print(n.val+ " ");
        show(n.next);
    }
}
