package foo;

import java.util.concurrent.Semaphore;

public class FooMain {
	static Foo foo;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		foo=new Foo();
		try {
			foo.second(new S());
			foo.first(new F());
			foo.third(new T());;
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