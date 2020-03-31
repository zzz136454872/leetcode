package foo;

import java.util.concurrent.Semaphore;

public class FooMain {
	Foo foo;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FooMain f=new FooMain();
		f.work();
	}
	
	public void work() {
	    foo=new Foo();
		Thread t1,t2,t3;
		t1=new Thread(new Caller(foo,1));
		t2=new Thread(new Caller(foo,2));
		t3=new Thread(new Caller(foo,3));
		t2.start();
		t1.start();
		t3.start();
	}
}

class Caller implements Runnable {
	Foo f;
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

class Foo {

	Semaphore oneBeforeTwo=new Semaphore(0);
	Semaphore twoBeforeThree=new Semaphore(0);

    public Foo() {

    }

    public void first(Runnable printFirst) throws InterruptedException {
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        oneBeforeTwo.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
    	oneBeforeTwo.acquire();
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        twoBeforeThree.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
    	twoBeforeThree.acquire();
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
       
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