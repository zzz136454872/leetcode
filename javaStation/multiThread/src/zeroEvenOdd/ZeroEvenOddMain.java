package zeroEvenOdd;

public class ZeroEvenOddMain {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ZeroEvenOddMain f=new ZeroEvenOddMain();
		f.work();
	}

	public void work() {
		ZeroEvenOdd zeo=new ZeroEvenOdd(5);
		new Thread(new Caller(zeo,1)).start();
		new Thread(new Caller(zeo,2)).start();
		new Thread(new Caller(zeo,3)).start();
	}
}

class Caller implements Runnable {
	ZeroEvenOdd z;
	int which;
	
	Caller(ZeroEvenOdd z,int func) {
		this.z=z;
		this.which=func;
	}
	
	public void run()
	{
		try {
			switch(which)
			{
			case 1:
			    z.zero(new IntConsumer());
				break;
			case 2:
			    z.odd(new IntConsumer());
				break;
			case 3:
			    z.even(new IntConsumer());
				break;
			default:
				System.out.println("error");
			}
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
}

