package zeroEvenOdd;

import java.util.concurrent.Semaphore;

class ZeroEvenOdd {
    private int n;
    Semaphore s0=new Semaphore(0);
    Semaphore so=new Semaphore(0);
    Semaphore se=new Semaphore(0);
    private int now=0;
    
    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
    	for(now=1;now<=n;now++)
    	{
    		printNumber.accept(0);
    		if(now%2==0)
    			se.release();
    		else
    			so.release();
    		s0.acquire();
    	}
        
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
    	for(int i=0;i<n/2;i++)
    	{
			se.acquire();
			printNumber.accept(now);
			s0.release();
    	}
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
    	for(int i=0;i<(1+n)/2;i++)
    	{
			so.acquire();
			printNumber.accept(now);
			s0.release();
    	}
    }
}

class IntConsumer {
	public void accept(int x) {
		System.out.println(x);
	}

}
