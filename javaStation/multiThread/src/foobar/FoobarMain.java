package foobar;

import java.util.concurrent.Semaphore;

//onlu the class foobar that can run. 

public class FoobarMain {
	Foobar f;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FoobarMain f=new FoobarMain();
		f.work();
	}
	
	public void work() {
	    foo=new Foobar();
		Thread t1,t2,t3;
		t1=new Thread(new Caller(foo,1));
		t2=new Thread(new Caller(foo,2));
		t2.start();
		t1.start();
	}
}

class Caller implements Runnable {
	Foobar f;
	int which;
	
	Caller(Foo f,int func) {
		this.f=f;
		this.which=func;

	}
	
	public void run()
	{
		try {
			switch(which)
			{
			case 1:
					f.first(new F());
				break;
			case 2:
				f.second(new S());
				break;
			case 3:
				f.third(new T());
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

class FooBar {

	Semaphore f=new Semaphore(1);
	Semaphore b=new Semaphore(0);
	private int n;

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
        	f.acquire();
        	// printFoo.run() outputs "foo". Do not change or remove this line.
        	printFoo.run();
        	b.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
        	b.acquire();
            // printBar.run() outputs "bar". Do not change or remove this line.
        	printBar.run();
        	f.release();
        }
    }
}

class F implements Runnable {

	public void run() {
		System.out.println("first");
	}

}

class S implements Runnable {

	public void run() {
		System.out.println("second");
	}

}

class T implements Runnable {

	public void run() {
		System.out.println("third");
	}

}