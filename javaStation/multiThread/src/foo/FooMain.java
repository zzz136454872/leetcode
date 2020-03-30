package foo;

public class FooMain {
	static Foo foo;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
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

    public Foo() {

    }

    public void first(Runnable printFirst) throws InterruptedException {
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
    }

    public void third(Runnable printThird) throws InterruptedException {
        
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