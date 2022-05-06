import java.util.LinkedList;
import java.util.Deque;

class RecentCounter {
    Deque<Integer> queue;

    public RecentCounter() {
        queue=new LinkedList<>();
    }
    
    public int ping(int t) {
        queue.addLast(t);
        while(queue.getFirst()<t-3000) {
            queue.removeFirst();
        }
        return queue.size();
    }

    public static void  main(String[] args) {
        RecentCounter rc=new RecentCounter();
        System.out.println(rc.ping(1));
        System.out.println(rc.ping(100));
        System.out.println(rc.ping(3001));
        System.out.println(rc.ping(3002));
    }

}
