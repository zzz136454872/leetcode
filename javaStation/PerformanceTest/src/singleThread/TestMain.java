package singleThread;

public class TestMain {
	static PerformanceTest p;
	String output;

	public static void main(String[] args) {
		p=new PerformanceTest();
		p.run();
	}
}
