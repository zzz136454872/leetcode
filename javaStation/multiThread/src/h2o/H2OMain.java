package h2o;

import java.util.concurrent.Semaphore;

public class H2OMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		H2OMain hm=new H2OMain();
		hm.work();
	}
	
	public void work() {
		H2O h2o=new H2O();
		new Thread(new Caller(h2o,1)).start();
		new Thread(new Caller(h2o,1)).start();
		new Thread(new Caller(h2o,1)).start();
		new Thread(new Caller(h2o,1)).start();
		new Thread(new Caller(h2o,1)).start();
		new Thread(new Caller(h2o,1)).start();
		new Thread(new Caller(h2o,1)).start();
		new Thread(new Caller(h2o,1)).start();
		new Thread(new Caller(h2o,2)).start();
		new Thread(new Caller(h2o,2)).start();
		new Thread(new Caller(h2o,2)).start();
		new Thread(new Caller(h2o,2)).start();
	}

}


class H2O {
	Object oo=new Object();
	
	Semaphore hBeforeO=new Semaphore(0);
	Semaphore oBeforeH=new Semaphore(2);
	
    public H2O() {
        
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
		oBeforeH.acquire();
		// releaseHydrogen.run() outputs "H". Do not change or remove this line.
		releaseHydrogen.run();
		hBeforeO.release();
    }

    public synchronized void oxygen(Runnable releaseOxygen) throws InterruptedException {
    	hBeforeO.acquire();
    	hBeforeO.acquire();
        // releaseOxygen.run() outputs "O". Do not change or remove this line.
		releaseOxygen.run();
    	oBeforeH.release();
    	oBeforeH.release();
    }
}

class Caller implements Runnable {
	H2O h;
	int which;
	
	Caller(H2O h,int func) {
		this.h=h;
		this.which=func;
	}
	
	public void run()
	{
		try {
			switch(which)
			{
			case 1:
				h.hydrogen(new H());
				break;
			case 2:
				h.oxygen(new O());
				break;
			default:
				System.out.println("error");
			}
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
}

class H implements Runnable {

	public void run() {
		System.out.println("H");
	}

}

class O implements Runnable {

	public void run() {
		System.out.println("O");
	}

}
