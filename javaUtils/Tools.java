package javaUtils;

import java.util.Arrays;

public class Tools {

    public static void print(Object o) {
        if(o==null) {
            print("null");
        }
        System.out.print(o.toString());
    }

    public static <T> void print(T[] arr) {
        if(arr==null) {
            print("null");
            return;
        }
        print("{");
        for(int i=0;i<arr.length;i++) {
            print(arr[i]);
            if(i!=arr.length-1)
                print(", ");
        }
        print("}");
    }

    public static void print(int[] arr) {
        print(Arrays.stream(arr).boxed().toArray());
    }

    public static void print(double[] arr) {
        print(Arrays.stream(arr).boxed().toArray());
    }

    public static void print(boolean[] arr) {
        Boolean[] tmp=new Boolean[arr.length];
        for(int i=0;i<arr.length;i++) {
            tmp[i]=Boolean.valueOf(arr[i]);
        }
        print(tmp);
    }

    public static <T> void print(T[][] arr) {
        print("{");
        for(int i=0;i<arr.length;i++) {
            print(arr[i]);
            if(i!=arr.length-1)
                print(", ");
        }
        print("}");
    }

    public static void print(int[][] arr) {
        print("{");
        for(int i=0;i<arr.length;i++) {
            print(arr[i]);
            if(i!=arr.length-1)
                print(", ");
        }
        print("}");
    }

    public static void println() {
        print("\n");
    }

    public static void println(Object s) {
        print(s);
        println();
    }

    public static void println(boolean[] arr) {
        print(arr);
        println();
    }

    public static void println(int a) {
        print(Integer.valueOf(a));
        print("\n");
    }

    public static void println(boolean a) {
        print(Boolean.valueOf(a));
        print("\n");
    }

    public static <T> void println(T[] arr) {
        print(arr);
        println();
    }

    public static void println(int[] arr) {
        print(arr);
        println();
    }

    public static void println(double[] arr) {
        print(arr);
        println();
    }

    public static void println(int[][] arr) {
        print(arr);
        println();
    }

    public static void main(String[] args) {
        int[] a={1,2,3};
        println(a);
        int[][] aa={{1,2,3},{3,4,5}};
        println(aa);
        System.out.println("done");
        boolean[] b={true,false};
        println(b);
    }
}
