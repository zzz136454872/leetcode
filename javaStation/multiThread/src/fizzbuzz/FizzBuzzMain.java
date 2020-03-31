package fizzbuzz;

public class FizzBuzzMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FizzBuzzMain f=new FizzBuzzMain();
		f.work();
	}

	public void work() {
		FizzBuzz fb=new FizzBuzz(15);
		new Thread(new Caller(fb,1)).start();
		new Thread(new Caller(fb,2)).start();
		new Thread(new Caller(fb,3)).start();
		new Thread(new Caller(fb,4)).start();

	}
}

class FizzBuzz {
	private int n=1;
	private boolean finish=false;
	private int target;

	public FizzBuzz(int n) {
		this.target = n;
	}

	// printFizz.run() outputs "fizz".
	public void fizz(Runnable printFizz) throws InterruptedException {
		while(!finish)
		{
			if(n%3==0&&n%15!=0)
			{
				if(n==target)
					finish=true;
				printFizz.run();
				n++;
			}
		}
	}

	// printBuzz.run() outputs "buzz".
	public void buzz(Runnable printBuzz) throws InterruptedException {
		while(!finish)
		{
			if(n%3!=0&&n%5==0)
			{
				if(n==target)
					finish=true;
				printBuzz.run();
				n++;
			}
		}

	}

	// printFizzBuzz.run() outputs "fizzbuzz".
	public void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
		while(!finish)
		{
			if(n%15==0)
			{
				if(n==target)
					finish=true;
				printFizzBuzz.run();
				n++;
			}
		}
	}

	// printNumber.accept(x) outputs "x", where x is an integer.
	public void number(IntConsumer printNumber) throws InterruptedException {
		while(!finish)
		{
			if(n%3!=0&&n%5!=0)
			{
				if(n==target)
					finish=true;
				printNumber.accept(n);
				n++;
			}
		}
	}
}

class F implements Runnable {

	public void run() {
		System.out.println("fizz");
	}

}

class B implements Runnable {

	public void run() {
		System.out.println("buzz");
	}

}

class FB implements Runnable {

	public void run() {
		System.out.println("fizzbuzz");
	}

}

class IntConsumer {

	public void accept(int x) {
		System.out.println(x);
	}

}

class Caller implements Runnable {
	FizzBuzz f;
	int which;
	
	Caller(FizzBuzz f,int func) {
		this.f=f;
		this.which=func;
	}
	
	public void run()
	{
		try {
			switch(which)
			{
			case 1:
			    f.fizz(new F());
				break;
			case 2:
				f.buzz(new B());
				break;
			case 3:
				f.fizzbuzz(new FB());
				break;
			case 4:
				f.number(new IntConsumer());
				break;
			default:
				System.out.println("error");
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
}
