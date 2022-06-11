
class Solution {
    private void show(int[] arr) {
        for(int i=0;i<arr.length;i++) {
            System.out.print(arr[i]+" ");
        }
        System.out.println();
    }

    public int minFlipsMonoIncr(String s) {
        int n=s.length();
        int c0[]=new int[n+1];
        int c1[]=new int[n+1];
        c0[0]=0;
        c1[n]=0;
        for(int i=0;i<n;i++) {
            if(s.charAt(i)=='0') 
                c0[i+1]=c0[i];
            else
                c0[i+1]=c0[i]+1;
        }
        for(int i=n-1;i>=0;i--) {
            if(s.charAt(i)=='0')
                c1[i]=c1[i+1]+1;
            else
                c1[i]=c1[i+1];
        }
        show(c0);
        show(c1);
        int res=n;
        for(int i=0;i<n+1;i++)
            res=Math.min(res,c0[i]+c1[i]);
        return res;
    }

    public static void main(String[] args) {
        String s = "00110";
        s = "010110";
        s = "00011000";
        Solution sl=new Solution();
        System.out.println(sl.minFlipsMonoIncr(s));
    }
}
