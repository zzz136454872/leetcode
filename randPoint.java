import static javaUtils.Tools.println;

class Solution {
    double x;
    double y;
    double r;

    public Solution(double radius, double x_center, double y_center) {
        x=x_center;
        y=y_center;
        r=radius;
    }
    
    public double[] randPoint() {
        double tmp=r*r+1;
        double xx=1;
        double yy=1;
        int i=0;
        while(tmp>r*r) {
            xx=2*r*Math.random()-r;
            yy=2*r*Math.random()-r;
            tmp=xx*xx+yy*yy;
            i+=1;
        }
        return new double[]{xx+x,yy+y};
    }

    public static void main(String[] args) {
        Solution sl=new Solution(1234793.7,73839.1,3289891.3);
        double[] res={0,0};
        for(int i=0;i<30000;i++) {
            double[] r=sl.randPoint();
            res[0]+=r[0];
            res[1]+=r[1];
        }
        println(res);
    }
}

