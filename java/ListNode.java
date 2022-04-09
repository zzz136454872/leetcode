class ListNode {
    int val;
    ListNode prev=null,next=null;

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

    public void remove(ListNode node) {
        prev.next=next;
        next.prev=prev;
    }
}

