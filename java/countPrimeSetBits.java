import java.util.HashSet;
import java.util.Set;
import java.util.Arrays;

class Solution {
    public int countPrimeSetBits(int left, int right) {
        Integer [] primesArray={2,3,5,7,11,13,17,19,23,29};
        Set<Integer> primes=new HashSet<Integer>(Arrays.asList(primesArray));
        int out=0;
        for(int i=left;i<=right;i++) {
            if(primes.contains(Integer.bitCount(i))) {
                out++;
            }
        }
        return out;
    }

    public static void main(String[] args) {
        Solution sl=new Solution();
        int left=6;
        int  right = 10;
        System.out.println(sl.countPrimeSetBits(left,right));
    }
}

