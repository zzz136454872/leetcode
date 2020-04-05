package diningPhilosophers;

import java.util.concurrent.Semaphore;

class DiningPhilosophers {
	Semaphore [] sList;

    public DiningPhilosophers() {
    	sList=new Semaphore[5];
    	for(int i=0;i<5;i++) {
    		sList[i]=new Semaphore(1);
    	}
    }

    // call the run() method of any runnable to execute its code
    public void wantsToEat(int philosopher,
                           Runnable pickLeftFork,
                           Runnable pickRightFork,
                           Runnable eat,
                           Runnable putLeftFork,
                           Runnable putRightFork) throws InterruptedException {
        if(philosopher%2==0) {
            sList[philosopher].acquire();
            pickLeftFork.run();
            sList[(philosopher+1)%5].acquire();
            pickRightFork.run();
        } 
        else {
            sList[(philosopher+1)%5].acquire();
            pickRightFork.run();
            sList[philosopher].acquire();
            pickLeftFork.run();
        }
        eat.run();
        if(philosopher%2==0) {
            putLeftFork.run();
            sList[philosopher].release();
            putRightFork.run();
            sList[(philosopher+1)%5].release();
        } 
        else {
            putRightFork.run();
            sList[(philosopher+1)%5].release();
            putLeftFork.run();
            sList[philosopher].release();
        }
    }
}